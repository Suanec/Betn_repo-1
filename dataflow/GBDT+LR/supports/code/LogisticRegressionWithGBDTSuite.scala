package com.weibo.datasys

import com.weibo.datasys.algorithms.GradientBoostingDecisionTrees
import com.weibo.datasys.algorithms.Optimization.Tron
import com.weibo.datasys.common._
import com.weibo.datasys.common.tree.TreeModelUtil
import org.apache.spark.mllib.classification.{LogisticRegressionModel, WeiBoLogisticRegression}
import org.apache.spark.mllib.evaluation.BinaryClassificationMetrics
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.tree.model.{GradientBoostedTreesModel, GradientBoostedTreesModelUtil}
import org.apache.spark.rdd.RDD
import org.apache.spark.sql.SparkSession

import scala.io.Source

/**
  * Created by wulei3 on 16/11/2.
  */
object LogisticRegressionWithGBDTSuite {

  def main(args: Array[String]) {

    val spark = SparkSession
      .builder
      .appName("LogisticRegressionWithGBDTSuite")
      .master("local[*]")
      .getOrCreate()

    val gbdtDataConf:String = "/Users/wulei3/IdeaProjects/spark-local-debug/gbdt.data.conf"
    val gbdtModelPath:String = "/Users/wulei3/IdeaProjects/spark-local-debug/GBDT.model.1.5.5"
    val lrDataConf:String = "/Users/wulei3/IdeaProjects/spark-local-debug/mds_feed_strategy_feature_engineering_gbdt.data.conf"
    val featureConf:String = "/Users/wulei3/IdeaProjects/spark-local-debug/mds_feed_strategy_feature_engineering_gbdt.feature.conf"
    val table:String = "mds_feed_strategy_feature_engineering_gbdt"
    val trainPath:String = "/Users/wulei3/IdeaProjects/spark-local-debug/debug_data.100"
    val whereStmt:String = ""
    val samplingRatio:String = "1:10"
    val hasIntercept:String = "true"
    val modelVersion:String = "20170207.1.5.5"
    val model_path:String = "/Users/wulei3/IdeaProjects/spark-local-debug/predict.model.20170207"
    val fieldDelimiter:String = "\t"

    val gbdtModel:GradientBoostedTreesModel = TreeModelUtil.loadGradientBoostedTreesModelFromFile(spark, gbdtModelPath)
    val weiboModel:GradientBoostedTreesModelUtil =
      new GradientBoostedTreesModelUtil(gbdtModel.algo, gbdtModel.trees, gbdtModel.treeWeights)
    val label_token:String = Source.fromFile(lrDataConf).getLines.toArray.filter(_.startsWith("@")).head
    val gbdtDcc = ParseConfFiles.loadDataConf(gbdtDataConf)
    val lrDcc = ParseConfFiles.loadDataConf(lrDataConf)
    val paramList = ParseConfFiles.getParamList(lrDcc, table)
    val fmc = ParseConfFiles.loadFeatureConf(featureConf)
    val idxs = ParseConfFiles.getColsID(lrDcc,fmc)
    val gbdtDcc_b = spark.sparkContext.broadcast(gbdtDcc)
    val lrDcc_b = spark.sparkContext.broadcast(lrDcc)
    val fmc_b = spark.sparkContext.broadcast(fmc)
    val idxs_b = spark.sparkContext.broadcast(idxs)
    val (mapLocalToGlobal:Map[String, Int], gbdtMaxIndex:Int) = TreeModelUtil.mapLocalNodeToGlobalId(gbdtModelPath)
    val b_mapLocalToGlobal = spark.sparkContext.broadcast(mapLocalToGlobal)

    val labelIndx:Int = label_token.split(':').last.toInt
    val sampledData:RDD[Array[String]] = spark.sparkContext.textFile(trainPath).map{
      case line:String =>
        line.split(fieldDelimiter)
    }
    /** Sampling should be done as EARLY as possible. */
    val trainData:RDD[LabeledPoint] = sampledData.map{
      splits:Array[String] =>
        val lrFeatures:String = DataMappor.SingleLineMappor(spark, lrDcc_b.value,fmc_b.value,idxs_b.value,paramList,splits)
        /** Generating GBDT features. */
        val gbdtFeatureValues:Array[Double] = DataMappor.getLabelPointsForGBDT(spark, gbdtDcc_b.value, splits)
        val leafNodes:Array[Int] = weiboModel.predictByIds(Vectors.dense(gbdtFeatureValues))
        val globalLeafNodes:Array[Int] = TreeModelUtil.gbdtLocalNodeIdToGlobalId(leafNodes, b_mapLocalToGlobal.value)
        //val lrMaxIndex:Int = fmc_b.value.values.map(_._2).toArray.flatten.map(_._idx).max
        val lrMaxIndex:Int = fmc_b.value.values.filterNot(_._1._category.equals("multimap"))
          .map(_._2).toArray.flatten.map(_._idx).max
        //val libsvmFeatures:String = GradientBoostingDecisionTrees.leafIdFormatting(leafNodes)(weiboModel)(lrMaxIndex)
        val libsvmFeatures:String = GradientBoostingDecisionTrees.globalNodeIdToLibsvm(globalLeafNodes)(lrMaxIndex)
        val features:String = lrFeatures + libsvmFeatures
        val label:String = if(splits(labelIndx).equals("-1")) "0" else splits(labelIndx)
        val lbString:String = label + " " + features
        val sparseMaxIndex:Int = lrMaxIndex + gbdtMaxIndex
        labelPointParser(lbString)(sparseMaxIndex)
    }

    val Array(trainRDD, crossRDD) = trainData.randomSplit(Array(0.9, 0.1))

    val optimizer = new Tron()
    val haveIntercept = hasIntercept.toBoolean

    val model:LogisticRegressionModel = new WeiBoLogisticRegression(optimizer)
      .setIntercept(haveIntercept)
      .run(trainRDD)
      .clearThreshold()

    val crossScoreAndLabels:RDD[(Double, Double)] = crossRDD.map{
      case lp:LabeledPoint =>
        val score:Double = model.predict(org.apache.spark.mllib.linalg.Vectors.dense(lp.features.toArray))
        lp.label match {
          case -1d => (score,0d)
          case _ => (score, lp.label)
        }
    }

    //scoreAndLabels.filter(x => x._1 == x._2).count / scoreAndLabels.count.toDouble
    val crossMetrics = new BinaryClassificationMetrics(crossScoreAndLabels)
    val crossAUC     = crossMetrics.areaUnderROC()

    model2file(model, model_path, haveIntercept, modelVersion)
    println("\nTraining set's AUC on cross validation data: " + crossAUC.toString + "\n")
    println("Model has been saved to local file system: " + model_path + "\n")

    0.asInstanceOf[AnyRef]

  }

  def model2file(_lrModel : LogisticRegressionModel,
                 _outPath : String,
                 haveIntercept:Boolean,
                 modelVersion:String) : Unit = {
    val writer = new java.io.PrintWriter(_outPath,"utf-8")
    var rst = ""
    rst += "version " + modelVersion + "\n"
    rst += "solver_type " + "L2R_LR\n"
    rst += "nr_class " + _lrModel.numClasses.toString + "\n"
    rst += "label " + "0 1" + "\n"
    rst += "nr_feature " + _lrModel.numFeatures.toString  + "\n"
    rst += "bias " + haveIntercept + "\n"
    writer.write(rst)
    rst = ""
    rst += "w \n"
    writer.write(rst)
    rst = ""
    writer.flush
    rst += _lrModel.weights.toArray.mkString("\n")
    if(haveIntercept) rst += "\n" + _lrModel.intercept.toString
    writer.write(rst)
    rst = ""
    writer.flush
    writer.close
  }

  def labelPointParser(lpString:String)(sparseMatrixSize:Int):LabeledPoint = {

    var label:Double = lpString.split(" ").head.toDouble
    label = if(label == -1.0) 0 else label

    val indexValue:Array[(Int, Double)] = lpString.split(" ").drop(1).map{
      case indexValue:String =>
        (indexValue.split(":")(0).toInt, indexValue.split(":")(1).toDouble)
    }

    LabeledPoint(label, Vectors.sparse(sparseMatrixSize + 1, indexValue.map(_._1), indexValue.map(_._2)))
  }

}

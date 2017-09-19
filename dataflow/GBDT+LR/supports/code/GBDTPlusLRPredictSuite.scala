package com.weibo.datasys

import com.weibo.datasys.algorithms.GradientBoostingDecisionTrees
import com.weibo.datasys.common._
import com.weibo.datasys.common.tree.TreeModelUtil
import org.apache.spark.mllib.classification.LogisticRegressionModel
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.tree.model.{GradientBoostedTreesModel, GradientBoostedTreesModelUtil}
import org.apache.spark.rdd.RDD
import org.apache.spark.sql.SparkSession

import scala.io.Source

/**
  * Created by wulei3 on 16/11/2.
  */
object GBDTPlusLRPredictSuite {

  def main(args: Array[String]) {

    val spark = SparkSession
      .builder
      .appName("LogisticRegressionWithGBDTSuite")
      .master("local[*]")
      .getOrCreate()

    val gbdtDataConf:String = "/Users/wulei3/IdeaProjects/spark-local-debug/gbdt.data.conf"
    val gbdtModelPath:String = "/Users/wulei3/IdeaProjects/spark-local-debug/gbdt1.gbdt.model"
    val dataPath:String = "/Users/wulei3/IdeaProjects/spark-local-debug/10-records.txt"
    val fieldDelimiter:String = "\t"
    val lrDataConf:String = "/Users/wulei3/IdeaProjects/spark-local-debug/mds_feed_strategy_feature_engineering_ranking_v13.data.conf"
    val featureConf:String = "/Users/wulei3/IdeaProjects/spark-local-debug/mds_feed_strategy_feature_engineering_ranking_v13.feature.conf"
    val table:String = "mds_feed_strategy_feature_engineering_ranking_v13"
    val lrModelPath:String = "/Users/wulei3/IdeaProjects/spark-local-debug/predict.model"

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
    val inputData:RDD[Array[String]] = spark.sparkContext.textFile(dataPath).map{
      line:String =>
        line.split(fieldDelimiter)
    }
    val predictData:RDD[LabeledPoint] = inputData.map{
      splits:Array[String] =>
        val lrFeatures:String = DataMappor.SparseVectorConstructor(spark, lrDcc_b.value,fmc_b.value,idxs_b.value,paramList,splits)
        /** Generating GBDT features. */
        val gbdtFeatureValues:Array[Double] = DataMappor.getLabelPointsForGBDT(spark, gbdtDcc_b.value, splits)
        val leafNodes:Array[Int] = weiboModel.predictByIds(Vectors.dense(gbdtFeatureValues))
        val globalLeafNodes:Array[Int] = TreeModelUtil.gbdtLocalNodeIdToGlobalId(leafNodes, b_mapLocalToGlobal.value)
        //val lrMaxIndex:Int = fmc_b.value.values.map(_._2).toArray.flatten.map(_._idx).max
        val lrMaxIndex:Int = fmc_b.value.values.filterNot(_._1._category.equals("multimap"))
          .map(_._2).toArray.flatten.map(_._idx).max
        //val libsvmFeatures:String = GradientBoostingDecisionTrees.leafIdFormatting(leafNodes)(weiboModel)(lrMaxIndex)
        val libsvmFeatures:String = GradientBoostingDecisionTrees.globalNodeIdToLibsvm(globalLeafNodes)(lrMaxIndex - 1)
        val sparseMaxIndex:Int = lrMaxIndex + gbdtMaxIndex
        val features:String = lrFeatures + libsvmFeatures
        val label:String = if(splits(labelIndx).equals("-1")) "0" else splits(labelIndx)
        val lbString:String = label + " " + features
        labelPointParser(lbString)(sparseMaxIndex)
        /**
        lbString
        val featureVector:org.apache.spark.mllib.linalg.Vector = featuresParser(features)(sparseMaxIndex)
        featureVector
          */
    }

    val lrModel:LogisticRegressionModel = lrModelLoader(lrModelPath).clearThreshold()
    val scoreAndLabels:RDD[(Double, Double)] = predictData.map{
      case lp:LabeledPoint =>
        (lrModel.predict(lp.features), lp.label)
    }

    scoreAndLabels.collect.foreach(println)
    predictData.collect.foreach(println)

    0.asInstanceOf[AnyRef]

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

  def featuresParser(features:String)(sparseMatrixSize:Int):org.apache.spark.mllib.linalg.Vector = {

    val indexValue:Array[(Int, Double)] = features.split(" ").map{
      case indexValue:String =>
        (indexValue.split(":")(0).toInt, indexValue.split(":")(1).toDouble)
    }

    val featureVector:org.apache.spark.mllib.linalg.Vector = Vectors.sparse(sparseMatrixSize + 1, indexValue.map(_._1), indexValue.map(_._2))
    featureVector
  }

  def lrModelLoader(path:String):LogisticRegressionModel = {
    val lines:Array[String] = scala.io.Source.fromFile(path).getLines().toArray
    val hasBias:Double = lines.filter(_.contains("bias")).head.split(" ").last.toDouble
    val bias:Double = if(hasBias == 1.0) lines.last.toDouble else 0.0
    val numFeatures:Int = lines.filter(_.contains("nr_feature")).head.split(" ").last.toInt
    val weights:Array[Double] = lines.slice(7, 7+numFeatures).map(_.toDouble)
    println(weights.head)
    println(weights.last)
    println(bias)
    new LogisticRegressionModel(
      Vectors.dense(weights), bias)
  }

}

package com.weibo.datasys

import com.weibo.datasys.algorithms.GradientBoostingDecisionTrees
import com.weibo.datasys.common._
import com.weibo.datasys.common.tree.TreeModelUtil
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.tree.model.{GradientBoostedTreesModel, GradientBoostedTreesModelUtil}
import org.apache.spark.rdd.RDD
import org.apache.spark.sql.SparkSession

/**
  * Created by wulei3 on 16/11/2.
  */
object GBDTPredictSuite {

  def main(args: Array[String]) {

    val spark = SparkSession
      .builder
      .appName("LogisticRegressionWithGBDTSuite")
      .master("local[*]")
      .getOrCreate()

    val gbdtDataConf:String = "/Users/wulei3/IdeaProjects/spark-local-debug/gbdt.data.conf"
    val gbdtModelPath:String = "/Users/wulei3/IdeaProjects/spark-local-debug/gbdt1.gbdt.model"
    val dataPath:String = "/Users/wulei3/IdeaProjects/spark-local-debug/new-single.txt"
    val fieldDelimiter:String = "\t"

    val gbdtModel:GradientBoostedTreesModel = TreeModelUtil.loadGradientBoostedTreesModelFromFile(spark, gbdtModelPath)
    val weiboModel:GradientBoostedTreesModelUtil =
      new GradientBoostedTreesModelUtil(gbdtModel.algo, gbdtModel.trees, gbdtModel.treeWeights)
    val gbdtDcc = ParseConfFiles.loadDataConf(gbdtDataConf)
    val gbdtDcc_b = spark.sparkContext.broadcast(gbdtDcc)
    val (mapLocalToGlobal:Map[String, Int], gbdtMaxIndex:Int) = TreeModelUtil.mapLocalNodeToGlobalId(gbdtModelPath)
    val b_mapLocalToGlobal = spark.sparkContext.broadcast(mapLocalToGlobal)

    val sampledRDD = spark.sparkContext.textFile(dataPath).map{
      case line:String =>
        line.split(fieldDelimiter)
    }
    /** Sampling should be done as EARLY as possible. */
    val trainData:RDD[String] = sampledRDD.map{
      splits:Array[String] =>
        /** Generating GBDT features. */
        val gbdtFeatureValues:Array[Double] = DataMappor.getLabelPointsForGBDT(spark, gbdtDcc_b.value, splits)
        val leafNodes:Array[Int] = weiboModel.predictByIds(Vectors.dense(gbdtFeatureValues))
        val globalLeafNodes:Array[Int] = TreeModelUtil.gbdtLocalNodeIdToGlobalId(leafNodes, b_mapLocalToGlobal.value)
        val gbdtFeatures:String = GradientBoostingDecisionTrees.globalNodeIdToLibsvm(globalLeafNodes)(0)
        gbdtFeatures
    }

    trainData.collect.foreach(println)
  }

}

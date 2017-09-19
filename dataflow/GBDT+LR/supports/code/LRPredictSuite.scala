package com.weibo.datasys

import com.weibo.datasys.common._
import org.apache.spark.rdd.RDD
import org.apache.spark.sql.SparkSession

import scala.io.Source

/**
  * Created by wulei3 on 16/11/2.
  */
object LRPredictSuite {

  def main(args: Array[String]) {

    val spark = SparkSession
      .builder
      .appName("LogisticRegressionWithGBDTSuite")
      .master("local[*]")
      .getOrCreate()

    //val dataPath:String = "/Users/wulei3/IdeaProjects/spark-local-debug/largeScale/10-records.txt"
    //val dataPath:String = "/data0/user/wulei3/highDimModel/10-records.txt"
    val dataPath:String = "/user/wulei3/outputs/10-records.txt"
    val fieldDelimiter:String = "\t"
    //val lrDataConf:String = "/Users/wulei3/IdeaProjects/spark-local-debug/largeScale/mds_feed_strategy_feature_engineering_ranking_v14.data.conf"
    val lrDataConf:String = "/data0/user/wulei3/highDimModel/mds_feed_strategy_feature_engineering_ranking_v14.data.conf"
    //val featureConf:String = "/Users/wulei3/IdeaProjects/spark-local-debug/largeScale/mds_feed_strategy_feature_engineering_ranking_v14.feature.conf"
    val featureConf:String = "/data0/user/wulei3/highDimModel/mds_feed_strategy_feature_engineering_ranking_v14.feature.conf"
    val table:String = "mds_feed_strategy_feature_engineering_ranking_v14"

    //val label_token:String = Source.fromFile(lrDataConf).getLines.toArray.filter(_.startsWith("@")).head
    val lrDcc = ParseConfFiles.loadDataConf(lrDataConf)
    val paramList = ParseConfFiles.getParamList(lrDcc, table)
    //val fmc = ParseConfFiles.loadFeatureConf(featureConf)
    println(".............Generating Feature Conf ..............")
    val fmc = ParseConfFiles.loadNewFeatureConf2(featureConf)
    println("=============Done Generating Feature Conf =========")
    val idxs = ParseConfFiles.getNewColsID(lrDcc)
    val lrDcc_b = spark.sparkContext.broadcast(lrDcc)
    val fmc_b = spark.sparkContext.broadcast(fmc)
    val idxs_b = spark.sparkContext.broadcast(idxs)

    //val labelIndx:Int = label_token.split(':').last.toInt
    val inputData:RDD[Array[String]] = spark.sparkContext.textFile(dataPath).map{
      line:String =>
        line.split(fieldDelimiter)
    }
    val predictData:RDD[String] = inputData.map{
      splits:Array[String] =>
        //val lrFeatures:String = DataMappor.SparseVectorConstructor(spark, lrDcc_b.value,fmc_b.value,idxs_b.value,paramList,splits)
        val lrFeatures:String = DataMappor.getSparseLibsvmForRecord(spark, lrDcc_b.value,fmc_b.value,idxs_b.value,paramList,splits)
        lrFeatures
    }

    predictData.collect.foreach(println)

    0.asInstanceOf[AnyRef]

  }

}

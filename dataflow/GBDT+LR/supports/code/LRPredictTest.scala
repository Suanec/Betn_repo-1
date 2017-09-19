package com.weibo.datasys

import com.weibo.datasys.common._
import org.apache.spark.rdd.RDD
import org.apache.spark.sql.SparkSession

/**
  * Created by wulei3 on 16/11/2.
  */
object LRPredictTest {

  def main(args: Array[String]) {

    val spark = SparkSession
      .builder
      .appName("LogisticRegressionWithGBDTSuite")
      .master("spark://10.77.16.120:7077")
      .getOrCreate()

    val dataPath:String = args(0)
    val fieldDelimiter:String = "\t"
    val lrDataConf:String = args(1)
    val featureConf:String = args(2)

    //val label_token:String = Source.fromFile(lrDataConf).getLines.toArray.filter(_.startsWith("@")).head
    val lrDcc = ParseConfFiles.loadDataConf(lrDataConf)
    val paramList = ParseConfFiles.getParamList(lrDcc, "")
    //val fmc = ParseConfFiles.loadFeatureConf(featureConf)
    val fmc = ParseConfFiles.loadNewFeatureConf2(featureConf)
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

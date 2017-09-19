package com.weibo.datasys

import com.weibo.datasys.common.tree.TreeModelUtil
import com.weibo.datasys.pipeline.MLRunnable
import org.apache.spark.mllib.tree.model.{DecisionTreeModel, GradientBoostedTreesModel, Node}
import org.apache.spark.sql.SparkSession

import scala.collection.mutable
import scala.io.Source

/**
  * Created by wulei3 on 16/10/25.
  */

object GBDTFeaturesCheckSuite extends MLRunnable{

  def run(spark:SparkSession, input:AnyRef, conf:Map[String,String]):AnyRef = {

    val gbdtDataConf:String = conf("gbdtDataConf")
    val gbdtModelPath:String = conf("gbdtModel")

    val gbdtModel:GradientBoostedTreesModel = TreeModelUtil.loadGradientBoostedTreesModelFromFile(spark, gbdtModelPath)

    val finalImpurityMap:mutable.Map[Int, Double] = mutable.Map[Int, Double]()

    for(i <- 0 until gbdtModel.numTrees) {
      val featureImpurityMap = fetchTreeFeatureImpurity(gbdtModel.trees(i))
      val treeWeight:Double  = gbdtModel.treeWeights(i)
      val weightedImpurity:Map[Int, Double]   = featureImpurityMap.mapValues(v => v * treeWeight).toMap
      finalImpurityMap ++= weightedImpurity
    }

    val featureNames:Array[String] = Source.fromFile(gbdtDataConf).getLines().toArray.filterNot{
      case s:String =>
        s.startsWith("#") ||
          s.startsWith("@") ||
          s.equals("") ||
          s.contains("persist") ||
          s.contains("multimap") ||
          s.contains("partition") ||
          s.contains("compound")
    }.map{
      case s:String =>
        val cols:Array[String] = s.split("@")
        val featureName:String = cols(1)
        featureName
    }

    val reducedFeatureImpurity:Array[String] = finalImpurityMap.toArray.groupBy(_._1).map{
      case (key:Int, value:Array[(Int, Double)]) =>
        val featureName:String = featureNames(key)
        //val meanImpurity:Double = value.map(_._2).sum / value.size
        val sumImpurity:Double = value.map(_._2).sum
        (featureName, sumImpurity)
    }.toArray
      .sortBy(_._2)
      .map{
      case (featureName:String, impurity:Double) =>
        featureName + "\t" + impurity.toString
    }

    println("GBDT selected features ordered by each feature's impurity:\n")
    println("Feature Name        Feature Impurity\n")
    //reducedFeatureImpurity.foreach(println)
    var inverseIndx:Int = reducedFeatureImpurity.size - 1
    while(inverseIndx >= 0) {
      println(reducedFeatureImpurity(inverseIndx))
      inverseIndx -= 1
    }
    println("\n")

    0.asInstanceOf[AnyRef]
  }

  def fetchTreeFeatureImpurity(tree:DecisionTreeModel):mutable.Map[Int, Double] = {
    val featureImpurityMap:mutable.Map[Int, Double] = mutable.Map[Int, Double]()

    recursiveFeed(tree.topNode, featureImpurityMap)

    featureImpurityMap
  }

  def recursiveFeed(node:Node, featureImpurityMap:mutable.Map[Int, Double]):Unit = {

    if(!node.isLeaf) {

      val featureIndx:Int        = node.split.get.feature
      val featureImpurity:Double = node.impurity

      featureImpurityMap += (featureIndx -> featureImpurity)
    }

    if(!node.leftNode.isEmpty) {
      recursiveFeed(node.leftNode.get, featureImpurityMap)
    }

    if(!node.rightNode.isEmpty) {
      recursiveFeed(node.rightNode.get, featureImpurityMap)
    }
  }

}


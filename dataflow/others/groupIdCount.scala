vetexes.map{ 
  node => 
    node._2 -> node
}
.groupByKey /// (key, List[Node])
.flatMap{
  /// ng : (key, List[Node])
  ng => 
  /// ng._2 : List[Node]
    ng._2.map{
      x => /// x : Node
      (x._1,x._2,ng._2.size)
    }
}


val rdd = sc.textFile("hdfs://10.87.216.166:8020/user/feed_weibo/haibo11/like_weibo/haibo_like_weibo/dt=20170904/000001_0.gz")
val originIdx = Seq(16,17,18,19,20,21,22,23,24,29,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47)
rdd.map{
  line =>
    val splits = line.split('\t')
    val rst = originIdx.map(i => splits(i))
    rst.mkString("\t")
}
case class DCC(
  var havedefault : Boolean = true,
  var defaultvalue: String = "0"
  )
val dataConf = new DCC
def check(colValue : String) : String = if (
    colValue.isEmpty ||
      colValue.equals("") ||
      colValue.equalsIgnoreCase("""\\N""") ||
      colValue.equalsIgnoreCase("""\N""") ||
      colValue.equalsIgnoreCase("""N""") ||
      colValue.equalsIgnoreCase("NULL")) {
    // Assign default value here.
    if(dataConf.havedefault) {
      dataConf.defaultvalue
    } else {
      "WEIBO_DIRTY_DATA"
    }
  } else {
    colValue
  }

def newCK(colValue: String) : String = try {
  colValue.toDouble
}




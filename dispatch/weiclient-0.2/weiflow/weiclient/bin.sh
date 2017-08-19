#!/usr/bin/env bash

function show_usage {
    echo "usage: -j <jar> -x <xml> -n <nodeID>"
}

#TODO(facai), getopts没有做错误检查
while getopts "h?j:x:n:" arg
do
  case ${arg} in
    h) show_usage
       exit 0;;
    j) jar=${OPTARG};;
    x) xml=${OPTARG};;
    n) nodeID=${OPTARG};;
    \?) show_usage
  esac
done

#scala -cp data-flow-1.0-SNAPSHOT.jar com.weibo.datasys.common.Main dataflow.xml 1
echo "jar: $jar"
echo "xml: $xml"
echo "nodeID: ${nodeID}"

# Notice: 2nd $jar is the argument required.
scala -cp $jar com.weibo.datasys.common.Main $jar $xml ${nodeID}

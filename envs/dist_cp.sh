#!/bin/bash


dest_hdfs=hdfs://10.85.125.175:9000


from_hdfs=$1
to_hdfs=$dest_hdfs$from_hdfs



echo ===========================================
cmd="hadoop distcp -m 200 $from_hdfs $to_hdfs"
dateBeforeStart=`date +%F_%H-%M-%S`
echo $cmd
$cmd
dataAfterStart=`date +%F_%H-%M-%S`

dataAfterEnd=`date +%F_%H-%M-%S`
echo ===========================================
echo dateBeforeStart : $dateBeforeStart
echo dataAfterStart : $dataAfterStart
echo dataAfterEnd : $dataAfterEnd


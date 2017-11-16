def readText(filePath = ""):
  import pydoop.hdfs as hdfs
  import os
  file_is_file = hdfs.path.isfile(filePath)
  file_is_dir = hdfs.path.isdir(filePath)
  file_exist = hdfs.path.exists(filePath)
  try:
    if(file_is_file):
      files = hdfs.open(filePath)
    elif(file_is_dir):
      files = []
      for pieceFile in hdfs.ls(filePath):
        files += hdfs.open(pieceFile)
    elif(not file_exist):
      if(os.path.exists(filePath)):
        print "[WARN] file not found on hdfs read local file."
        files = open(filePath)
  except Exception as e:
    raise e
  finally:
    print type(files)
  return files



/home/suanec/ksp/tfos/ecosystem/README.md
/user/feed_weibo/warehouse/feed_sample_json_final/cleanedData/clean11437


/user/push_weibo/temp_cuiwei_push_log_singlegroup_distinct_dt
hdfs://ns1nn2.hadoop.data.sina.com.cn:8020/user/weibo_bigdata_dm/warehouse/temp_cuiwei_push_log_singlegroup_distinct_dt
hdfs://10.87.49.220:8020/user/push_weibo/test_dir


nohup hadoop distcp -m 100 hdfs://ns1nn2.hadoop.data.sina.com.cn:8020/user/weibo_bigdata_dm/warehouse/temp_cuiwei_push_log_singlegroup_distinct_dt hdfs://10.87.49.220:8020/user/push_weibo/temp_cuiwei_push_log_singlegroup_distinct_dt &

hadoop jar hadoop-yarn-applications-distributedshell-2.7.3.jar org.apache.hadoop.yarn.applications.distributedshell.Client -jar hadoop-yarn-applications-distributedshell-2.7.3.jar -shell_command ls
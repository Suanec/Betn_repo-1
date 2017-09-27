cp -r /data0/spark_weibo_bigdata_pa/libs/yarn-setting/hadoop-2.7.3  /data0/spark_weibo_bigdata_pa/libs/yarn-setting/spark-2.0.2-bin-hadoop2.7 /data0/spark_weibo_bigdata_pa/libs/yarn-setting/jdk1.8.0_131 /data0/spark_weibo_bigdata_pa/libs/yarn-setting/scala-2.11.8 /data0/rsync_data/control_center/ccConfs/yarn-setting

useradd -d /usr/home/d1_weibo_bigdata_pa -m d1_weibo_bigdata_pa 
useradd -d /usr/home/d1_weibo_bigdata_ba -m d1_weibo_bigdata_ba 
useradd -d /usr/home/d1_weibo_bigdata_push -m d1_weibo_bigdata_push 
useradd -d /usr/home/d1_weibo_bigdata_sys -m d1_weibo_bigdata_sys 
useradd -d /usr/home/d1_weibo_bigdata_vf -m d1_weibo_bigdata_vf 
useradd -d /usr/home/d1_weibo_bigdata_hotmblog -m d1_weibo_bigdata_hotmblog 
useradd -d /usr/home/d1_weibo_bigdata_spam -m d1_weibo_bigdata_spam 

# sudo -s
# useradd -d /usr/home/weibo_bigdata_ds -m weibo_bigdata_ds
# echo 'd123w123' | passwd --stdin weibo_bigdata_ds
# su weibo_bigdata_ds
# hadoop fs -ls /
# hadoop fs -ls / | wc -l
# exit
# exit
# exit

echo '123qwe' | passwd --stdin d1_weibo_bigdata_pa
echo '123qwe' | passwd --stdin d1_weibo_bigdata_ba
echo '123qwe' | passwd --stdin d1_weibo_bigdata_push
echo '123qwe' | passwd --stdin d1_weibo_bigdata_sys
echo '123qwe' | passwd --stdin d1_weibo_bigdata_vf
echo '123qwe' | passwd --stdin d1_weibo_bigdata_hotmblog
echo '123qwe' | passwd --stdin d1_weibo_bigdata_spam

echo 'export ccConfHome=/data0/rsync_data/control_center/ccConfs' >> /usr/home/d1_weibo_bigdata_pa/.bashrc
echo 'export JAVA_HOME=$ccConfHome/yarn-setting/jdk1.8.0_131' >> /usr/home/d1_weibo_bigdata_pa/.bashrc
echo 'export HADOOP_HOME=$ccConfHome/yarn-setting/hadoop-2.7.3' >> /usr/home/d1_weibo_bigdata_pa/.bashrc
echo 'export SPARK_HOME=$ccConfHome/yarn-setting/spark-2.0.2-bin-hadoop2.7' >> /usr/home/d1_weibo_bigdata_pa/.bashrc
echo 'export SCALA_HOME=$ccConfHome/yarn-setting/scala-2.11.8' >> /usr/home/d1_weibo_bigdata_pa/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$SPARK_HOME/bin:$SCALA_HOME/bin:$PATH' >> /usr/home/d1_weibo_bigdata_pa/.bashrc
echo 'export HADOOP_CONF_DIR=/data0/rsync_data/control_center/ccConfs/yarn-setting/EMR-118-conf' >> /usr/home/d1_weibo_bigdata_pa/.bashrc
echo 'export HADOOP_USER_NAME=feed_weibo' >> /usr/home/d1_weibo_bigdata_pa/.bashrc

echo 'export ccConfHome=/data0/rsync_data/control_center/ccConfs' >> /usr/home/d1_weibo_bigdata_ba/.bashrc
echo 'export JAVA_HOME=$ccConfHome/yarn-setting/jdk1.8.0_131' >> /usr/home/d1_weibo_bigdata_ba/.bashrc
echo 'export HADOOP_HOME=$ccConfHome/yarn-setting/hadoop-2.7.3' >> /usr/home/d1_weibo_bigdata_ba/.bashrc
echo 'export SPARK_HOME=$ccConfHome/yarn-setting/spark-2.0.2-bin-hadoop2.7' >> /usr/home/d1_weibo_bigdata_ba/.bashrc
echo 'export SCALA_HOME=$ccConfHome/yarn-setting/scala-2.11.8' >> /usr/home/d1_weibo_bigdata_ba/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$SPARK_HOME/bin:$SCALA_HOME/bin:$PATH' >> /usr/home/d1_weibo_bigdata_ba/.bashrc
echo 'export HADOOP_CONF_DIR=/data0/rsync_data/control_center/ccConfs/yarn-setting/EMR-118-conf' >> /usr/home/d1_weibo_bigdata_ba/.bashrc
echo 'export HADOOP_USER_NAME=algorithm_weibo' >> /usr/home/d1_weibo_bigdata_ba/.bashrc

echo 'export ccConfHome=/data0/rsync_data/control_center/ccConfs' >> /usr/home/d1_weibo_bigdata_push/.bashrc
echo 'export JAVA_HOME=$ccConfHome/yarn-setting/jdk1.8.0_131' >> /usr/home/d1_weibo_bigdata_push/.bashrc
echo 'export HADOOP_HOME=$ccConfHome/yarn-setting/hadoop-2.7.3' >> /usr/home/d1_weibo_bigdata_push/.bashrc
echo 'export SPARK_HOME=$ccConfHome/yarn-setting/spark-2.0.2-bin-hadoop2.7' >> /usr/home/d1_weibo_bigdata_push/.bashrc
echo 'export SCALA_HOME=$ccConfHome/yarn-setting/scala-2.11.8' >> /usr/home/d1_weibo_bigdata_push/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$SPARK_HOME/bin:$SCALA_HOME/bin:$PATH' >> /usr/home/d1_weibo_bigdata_push/.bashrc
echo 'export HADOOP_CONF_DIR=/data0/rsync_data/control_center/ccConfs/yarn-setting/EMR-118-conf' >> /usr/home/d1_weibo_bigdata_push/.bashrc
echo 'export HADOOP_USER_NAME=push_weibo' >> /usr/home/d1_weibo_bigdata_push/.bashrc

echo 'export ccConfHome=/data0/rsync_data/control_center/ccConfs' >> /usr/home/d1_weibo_bigdata_sys/.bashrc
echo 'export JAVA_HOME=$ccConfHome/yarn-setting/jdk1.8.0_131' >> /usr/home/d1_weibo_bigdata_sys/.bashrc
echo 'export HADOOP_HOME=$ccConfHome/yarn-setting/hadoop-2.7.3' >> /usr/home/d1_weibo_bigdata_sys/.bashrc
echo 'export SPARK_HOME=$ccConfHome/yarn-setting/spark-2.0.2-bin-hadoop2.7' >> /usr/home/d1_weibo_bigdata_sys/.bashrc
echo 'export SCALA_HOME=$ccConfHome/yarn-setting/scala-2.11.8' >> /usr/home/d1_weibo_bigdata_sys/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$SPARK_HOME/bin:$SCALA_HOME/bin:$PATH' >> /usr/home/d1_weibo_bigdata_sys/.bashrc
echo 'export HADOOP_CONF_DIR=/data0/rsync_data/control_center/ccConfs/yarn-setting/EMR-118-conf' >> /usr/home/d1_weibo_bigdata_sys/.bashrc
echo 'export HADOOP_USER_NAME=dcps_weibo' >> /usr/home/d1_weibo_bigdata_sys/.bashrc

echo 'export ccConfHome=/data0/rsync_data/control_center/ccConfs' >> /usr/home/d1_weibo_bigdata_vf/.bashrc
echo 'export JAVA_HOME=$ccConfHome/yarn-setting/jdk1.8.0_131' >> /usr/home/d1_weibo_bigdata_vf/.bashrc
echo 'export HADOOP_HOME=$ccConfHome/yarn-setting/hadoop-2.7.3' >> /usr/home/d1_weibo_bigdata_vf/.bashrc
echo 'export SPARK_HOME=$ccConfHome/yarn-setting/spark-2.0.2-bin-hadoop2.7' >> /usr/home/d1_weibo_bigdata_vf/.bashrc
echo 'export SCALA_HOME=$ccConfHome/yarn-setting/scala-2.11.8' >> /usr/home/d1_weibo_bigdata_vf/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$SPARK_HOME/bin:$SCALA_HOME/bin:$PATH' >> /usr/home/d1_weibo_bigdata_vf/.bashrc
echo 'export HADOOP_CONF_DIR=/data0/rsync_data/control_center/ccConfs/yarn-setting/EMR-118-conf' >> /usr/home/d1_weibo_bigdata_vf/.bashrc

echo 'export ccConfHome=/data0/rsync_data/control_center/ccConfs' >> /usr/home/d1_weibo_bigdata_hotmblog/.bashrc
echo 'export JAVA_HOME=$ccConfHome/yarn-setting/jdk1.8.0_131' >> /usr/home/d1_weibo_bigdata_hotmblog/.bashrc
echo 'export HADOOP_HOME=$ccConfHome/yarn-setting/hadoop-2.7.3' >> /usr/home/d1_weibo_bigdata_hotmblog/.bashrc
echo 'export SPARK_HOME=$ccConfHome/yarn-setting/spark-2.0.2-bin-hadoop2.7' >> /usr/home/d1_weibo_bigdata_hotmblog/.bashrc
echo 'export SCALA_HOME=$ccConfHome/yarn-setting/scala-2.11.8' >> /usr/home/d1_weibo_bigdata_hotmblog/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$SPARK_HOME/bin:$SCALA_HOME/bin:$PATH' >> /usr/home/d1_weibo_bigdata_hotmblog/.bashrc
echo 'export HADOOP_CONF_DIR=/data0/rsync_data/control_center/ccConfs/yarn-setting/EMR-118-conf' >> /usr/home/d1_weibo_bigdata_hotmblog/.bashrc
echo 'export HADOOP_USER_NAME=hot_weibo' >> /usr/home/d1_weibo_bigdata_hotmblog/.bashrc

echo 'export ccConfHome=/data0/rsync_data/control_center/ccConfs' >> /usr/home/d1_weibo_bigdata_spam/.bashrc
echo 'export JAVA_HOME=$ccConfHome/yarn-setting/jdk1.8.0_131' >> /usr/home/d1_weibo_bigdata_spam/.bashrc
echo 'export HADOOP_HOME=$ccConfHome/yarn-setting/hadoop-2.7.3' >> /usr/home/d1_weibo_bigdata_spam/.bashrc
echo 'export SPARK_HOME=$ccConfHome/yarn-setting/spark-2.0.2-bin-hadoop2.7' >> /usr/home/d1_weibo_bigdata_spam/.bashrc
echo 'export SCALA_HOME=$ccConfHome/yarn-setting/scala-2.11.8' >> /usr/home/d1_weibo_bigdata_spam/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$SPARK_HOME/bin:$SCALA_HOME/bin:$PATH' >> /usr/home/d1_weibo_bigdata_spam/.bashrc
echo 'export HADOOP_CONF_DIR=/data0/rsync_data/control_center/ccConfs/yarn-setting/EMR-118-conf' >> /usr/home/d1_weibo_bigdata_spam/.bashrc

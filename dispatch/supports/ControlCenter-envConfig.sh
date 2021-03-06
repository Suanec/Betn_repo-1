useradd -d /usr/home/spark_weibo_bigdata_ba -m spark_weibo_bigdata_ba -p spark_weibo_bigdata_ba
echo '123qwe' | passwd --stdin spark_weibo_bigdata_ba
useradd -d /usr/home/weibo_bigdata_ds -m weibo_bigdata_ds -p weibo_bigdata_ds
echo '123qwe' | passwd --stdin weibo_bigdata_ds


sudo -s
useradd -d /usr/home/feed_weibo -m feed_weibo -p feed_weibo
echo '123qwe' | passwd --stdin feed_weibo
cd /usr/home/feed_weibo/
rz -bye


tar xvf EMR-131-conf.tar
echo "" >> /etc/hosts
cat EMR-131-conf/hosts >> /etc/hosts
cp /usr/home/feed_weibo/EMR-131-conf/jersey-bundle-1.17.1.jar /data0/spark_weibo_bigdata_pa/libs/yarn-setting/spark-2.0.2-bin-hadoop2.7/jars
su - feed_weibo -s /bin/bash
vim ~/.bashrc



export JAVA_HOME=/data0/spark_weibo_bigdata_pa/libs/yarn-setting/jdk1.8.0_131
export HADOOP_HOME=/data0/spark_weibo_bigdata_pa/libs/yarn-setting/hadoop-2.7.3
export SPARK_HOME=/data0/spark_weibo_bigdata_pa/libs/yarn-setting/spark-2.0.2-bin-hadoop2.7
export HADOOP_CONF_DIR=/data0/spark_weibo_bigdata_pa/libs/yarn-setting/etc/hadoop
export PATH=/data0/spark_weibo_bigdata_pa/libs/yarn-setting/jdk1.8.0_131/bin:/data0/spark_weibo_bigdata_pa/libs/yarn-setting/hadoop-2.7.3/bin:/data0/spark_weibo_bigdata_pa/libs/yarn-setting/spark-2.0.2-bin-hadoop2.7/bin:/usr/local/jdk1.7.0_67/bin:/usr/local/jdk1.7.0_67/jre/bin:/usr/local/hadoop-2.4.0/bin:/usr/local/hive-0.13.0/bin:/usr/lib64/qt-3.3/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/usr/home/spark_weibo_bigdata_pa/.local/bin:/usr/home/spark_weibo_bigdata_pa/bin
export SCALA_HOME=/data0/spark_weibo_bigdata_pa/libs/yarn-setting/scala-2.11.8
export PATH=$SCALA_HOME/bin:$PATH

export hdc2=/usr/home/feed_weibo/EMR-131-conf/etc/hadoop
export HADOOP_CONF_DIR=$hdc2



source ~/.bashrc
hadoop fs -ls 


spark-shell --master yarn \
--jars /data0/spark_weibo_bigdata_pa/libs/yarn-setting/spark-2.0.2-bin-hadoop2.7/jars/jersey-bundle-1.17.1.jar


spark-shell --master yarn



sudo -s 
mkdir -p /data0/weibo_bigdata_pa/control_center
cd /data0/weibo_bigdata_pa/control_center
rsync -vzrtopg --progress 10.77.29.68::backup/data/odps-for-control-center.tar .
tar xvf odps-for-control-center.tar
chown -R weibo_bigdata_pa:weibo_bigdata_pa /data0/weibo_bigdata_pa
vim /usr/home/weibo_bigdata_pa/.bashrc
GGo
export ODPS_HOME=/data0/weibo_bigdata_pa/control_center/odps-for-control-center
export PATH=$ODPS_HOME/bin:$PATH


su - weibo_bigdata_pa -s /bin/bash
odpscmd
quit;
exit
exit
exit



# ============================sigleEnvConfig============================
d1_weibo_bigdata_pa 
d1_weibo_bigdata_ba 
d1_weibo_bigdata_push 
d1_weibo_bigdata_sys 
d1_weibo_bigdata_vf 
d1_weibo_bigdata_hotmblog 
d1_weibo_bigdata_spam 


vim /usr/home/mc_weibo_bigdata_pa/.bashrc
:12,20d
:wq

vim /usr/home/mc_weibo_bigdata_ba/.bashrc
:12,20d
:wq

vim /usr/home/mc_weibo_bigdata_push/.bashrc
:12,20d
:wq

vim /usr/home/mc_weibo_bigdata_sys/.bashrc
:12,20d
:wq

vim /usr/home/mc_weibo_bigdata_vf/.bashrc
:12,20d
:wq

vim /usr/home/mc_weibo_bigdata_hotmblog/.bashrc
:12,20d
:wq

vim /usr/home/mc_weibo_bigdata_spam/.bashrc
:12,20d
:wq

# ============================sigleEnvConfig============================

useradd -d /usr/home/d1_weibo_bigdata_pa -m d1_weibo_bigdata_pa 
useradd -d /usr/home/d1_weibo_bigdata_ba -m d1_weibo_bigdata_ba 
useradd -d /usr/home/d1_weibo_bigdata_push -m d1_weibo_bigdata_push 
useradd -d /usr/home/d1_weibo_bigdata_sys -m d1_weibo_bigdata_sys 
useradd -d /usr/home/d1_weibo_bigdata_vf -m d1_weibo_bigdata_vf 
useradd -d /usr/home/d1_weibo_bigdata_hotmblog -m d1_weibo_bigdata_hotmblog 
useradd -d /usr/home/d1_weibo_bigdata_spam -m d1_weibo_bigdata_spam 

echo '123qwe' | passwd --stdin d1_weibo_bigdata_pa
echo '123qwe' | passwd --stdin d1_weibo_bigdata_ba
echo '123qwe' | passwd --stdin d1_weibo_bigdata_push
echo '123qwe' | passwd --stdin d1_weibo_bigdata_sys
echo '123qwe' | passwd --stdin d1_weibo_bigdata_vf
echo '123qwe' | passwd --stdin d1_weibo_bigdata_hotmblog
echo '123qwe' | passwd --stdin d1_weibo_bigdata_spam

useradd -d /usr/home/mc_weibo_bigdata_pa -m mc_weibo_bigdata_pa -p mc_weibo_bigdata_pa
useradd -d /usr/home/mc_weibo_bigdata_ba -m mc_weibo_bigdata_ba -p mc_weibo_bigdata_ba
useradd -d /usr/home/mc_weibo_bigdata_push -m mc_weibo_bigdata_push -p mc_weibo_bigdata_push
useradd -d /usr/home/mc_weibo_bigdata_sys -m mc_weibo_bigdata_sys -p mc_weibo_bigdata_sys
useradd -d /usr/home/mc_weibo_bigdata_vf -m mc_weibo_bigdata_vf -p mc_weibo_bigdata_vf
useradd -d /usr/home/mc_weibo_bigdata_hotmblog -m mc_weibo_bigdata_hotmblog -p mc_weibo_bigdata_hotmblog
useradd -d /usr/home/mc_weibo_bigdata_spam -m mc_weibo_bigdata_spam -p mc_weibo_bigdata_spam

echo '123qwe' | passwd --stdin mc_weibo_bigdata_pa
echo '123qwe' | passwd --stdin mc_weibo_bigdata_ba
echo '123qwe' | passwd --stdin mc_weibo_bigdata_push
echo '123qwe' | passwd --stdin mc_weibo_bigdata_sys
echo '123qwe' | passwd --stdin mc_weibo_bigdata_vf
echo '123qwe' | passwd --stdin mc_weibo_bigdata_hotmblog
echo '123qwe' | passwd --stdin mc_weibo_bigdata_spam

mkdir -p /data0/rsync_data/control_center/ccConfs/yarn-setting
cd /data0/rsync_data/control_center/ccConfs/yarn-setting
cp -r /data0/spark_weibo_bigdata_pa/libs/yarn-setting/hadoop-2.7.3  /data0/spark_weibo_bigdata_pa/libs/yarn-setting/spark-2.0.2-bin-hadoop2.7 /data0/spark_weibo_bigdata_pa/libs/yarn-setting/jdk1.8.0_131 /data0/spark_weibo_bigdata_pa/libs/yarn-setting/scala-2.11.8 /data0/rsync_data/control_center/ccConfs/yarn-setting

rsync -vzrtopg --progress 10.77.29.68::backup/data/ccConf.tar .
tar xvf ccConf.tar

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
echo 'export HADOOP_USER_NAME=dspc_weibo' >> /usr/home/d1_weibo_bigdata_sys/.bashrc

echo 'export ccConfHome=/data0/rsync_data/control_center/ccConfs' >> /usr/home/d1_weibo_bigdata_vf/.bashrc
echo 'export JAVA_HOME=$ccConfHome/yarn-setting/jdk1.8.0_131' >> /usr/home/d1_weibo_bigdata_vf/.bashrc
echo 'export HADOOP_HOME=$ccConfHome/yarn-setting/hadoop-2.7.3' >> /usr/home/d1_weibo_bigdata_vf/.bashrc
echo 'export SPARK_HOME=$ccConfHome/yarn-setting/spark-2.0.2-bin-hadoop2.7' >> /usr/home/d1_weibo_bigdata_vf/.bashrc
echo 'export SCALA_HOME=$ccConfHome/yarn-setting/scala-2.11.8' >> /usr/home/d1_weibo_bigdata_vf/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$SPARK_HOME/bin:$SCALA_HOME/bin:$PATH' >> /usr/home/d1_weibo_bigdata_vf/.bashrc
echo 'export HADOOP_CONF_DIR=/data0/rsync_data/control_center/ccConfs/yarn-setting/EMR-118-conf' >> /usr/home/d1_weibo_bigdata_vf/.bashrc
echo 'export HADOOP_USER_NAME=dspc_weibo' >> /usr/home/d1_weibo_bigdata_sys/.bashrc

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

cat /data0/rsync_data/control_center/ccConfs/yarn-setting/EMR-118-conf/hst >> /etc/hosts

mv /data0/weibo_bigdata_pa/control_center/odps-for-control-center /data0/rsync_data/control_center/ccConfs/
#echo 'export ODPS_HOME=/$ccConfHome/odps-for-control-center'
#echo 'export PATH=$ODPS_HOME/bin:$PATH'

exit
exit
exit


wc -l  /usr/home/d1_weibo_bigdata_pa/.bashrc
wc -l  /usr/home/d1_weibo_bigdata_ba/.bashrc
wc -l  /usr/home/d1_weibo_bigdata_push/.bashrc
wc -l  /usr/home/d1_weibo_bigdata_sys/.bashrc
wc -l  /usr/home/d1_weibo_bigdata_vf/.bashrc
wc -l  /usr/home/d1_weibo_bigdata_hotmblog/.bashrc
wc -l  /usr/home/d1_weibo_bigdata_spam/.bashrc





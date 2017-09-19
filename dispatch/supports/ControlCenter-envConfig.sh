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






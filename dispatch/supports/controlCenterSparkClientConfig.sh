rsync -vzrt --progress 10.77.29.68::backup/spark/yarn-setting.tar .
rsync -vzrt --progress 10.77.29.68::backup/spark/scala-2.11.8.tgz .
tar xvf scala-2.11.8.tgz
echo "export SCALA_HOME=/data0/spark_weibo_bigdata_pa/yarn-setting/scala-2.11.8" >> ~/.bashrc
echo "export PATH=\$SCALA_HOME/bin:\$PATH" >> ~/.bashrc
echo ""
su - spark_weibo_bigdata_pa -s /bin/bash
hadoop fs -ls /user
cat ""
rsync -vzrt --progress scala-2.11.8.tgz 10.77.29.68::backup/spark/
10.77.29.69,10.77.29.70,10.77.29.71,10.77.29.72,10.77.29.73,10.77.29.74,10.77.29.75


10.77.29.69
10.77.29.70
10.77.29.71
10.77.29.72
10.77.29.73
10.77.29.74
10.77.29.75

sudo su -
su - spark_weibo_bigdata_pa -s /bin/bash
cd /data0/spark_weibo_bigdata_pa/libs/yarn-setting/
rsync -vzrt --progress 10.77.29.68::backup/spark/scala-2.11.8.tgz .
tar xvf scala-2.11.8.tgz
echo "export SCALA_HOME=/data0/spark_weibo_bigdata_pa/libs/yarn-setting/scala-2.11.8" >> ~/.bashrc
echo "export PATH=\$SCALA_HOME/bin:\$PATH" >> ~/.bashrc
source ~/.bashrc
scala

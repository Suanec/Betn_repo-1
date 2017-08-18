if [ $1 = ""];then
  MASTER=local
else
  MASTER=$1
fi
spark-shell \
  --driver-memory 20g \
  --jars dataflow-Tron.jar \
  --master $MASTER \
  --num-executors 7 \
  #--executor-cores 10 \
  #--executor-memory 20g \
#  --files meta,data.conf,feature.conf,pipeline.xml,dataflow.jar \
#  --deploy-mode client \


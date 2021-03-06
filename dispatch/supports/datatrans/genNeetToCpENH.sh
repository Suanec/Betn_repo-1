TARGET_DIR="hdfs://istinct_dt"
SOURCE_DIR="hdfs://_dt"
ROOT_DIR="warehouse"
DISTCP_CMD="hadoop distcp -m 100 -bandwidth 100 -update "
IS_DROPPED=1
FATHER_DIR=$(echo ${SOURCE_DIR} | awk -F"/" '{print $NF}')
if [ ${IS_DROPPED} == 1 ]; then
  hadoop fs -du -h ${TARGET_DIR} \
  | grep "0        hdfs:" \
  | awk -F${FATHER_DIR} -v SOURCE_DIR=${SOURCE_DIR} '{print SOURCE_DIR$2}' \
  | awk -F${ROOT_DIR} -v TARGET_DIR=${TARGET_DIR} -v SOURCE_DIR=${SOURCE_DIR} '{print SOURCE_DIR$2 " "TARGET_DIR$2}' \
  | awk -F" " '{print "'"hadoop distcp -m 100 -bandwidth 100 -update "'"$1" "$2}' \
  > needToCp.sh
else
echo false
fi


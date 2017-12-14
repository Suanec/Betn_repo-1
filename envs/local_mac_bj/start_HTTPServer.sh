TARGET_FILE_NAME=$1
#ifconfig | grep inet | grep netmask
#LOCAL_IP=ifconfig | awk '/inet / {print $2}'
LOCAL_IP=`ifconfig | awk '/inet / {print $2}' | grep -v "127.0.0.1"`
#read -r -p "input Local IP : " LOCAL_IP
echo "wget -c -t 10 ${LOCAL_IP}:12306/${TARGET_FILE_NAME}"
python -m SimpleHTTPServer 12306

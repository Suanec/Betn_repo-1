LOCAL_IP=`ifconfig | awk '/inet / {print $2}' | grep -v "127.0.0.1"`
echo $LOCAL_IP

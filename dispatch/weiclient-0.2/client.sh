#!/bin/sh

if [ $# -lt 4 ];then
    echo "usage src_dir userName job_name clusterVersion"
    exit 1
fi

src_dir=$1
userName=$2
job_name=$3
clusterVersion=$4

if [ ! -d $src_dir ];then
    echo "just dir allowed!"
    exit 1
fi

# cut /dir1/last//// to /dir1/last
while [[ "${src_dir##*/}"x = ""x ]]
do
   src_dir="${src_dir%/*}"
done

cmd="rsync -vzrtopg --progress $src_dir 10.77.29.68::backup/weiflow"
echo "rsync cmd: $cmd"
$cmd

if [ $? -ne 0 ];then
    echo "rsync error!"
    exit 1
fi

last_dir=${src_dir##*/}
url="http://10.77.29.68:8080/controlCenter-1.0.0/notify.do?fileMode=local&clusterType=spark&fileName=$last_dir&account=$userName&jobName=$job_name&version=$clusterVersion"
echo "url: $url"
curl $url

#!/usr/bin/env bash

function show_usage {
    echo "usage -x <src_dir> -n <user_name> -j <job_name> -v <cluster_version> -d <data_path> -t <cluster_type>"
    echo "OR usage -f <conf_file> "
}
function load_config() {
	while read line;do  
	    eval "$line"  
    done < $conf_file
}


while getopts "h?d:f:j:n:t:v:x:" arg
#    if [ $arg = "" ]; then
#       show_usage
#       exit 0
#    fi
do
	case ${arg} in
      h) show_usage
          exit 0;;
      d) data_path=${OPTARG};;
      f) conf_file=${OPTARG}
          load_config;;
      j) job_name=${OPTARG};;
      n) user_name=${OPTARG};;
      t) cluster_type=${OPTARG};;
      v) cluster_version=${OPTARG};;
      x) src_dir=${OPTARG};;
      \?) show_usage
          exit 0;;
    esac
done


if [ ! -d $src_dir ];then
	echo "just dir allowed!"
	exit 1
fi

# cut /dir1/last//// to /dir1/last
while [[ "${src_dir##*/}"x = ""x ]]
do
	src_dir="${src_dir%/*}"
done


time_stamp=$(date +%s)
execute_dir=${src_dir##*/}-${time_stamp}
last_dir=${execute_dir##*/}
echo "src_dir: ${src_dir}"
echo "user_name: ${user_name}"
echo "job_name: ${job_name}"
echo "cluster_version: ${cluster_version}"
echo "cluster_type: ${cluster_type}"
echo "execute_dir: ${execute_dir}"

if [ ! -n "$data_path" ] ;
  then
    echo "data_path is empty"
else
    echo "data_path: ${data_path}"
    echo $data
    data_cmd="rsync -vzrtopg --progress $data_path 10.77.29.68::backup/data/"
    echo "rsync data_cmd: $data_cmd"
    $data_cmd
fi

cmd="rsync -vqzrtopg --progress $src_dir/* 10.77.29.68::backup/weiflow/$last_dir"
echo "rsync cmd: $cmd"
$cmd

if [ $? -ne 0 ];then
	echo "rsync error!"
	exit 1
fi

url="http://10.77.29.68:8080/controlCenter-1.0.0/notify.do?fileMode=local&clusterType=$cluster_type&fileName=$last_dir&account=$user_name&jobName=$job_name&version=$cluster_version"

echo "url: $url"
curl $url


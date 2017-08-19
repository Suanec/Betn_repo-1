#!/usr/bin/env bash

function show_usage {
    echo "usage -x <src_dir> -n <user_name> -j <job_name> -v <cluster_version> -d <data_dir> -t <cluster_type>"
}

while getopts "h?x:n:j:v:d:t:" arg
do
	case ${arg} in
      h) show_usage
      	exit 0;;
      d) data_dir=${OPTARG};;
      j) job_name=${OPTARG};;
      n) user_name=${OPTARG};;
	  t) cluster_type=${OPTARG};;
      v) cluster_version=${OPTARG};;
      x) src_dir=${OPTARG};;
      \?) show_usage
      		exit 0;;
    esac
done

echo "src_dir: ${src_dir}"
echo "user_name: ${user_name}"
echo "job_name: ${job_name}"
echo "cluster_version: ${cluster_version}"
echo "cluster_type: ${cluster_type}"
echo "data_dir: ${data_dir}"


if [ ! -d $src_dir ];then
	echo "just dir allowed!"
	exit 1
fi

# cut /dir1/last//// to /dir1/last
while [[ "${src_dir##*/}"x = ""x ]]
do
	src_dir="${src_dir%/*}"
done

data_cmd="rsync -vzrtopg --progress $data_dir 10.77.29.68::backup/data/"
echo "rsync data_cmd: $data_cmd"
$data_cmd
cmd="rsync -vzrtopg --progress $src_dir 10.77.29.68::backup/weiflow"
echo "rsync cmd: $cmd"
$cmd

if [ $? -ne 0 ];then
	echo "rsync error!"
	exit 1
fi

last_dir=${src_dir##*/}
url="http://10.77.29.68:8080/controlCenter-1.0.0/notify.do?fileMode=local&clusterType=$cluster_type&fileName=$last_dir&account=$user_name&jobName=$job_name&version=$cluster_version"

echo "url: $url"
# curl $url


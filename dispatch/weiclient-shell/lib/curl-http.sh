#!/usr/bin/env bash
#'{"owner":"lihan3","name":"lihan_test","command":"cd /data0/users/jihui2/ctr; python t.py  --distributed False","user":"root","deleNotCrontJob":true,"host":"10.77.9.131"}'
function show_usage {
	echo "usage : -f <config_file>"
}

function load_config() {
	while read line;do
		eval "$line"
	done < $conf_file
}

while getopts "h?d:f:j:n:t:v:x:" arg
do
  case ${arg} in
    h) show_usage
        exit 0;;
#    d) data_path=${OPTARG};;
    f) conf_file=${OPTARG}
        load_config;;
#    j) job_name=${OPTARG};;
#    n) user_name=${OPTARG};;
#    t) cluster_type=${OPTARG};;
#    v) cluster_version=${OPTARG};;
#    x) src_dir=${OPTARG};;
    \?) show_usage
        exit 0;;
  esac
done


curl -G ${HTTPSERVER} --data-urlencode job="{\"owner\":\"${OWNER}\",\"name\":\"${NAME}\",\"command\":\"${COMMAND}\",\"user\":\"${USER}\",\"deleNotCrontJob\":${DELENOTCRONTJOB},\"host\":\"${HOST}\"}"

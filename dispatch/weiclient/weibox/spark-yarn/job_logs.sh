#!/bin/bash

SELF_DIR="$( cd "$( dirname "$0" )" && pwd )"
grep "URL:" weiflow-from-weiclient.log | uniq | awk -F": http:" '{print $2}' | awk -F"\/" '{print $5}' | xargs yarn logs -applicationId
 
rm1=$(grep "URL:" weiflow-from-weiclient.log | uniq | awk -F": http:" '{print $2}' | awk -F":" '{print "http://10.87.49.220:"$2}' ) #| xargs echo
rm2=$(grep "URL:" weiflow-from-weiclient.log | uniq | awk -F": http:" '{print $2}' | awk -F":" '{print "http://10.87.49.221:"$2}') # | xargs echo

req_status=$(curl -s ${rm1}) 
#echo $req_status
JOB_HEADER="JOB TRACK URL: "

if [[ ${req_status} = "" ]]
then
    echo ${JOB_HEADER}${rm2}
else
    echo ${JOB_HEADER}${rm1}
fi

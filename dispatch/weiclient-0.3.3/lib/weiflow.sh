#!/usr/bin/env bash

CUR_DIR="$( cd "$( dirname "$0" )" && pwd )"
chown -R weibo_bigdata_pa $CUR_DIR
#chown -R enzhao $CUR_DIR
su - weibo_bigdata_pa -s /bin/bash <<EOF
#whoami >> weiflow-from-weiclient.log 2>&1;
echo $PATH >> weiflow-from-weiclient.log 2>&1;
#su - enzhao -s /bin/bash <<EOF
cd $CUR_DIR;
sh _script_path -j _jar_path -x ./conf/weiflow_config.xml.template -n 1 >> weiflow-from-weiclient.log 2>&1;
exit;
EOF

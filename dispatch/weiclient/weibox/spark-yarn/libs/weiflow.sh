#!/usr/bin/env bash

CUR_DIR="$( cd "$( dirname "$0" )" && pwd )"
useradd _submit_account
chown -R _submit_account $CUR_DIR
su - _submit_account -s /bin/bash <<EOF
cd $CUR_DIR;
sh _script_path -j _jar_path -x dataflow-pipeline.xml -n 3 > weiflow-from-weiclient.log 2>&1;
exit;
EOF

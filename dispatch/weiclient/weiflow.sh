#!/usr/bin/env bash

#su - weibo_bigdata_pa -s /bin/bash && sh _script_path -j _jar_path -x weiflow-testShell.xml -n 2 > weiflow.log 2>&1
#!/usr/bin/env bash

CUR_DIR="$( cd "$( dirname "$0" )" && pwd )"
chown -R weibo_bigdata_pa $CUR_DIR
su - weibo_bigdata_pa -s /bin/bash <<EOF
cd $CUR_DIR;
sh _script_path -j _jar_path -x ./conf/weiflow_config.xml.template -n 1 >> weiflow-from-weiclient.log 2>&1;
exit;
EOF

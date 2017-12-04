#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

from ..tools import logger_helper

logger = logger_helper.wei_logger("sys_helper")
def sys_run(_cmd = ''):
    logger.info("command running... ")
    logger.debug("command running... %s" % _cmd)
    response_code = os.system(_cmd)
    if(response_code != 0):
        logger.error("run command %s found error!! with exit code %d!!" % (_cmd,response_code))
    else:
        logger.info("run command success!! with exit code %d!!" % response_code)
        logger.debug("run command %s success!! with exit code %d!!" % (_cmd, response_code))
    return response_code

def gen_spark_weiflow_docker( _dict = {} ):
    docker_run_str = "docker run " \
                     ""
def gen_spark_weiflow(_client_job_path ="./weibox/spark-yarn",
                      _jar_file ="_jar_path",
                      _config_file ="./conf/weiflow_config.xml.template",
                      _command = 1):
    weiflow_str = "#!/usr/bin/env bash\n\n" \
                  'CUR_DIR="$( cd "$( dirname "$0" )" && pwd )"\n' \
                  "useradd _submit_account\n" \
                  "chown -R _submit_account $CUR_DIR\n" \
                  "su - _submit_account -s /bin/bash <<EOF\n" \
                  "cd $CUR_DIR;\n" \
                  "sh _script_path -j %s -x %s -n %d > weiflow-from-weiclient.log 2>&1;\n" \
                  "exit;\n" \
                  "EOF\n" % (_jar_file, _config_file, _command)
    logger.debug("generate dataflow submit commands.")
    writer = open("%s/libs/weiflow.sh" % _client_job_path, "w+")
    try:
        writer.write(weiflow_str)
        logger.debug("gen spark submit command shell succeed!! ")
    except IOError,e:
        logger.debug("gen spark submit command shell failed!! ")
        logger.error(e.message)
    finally:
        writer.close()

def rsync_sandbox(cluster_type = "spark",
                  command = 1):
    return 0


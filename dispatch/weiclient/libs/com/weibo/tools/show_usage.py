#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
from com.weibo.tools.logger_helper import wei_logger

def global_usage():
    usage = "\n weicmd ${command} ${sub-command}." \
            "\n\n supported command :" \
            "\n submit ${sub-command}. " \
            "\n\t For help type in : submit -h." \
            "\n\t EXAMPLE: submit -f ${CONF_FILE} " \
            "\n rsync ${sub-command}. " \
            "\n\t For help type in : rsync ." \
            "EXAMPLE: rsync ${SRC_FILE} ${DEST_FILE}" \
            "\n query ${sub-command}. " \
            "\n\t For help type in : " \
            "\n\t query cluster OR query cluster -h." \
            "\n\t query job OR query job -h." \
            "EXAMPLE: query cluster all OR query job all" \
            "\n kill ${sub-command}. " \
            "\n\t For help type in : " \
            "\n\t kill ." \
            "\n\t EXAMPLE: kill ${JOB_NAME}"
    return usage
def show_usage():
    print 'usage : \n' \
          '-j --job_name <job_name> \n' \
          '-n --center_user_name <center_user_name> \n' \
          '-x --client_job_path <client_job_path> \n'
    print 'OR usage -f --conf_file <conf_file> (RECOMMENDED) '

def show_usage_query():
    print 'usage : \n' \
          '-c --cluster_name <cluster_name> \n' \
          '-n --user_name <user_name> \n' \
          '-t --query_type <query_type> \n' \
          '-x --src_dir <src_dir> \n'
    print 'OR usage -f --conf_file <conf_file> (RECOMMENDED) '


def show_usage_job_query():
    print 'usage : \n' \
          '-j --job_name <job_name> \n' \
          '-n --user_name <user_name> \n' \
          '-t --query_type <query_type> \n'
    print 'OR usage -f --conf_file <conf_file> (RECOMMENDED) '

def show_success_info():
    print "\t\t====================================================\n" \
          "\t\tINFO: JOB HAD SUBMITTED, PLEASE CHECK IT BY GOTO: \n" \
          "\t\t信息: 作业已提交，请到控制台查看： \n" \
          "\t\thttps://mlplat.intra.weibo.com/math/ctrlUserCenter\n" \
          "\t\t====================================================\n"

def kill_show_success_info():
    print "\t\t====================================================\n" \
          "\t\tINFO: JOB HAD KILLED, PLEASE CHECK IT BY GOTO: \n" \
          "\t\t信息: 作业已终止，请到控制台查看： \n" \
          "\t\thttps://mlplat.intra.weibo.com/math/ctrlUserCenter\n" \
          "\t\t====================================================\n"

def show_job_info(client_center_host_name = "",
                  client_job_path = "",
                  center_user_name = "",
                  job_name = "",
                  cluster_dispatch_type = "",
                  job_common_submit_type = "",
                  execute_dir = "",
                  last_dir = ""):
    print "====================================================\n" \
          "INFO: JOB HAD SUBMITING, JOB INFO: \n" \
          "client_center_host_name: %s\n" \
          "client_job_path : %s\n" \
          "center_user_name: %s\n" \
          "job_name: %s\n" \
          "cluster_dispatch_type: %s\n" \
          "job_common_submit_type: %s\n" \
          "execute_dir: %s\n" \
          "last_dir: %s\n" \
          "====================================================\n" % \
          (client_center_host_name,
           client_job_path,
           center_user_name,
           job_name,
           cluster_dispatch_type,
           job_common_submit_type,
           execute_dir,
           last_dir)

def request_info_check(http_response_code = "", logger = wei_logger()):
    if(len(http_response_code.strip()) == 0 ):
        show_success_info()
    elif(http_response_code.strip()[0] == "{"):
        http_response_code_json_map = json.loads(http_response_code)
        if(http_response_code_json_map.has_key("message")):
            if( http_response_code_json_map.get("message").find(u'success') >= 0 ):
                show_success_info()
            else:
                logger.error(http_response_code_json_map["message"])
        elif( http_response_code_json_map.has_key("errCode") ):
            if( http_response_code_json_map.get("errCode") == u''):
                show_success_info()
            else:
                logger.error(http_response_code_json_map["errMsg"])
        else:
            logger.error(http_response_code_json_map["errMsg"])
    else:
        logger.error(http_response_code)

def kill_request_info_check(http_response_code = "", logger = wei_logger()):
    if(len(http_response_code.strip()) == 0 ):
        kill_show_success_info()
    elif(http_response_code.strip()[0] == "{"):
        http_response_code_json_map = json.loads(http_response_code)
        if(http_response_code_json_map.has_key("message")):
            if( http_response_code_json_map.get("message").find(u'success') >= 0 ):
                kill_show_success_info()
            else:
                logger.error(http_response_code_json_map["message"])
        elif( http_response_code_json_map.has_key("errCode") ):
            if( http_response_code_json_map.get("errCode") == u''):
                kill_show_success_info()
            else:
                logger.error(http_response_code_json_map["errMsg"])
        else:
            logger.error(http_response_code_json_map["errMsg"])
    else:
        logger.error(http_response_code)


#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import sys
import urllib2

from com.weibo.tools.url_helper import gen_host
from com.weibo.tools import logger_helper
from com.weibo.tools.init_get_opts import query_job_get_opts
from com.weibo.tools.http_helper import post, get

logger = logger_helper.wei_logger("query_job_info")

def useful_info(_key = ""):
    return (_key.find("version") >= 0
            or _key.find("jobName") >= 0
            or _key.find("uiUrl") >= 0
            or _key.find("jobType") >= 0)

def format_job_info(_job_info = ""):
    result = json.loads(_job_info).get("result")
    show_info = ""
    for job_elem in result:
        for key in filter(
                lambda _key: (_key.find("jobName") >= 0
                              or _key.find("status") >= 0
                              or _key.find("jobUrl") >= 0
                              or _key.find("submitTime") >= 0
                              or _key.find("clusterType") >= 0),
                job_elem):
            show_info += "%s : %s\n\t" % (key, job_elem[key])
        if(len(show_info) == 0):
            show_info = result
        logger.info(show_info)
    return show_info

def get_all_job(_job_name = "", _param = {}):
    if(len(_param) == 0):
        host_name = "http://controlcenter.ds.sina.com.cn/controlCenter-1.0.0"
    else:
        host_name = gen_host(_param)
    url = '%s/query.do?op=query&query_type=job&job_name=%s' % (host_name,_job_name)
    job_info = get(url)
    show_info = format_job_info(job_info)
    print "JOB INFO LIST FOLLOW : "
    if(type(show_info) == str):
        for show_info_line in show_info:
            print show_info_line
    else:
        print show_info
# get_all_job("EMR")

def get_job_info_by_jobname(_jobname, _param = {}):
    if(len(_param) == 0):
        host_name = "http://controlcenter.ds.sina.com.cn/controlCenter-1.0.0"
    else:
        host_name = gen_host(_param)
    url = "%s/query.do?op=query&query_type=job&job_name=" % host_name + _jobname
    job_info = get(url)
    show_info = format_job_info(job_info)
    print "JOB INFO LIST FOLLOW : "
    for show_info_line in show_info:
        print show_info_line
# get_job_info_by_jobname("baozhan")

def get_job_info_by_jobname_special_k8s(_jobname, _param = {}):
    if(len(_param) == 0):
        host_name = "http://controlcenter.ds.sina.com.cn/controlCenter-1.0.0"
    else:
        host_name = gen_host(_param)

    if(_param.has_key("job_common_submit_type")):
        job_common_submit_type = _param["job_common_submit_type"]
    if(_param.has_key("job_common_is_distributed")):
        job_common_is_distributed = _param["job_common_is_distributed"]
    if(_param.has_key("cluster_dispatch_type")):
        cluster_dispatch_type= _param["cluster_dispatch_type"]
    if(_param.has_key("job_query_command")):
        # job_query_command = "sh%20" + _param["job_query_command"] + """%20""" + """po"""
        job_query_command = "sh %s po" % _param["job_query_command"]
    if(_param.has_key("job_common_is_docker")):
        job_common_is_docker = _param.get("job_common_is_docker")
    if(job_common_submit_type == "tensorflow" and
               job_common_is_distributed == "1" and
               cluster_dispatch_type == "k8s"):
        query_status_param = {}
        query_status_param["job_name"] = _jobname
        query_status_param["command"] = job_query_command
        query_status_param["job_common_is_docker"] = job_common_is_docker
        # url = "%s/queryJobStatus.do?command=%s&jobName=%s" % (host_name, job_query_command, _jobname)
        host_url = gen_host(_param) + "/queryJobStatus.do"
        job_info = post(host_url, query_status_param)
    elif(job_common_submit_type == "spark" and
               job_common_is_distributed == "1" and
               cluster_dispatch_type == "yarn"):
        query_status_param = {}
        query_status_param["job_name"] = _jobname
        query_status_param["command"] = "sh " + _param["job_query_command"]
        query_status_param["job_common_is_docker"] = job_common_is_docker
        # url = "%s/queryJobStatus.do?command=%s&jobName=%s" % (host_name, job_query_command, _jobname)
        host_url = gen_host(_param) + "/queryJobStatus.do"
        job_info = post(host_url, query_status_param)
        result_info = json.loads(job_info).get("result")
        if(len(result_info) <= 0):
            logger.error("no result info received. PLEASE CHECK JOB_NAME. ")
            print("no result info received. PLEASE CHECK JOB_NAME. ")
            exit(1)
        show_info = result_info[0]
        split_show_info = show_info.split("proxy")
        if(len(split_show_info) > 1):
            EMR_MASTER = "http://10.87.49.221:8088/cluster/"
            APP_INFO = "app/" + split_show_info[-1]
            show_info = EMR_MASTER + APP_INFO
            logger.debug("SHOW_INFO : " + show_info)
        print u"TASK信息 : \n\t%s" % show_info
        print u"当前TASK标准日志输出链接 : \n\t%s/queryJobLog.do?command=sh+%s&log_type=0&job_name=%s&job_common_is_docker=%s" % (
            host_name,
            _param["job_log_command"],
            _jobname,
            job_common_is_docker
        )
        print u"当前TASK用户日志输出链接 :  \n\t%s/queryJobLog.do?command=sh+%s&log_type=1&job_name=%s&job_common_is_docker=%s" % (
            host_name,
            _param["job_log_command"],
            _jobname,
            job_common_is_docker
        )
        exit(0)
    else:
        url = "%s/query.do?op=query&query_type=job&job_name=" % host_name + _jobname
        job_info = get(url)

    logger.debug(job_info)
    show_info = format_job_info(job_info)
    print "JOB INFO LIST FOLLOW : "
    for show_info_line in show_info:
        print u"TASK信息 : \n\t%s" % show_info_line
        print u"当前TASK标准日志输出链接 : \n\t%s/queryJobLog.do?command=sh+%s+0+%s&job_name=%s&job_common_is_docker=%s" % (
            host_name,
            _param["job_log_command"],
            show_info_line.split(" ")[0],
            _jobname,
            job_common_is_docker
        )
        print u"当前TASK用户日志输出链接 :  \n\t%s/queryJobLog.do?command=sh+%s+1+%s&job_name=%s&job_common_is_docker=%s" % (
            host_name,
            _param["job_log_command"],
            show_info_line.split(" ")[0],
            _jobname,
            job_common_is_docker
        )
# get_job_info_by_jobname("k8s")

def get_job_log_by_jobname_special_k8s(_jobname, _param = {}):
    if(len(_param) == 0):
        host_name = "http://controlcenter.ds.sina.com.cn/controlCenter-1.0.0"
    else:
        host_name = gen_host(_param)

    if(_param.has_key("job_common_submit_type")):
        job_common_submit_type = _param["job_common_submit_type"]
    if(_param.has_key("job_common_is_distributed")):
        job_common_is_distributed = _param["job_common_is_distributed"]
    if(_param.has_key("cluster_dispatch_type")):
        cluster_dispatch_type= _param["cluster_dispatch_type"]
    if(_param.has_key("job_query_command")):
        # job_query_command = "sh%20" + _param["job_query_command"] + """%20""" + """po"""
        job_query_command = "sh %s %s" % (_param["job_log_command"], _param["query_name"])
    if(job_common_submit_type == "tensorflow" and
               job_common_is_distributed == "1" and
               cluster_dispatch_type == "k8s"):
        query_status_param = {}
        query_status_param["job_name"] = _jobname
        query_status_param["command"] = job_query_command
        # url = "%s/queryJobStatus.do?command=%s&jobName=%s" % (host_name, job_query_command, _jobname)
        host_url = gen_host(_param) + "/queryJobLog.do"
        job_info = post(host_url, query_status_param)
    else:
        url = "%s/query.do?op=query&query_type=job&job_name=" % host_name + _jobname
        job_info = get(url)

    logger.debug(job_info)
    print "JOB LOG  LIST FOLLOW : "
    print job_info
# get_job_info_by_jobname("k8s")

def get_job_info_by_username(_username, _param = {}):
    if(len(_param) == 0):
        host_name = "http://controlcenter.ds.sina.com.cn/controlCenter-1.0.0"
    else:
        host_name = gen_host(_param)
    url = "%s/query.do?op=query&query_type=job&job_name=" % host_name
    job_info = get(url)
    result = json.loads(job_info).get("result")
    for job_elem in result:
        show_info = ""
        for key in filter(
                lambda _key: (_key.find("jobName") >= 0
                              or _key.find("status") >= 0
                              or _key.find("jobUrl") >= 0
                              or _key.find("submitTime") >= 0
                              or _key.find("clusterType") >= 0),
                job_elem):
            if job_elem['account'] == _username:
                show_info += "%s : %s\n\t" % (key, job_elem[key])
        logger.info("\n" + show_info)

def get_job_by_username_with_jobname(_username, _jobname, _param = {}):
    if(len(_param) == 0):
        host_name = "http://controlcenter.ds.sina.com.cn/controlCenter-1.0.0"
    else:
        host_name = gen_host(_param)
    url = "%s/query.do?op=query&query_type=job&job_name=" %host_name + _jobname
    job_info = get(url)
    result = json.loads(job_info).get("result")
    for job_elem in result:
        show_info = ""
        for key in filter(
                lambda _key: (_key.find("jobName") >= 0
                              or _key.find("status") >= 0
                              or _key.find("jobUrl") >= 0
                              or _key.find("submitTime") >= 0
                              or _key.find("clusterType") >= 0),
                job_elem):
            if job_elem['account'] == _username:
                show_info += "%s : %s\n\t" % (key, job_elem[key])
        logger.info("\n" + show_info)
# get_job_info_by_username("baozhan")

def err_show():
    print "[WARN] : Query job Informations Need Parameters."
    print "     OR  Query All job Informations Need Parameter 'all'."
    print "     OR  Query job Informations by Job Name Need Parameter '$job_name'."
    print """     OR  "-f" "--conf_file" """
    print """         "-j", "--job_name" """
    print """         "-n", "--user_name" """
    print """         "-t", "--query_type(username OR jobname)(k8s only supported jobname)" """


def query_job_info_client(_args):
    if(len(_args) < 2):
        err_show()
        exit(1)

    # list of args
    query_args = query_job_get_opts(_args[1:])
    logger.debug(query_args)

    # simple version of get all jobs.
    # weiclient query job all
    if(len(_args) == 2):
        # list after keywords query
        query_param = _args[1].lower()
        if(query_param == "all"):
            get_all_job("",query_args)
        else :
            # get_job_info_by_username(query_param)
            get_job_info_by_jobname(query_param,query_args)

    # more args for query job
    # "-f", "--conf_file")
    # "-j", "--job_name"):
    # "-n", "--user_name")
    # "-t", "--query_type"
    else:
        if(query_args.has_key("query_type")):
            query_type = query_args.get("query_type")
            if(query_type == "all"):
                get_all_job("",query_args)
            elif(query_type == "username" and query_args.has_key("user_name")):
                get_job_info_by_username(query_args.get("user_name"),query_args)
            elif(query_type == "jobname" and query_args.has_key("job_name")):
                # get_job_info_by_jobname_special_k8s(query_args.get("job_name"),query_args)
                get_all_job(query_args.get("job_name"),query_args)
            elif(query_type == "log" and query_args.has_key("query_name")):
                get_job_log_by_jobname_special_k8s(query_args.get("job_name"),query_args)
            else:
                err_show()
                exit(1)
        elif(query_args.has_key("user_name") and query_args.has_key("job_name")):
            get_job_by_username_with_jobname(
                query_args.get("user_name"),
                query_args.get("job_name"),query_args
            )
        elif(query_args.has_key("job_name")):
            get_job_info_by_jobname_special_k8s(query_args.get("job_name"),query_args)
        elif(query_args.has_key("user_name")):
            get_job_info_by_username(query_args.get("user_name"),query_args)
        elif(not query_args.has_key("query_type") and query_args.has_key("user_name")):
            get_job_info_by_username(query_args.get("user_name"),query_args)
        else:
            err_show()
            exit(1)

if __name__ == '__main__':
    query_job_info_client(sys.argv)

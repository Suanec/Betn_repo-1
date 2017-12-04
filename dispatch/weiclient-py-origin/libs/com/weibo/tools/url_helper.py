#!/usr/bin/python
# -*- coding: UTF-8 -*-
from com.weibo.tools import logger_helper

from com.weibo.tools.dict_helper import *

logger = logger_helper.wei_logger("url_helper")

# generate url by config dictionary
def gen_url_by_dict( _dict,
                     _last_dir):
    # config host_name
    client_center_host_name = 'http://controlcenter.ds.sina.com.cn'
    change_host = get_or_str(_dict,"change_host",False)
    if(change_host == 'true'):
        client_center_host_name = get_or_str(_dict,"host_name",'http://controlcenter.ds.sina.com.cn')
    # config control_center_version
    client_control_center_version = 'controlCenter-1.0.0'
    if(get_or_else(_dict,"control_center_version") != None):
        client_control_center_version = get_or_else(_dict,"client_control_center_version")
    # read user_name
    center_user_name = get_or_str(_dict,"center_user_name","Empty").strip()
    # read job_name
    job_name = get_or_str(_dict,"job_name","Empty").strip()
    # read cluster_version
    cluster_version = get_or_str(_dict,"cluster_version","1.3.0").strip()
    # read cluster_type
    cluster_type = get_or_str(_dict,"cluster_type","Empty").strip()
    # read cluster_name
    cluster_name = get_or_str(_dict,"cluster_name","Empty").strip()
    # read command
    command = get_or_str(_dict,"command","Empty").strip()
    isCheck = get_or_str(_dict, "isCheck", "1").strip()

    # config file_mode when cluster_type contains spark
    if(cluster_type.find('spark') >= 0):
        file_mode = 'rsync'
        command = 'null'
    else:
        file_mode = 'null'
    if(cluster_type.find('storm') >= 0):
        file_mode = 'rsync'
    # generate url_base
    url_base = gen_url_base_by_parameters(client_center_host_name,client_control_center_version,file_mode,cluster_type,_last_dir,center_user_name,job_name,cluster_version,command,cluster_name,isCheck)
    # generate url_base when cluster_type is tensorflow_gpu
    if(cluster_type == 'tensorflow_gpu'):
        gpu = get_or_str(_dict,"gpu")
        if(len(gpu) == 0):
            logger.error('"gpu" must be setted when cluster_type is tensorflow_gpu!')
            exit(1)
        url_base += '&gpu=%s' % gpu
    # generate url_base when cluster_type is tensorflow_cluster
    if(cluster_type == 'tensorflow_cluster'):
        ps_number = get_or_warn(_dict,"ps_number")
        env = get_or_str(_dict,"env","local").strip()
        worker_number = get_or_warn(_dict, "worker_number")
        gpu = get_or_else(_dict, "gpu", "0")
        ps_port = get_or_else(_dict, "ps_port", "2222")
        worker_port = get_or_else(_dict, "worker_port", "2223")
        url_base += '&gpu=%s&psNumber=%s&workerNumber=%s&env=%s' % (gpu,ps_number, worker_number, env)
        url_base += '&psPort=%s&workerPort=%s' % (ps_port, worker_port)
    return url_base

# generate url when parameter was configed.
def gen_url_base_by_parameters(_host_name,
                               _control_center_version,
                               _file_mode,
                               _cluster_type,
                               _last_dir,
                               _user_name,
                               _job_name,
                               _cluster_version,
                               _command,
                               _cluster_name,
                               _is_check):
    urlBase="%s/" \
            "%s/notify.do?" \
            "fileMode=%s" \
            "&clusterType=%s" \
            "&fileName=%s" \
            "&account=%s" \
            "&jobName=%s" \
            "&version=%s" \
            "&command=%s" \
            "&clusterName=%s" \
            "&isCheck=%s" % (_host_name,_control_center_version,_file_mode,_cluster_type,_last_dir,_user_name,_job_name,_cluster_version,_command,_cluster_name,_is_check)
    return urlBase

# generate url by config parameters
def gen_url_kill_job_old(_host_name="http://controlcenter.ds.sina.com.cn",
                     _control_center_version="controlCenter-1.0.0",
                     _job_name = "Empty",
                     _job_stop_command = "Empty"):
    url = "%s/" \
          "%s/killJob.do?" \
          "&command=sh+%s" \
          "&jobName=%s" % (_host_name,_control_center_version,_job_stop_command,_job_name)
    return url

def gen_url_kill_job(_client_center_host_name=
                     "http://controlcenter.ds.sina.com.cn/controlCenter-1.0.0",
                     _job_name = "Empty",
                     _job_stop_command = "Empty"):
    url = "%s/killJob.do?" \
          "&command=sh+%s" \
          "&job_name=%s" % (_client_center_host_name,_job_stop_command,_job_name)
    return url

# generate url by config dictionary for post request
def gen_url_for_post(_dict, _operations = "notify.do"):
    host_name = gen_host(_dict)
    host = "%s/%s" % (host_name, _operations)
    return host

# generate host_name by config dictionary for all request
def gen_host(_dict):
    if(_dict.has_key("client_change_host") and
               _dict["client_change_host"] == "true" and
           _dict.has_key("client_center_host_name")):
        host_name = _dict["client_center_host_name"]
    else:
        host_name = "http://controlcenter.ds.sina.com.cn"
    if(_dict.has_key("client_control_center_version")):
        client_control_center_version = _dict["client_control_center_version"]
    else:
        client_control_center_version = "controlCenter-1.0.0"
    host = "%s/%s" % (host_name, client_control_center_version)
    return host


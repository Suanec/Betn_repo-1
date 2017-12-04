#!/usr/bin/python
# -*- coding: UTF-8 -*-
# model(client)

import logging
import time

from com.weibo.tools import http_helper
from com.weibo.tools.init_get_opts import *
from com.weibo.tools.logger_helper import *
from com.weibo.tools.show_usage import *
from com.weibo.tools.sys_helper import *
from com.weibo.tools.url_helper import gen_url_for_post

from com.weibo.tools.dict_helper import *


def client_submit(_argvs):

    client_center_host_name = 'http://controlcenter.ds.sina.com.cn'
    param_map = init_get_opts(_argvs)
    if(param_map.has_key("debug") and param_map["debug"] == "true" ):
        WeiGlobalLogLevel.set_logger_level(logging.DEBUG)

    logger = wei_logger("client_submit",WeiGlobalLogLevel.get_logger_level())
    logger.debug(_argvs)
    logger.debug(client_center_host_name)
    logger.debug(_argvs)
    logger.debug(param_map)

    client_job_path = "./weibox/" + get_or_str(param_map,"client_job_path","").strip()
    client_change_host = get_or_str(param_map,"client_change_host","false")
    if(client_change_host == "true"):
        client_center_host_name = get_or_str(param_map,"client_center_host_name",'http://controlcenter.ds.sina.com.cn')

    center_user_name = get_or_str(param_map,"center_user_name","center_user_name_empty").strip()
    job_name = get_or_str(param_map,"job_name","job_name_empty").strip()
    cluster_dispatch_type = get_or_str(param_map,"cluster_dispatch_type","cluster_version_empty").strip()
    job_common_submit_type = get_or_str(param_map,"job_common_submit_type","cluster_type_empty").strip()
    job_common_is_distributed = get_or_str(param_map,"job_common_is_distributed","0").strip()
    logger.debug("client_job_path : %s" % client_job_path)

    execute_dir = get_or_str(param_map,"execute_dir","Empty").strip()
    # src_dir just allow dir
    if(os.path.isdir(client_job_path) != True):
        logger.error('client_job_path : %s just directory allowed!!' % client_job_path)
        exit(1)
    # cut /dir1/last//// to /dir1/last
    while(client_job_path.endswith('/')):
        client_job_path = client_job_path[:-1]

    time_stamp = str(long(time.time()*1e6))
    # exe_dir = src_dir + '-' + time_stamp
    # last_dir = exe_dir.split('/')[-1]
    # enzhao-spark-2.0.2-control_center-1505880713 (deprecated)
    # baozhan-tensorflow-mesos-enzhao-test-standalone-1507464913119044
    last_dir = '%s-%s-%s-%s-%s' % (center_user_name,job_common_submit_type,cluster_dispatch_type,job_name,time_stamp)

    logger.debug("client_center_host_name: %s" % client_center_host_name)
    logger.debug("client_job_path : %s" % client_job_path)
    logger.debug("center_user_name: %s" % center_user_name)
    logger.debug("job_name: %s" % job_name)
    logger.debug("cluster_dispatch_type: %s" % cluster_dispatch_type)
    logger.debug("job_common_submit_type: %s" % job_common_submit_type)
    logger.debug("execute_dir: %s" % execute_dir)
    logger.debug("last_dir: %s" % last_dir)

    show_job_info( client_center_host_name,
                   client_job_path,
                   center_user_name,
                   job_name,
                   cluster_dispatch_type,
                   job_common_submit_type,
                   execute_dir,
                   last_dir )

    data_path = get_or_else(param_map,"")
    if(data_path == None):
        logger.warn("data_path is Not Config, Ignored! ")
    elif(len(data_path) == 0):
        logger.warn("data_path is Empty!")
    else :
        logger.warn("data_path : %s" % data_path)
        data_cmd_show = "rsync -vzrtopg --progress %s fileCenter::backup/data/" % data_path
        logger.debug("rsync data_cmd: %s" % data_cmd_show)
        data_cmd = "rsync -vzrtopg --progress %s 10.77.29.68::backup/data/" % data_path
        os.system(data_cmd)
    rsync_cmd_show = "rsync -vzrtopg --progress %s/* fileCenter::backup/weiflow/%s" % (client_job_path, last_dir)
    logger.debug("rsync cmd: %s" % rsync_cmd_show)
    rsync_cmd = "rsync -vzrtopg --progress %s/* 10.77.29.68::backup/weiflow/%s" % (client_job_path, last_dir)
    if( job_common_submit_type == "spark" and
            get_or_warn(param_map, "cluster_dispatch_type") == "yarn" and
            get_or_warn(param_map, "job_common_is_docker") == "0" ):
        spark_job_jar_path = get_or_str(param_map, "job_common_submit_jar","_jar_path")
        spark_job_config = get_or_str(param_map, "job_common_submit_xml","pipeline.xml")
        spark_job_node_id = int(get_or_str(param_map, "job_common_submit_node_id","1"))
        gen_spark_weiflow(client_job_path, spark_job_jar_path, spark_job_config, spark_job_node_id)
    response_code = sys_run(rsync_cmd)
    # response_code = 0
    if(response_code != 0):
        logger.error("rsync error! With exit code %d" % response_code)
        exit(response_code)

    # if(param_map.has_key("job_submit_command")):param_map["job_command"] = param_map["job_submit_command"]
    # if(param_map.has_key("job_tensorflow_gpu_num_pertask")):
    #     param_map["job_tensorflow_gpu_num_pernode"] = param_map["job_tensorflow_gpu_num_pertask"]
    param_map = dict_enhance(param_map)
    # tensorflow_gpu_standalone
    if(job_common_submit_type == "tensorflow" and job_common_is_distributed == "0"):
        param_map = dict_param_update_tensorflow(param_map)
        param_map["file_name"] = last_dir
    # tensorflow_gpu_cluster
    elif(job_common_submit_type == "tensorflow" and
                 job_common_is_distributed == "1" and
             get_or_warn(param_map,"cluster_dispatch_type") == "mesos"):
        param_map = dict_param_update_tfcluster(param_map)
        param_map["file_name"] = last_dir
    # tensorflow_gpu_k8s_cluster
    elif(job_common_submit_type == "tensorflow" and
                 job_common_is_distributed == "1" and
                 get_or_warn(param_map, "cluster_dispatch_type") == "k8s"):
        param_map = dict_param_update_k8s(param_map)
        param_map["file_name"] = last_dir
    # storm
    elif(job_common_submit_type == "storm" and
             get_or_warn(param_map, "cluster_dispatch_type") == "storm"):
        param_map = dict_param_update_storm(param_map)
    elif(job_common_submit_type == "spark" and
        get_or_warn(param_map, "cluster_dispatch_type") == "yarn"):
        param_map = dict_param_update_spark(param_map)
        param_map["file_name"] = last_dir
    # url = gen_url_by_dict(param_map,last_dir)
    host_name = gen_url_for_post(param_map)
    logger.info("host_name = %s" % host_name)
    print "host_name = %s" % host_name
    # http_response_code = http_helper.get(url)
    http_response_code = http_helper.post(host_name, param_map)

    request_info_check(http_response_code, logger)

def run(_args = []):
    client_submit(_args)



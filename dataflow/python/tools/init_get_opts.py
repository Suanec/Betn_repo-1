#!/usr/bin/python
# -*- coding: UTF-8 -*-
import getopt
import os,sys

from com.weibo.tools import logger_helper
from com.weibo.tools.show_usage import *

logger = logger_helper.wei_logger("init_get_opts")

def load_config(_file_name = "./conf/weiclient.conf.core.site.template"):
    logger.info("Read Config File with file_name: %s" % _file_name)
    file_object = open(_file_name)
    try:
        all_the_config = file_object.read()
    finally:
        file_object.close()
    lines = all_the_config.split('\n')
    rst_dict = {}
    for line in lines :
        config = line.split('#')[0].split('=')
        if(line.startswith('#') != True
            and len(config) >= 2):
            config_name = config[0].strip()
            config_value = config[1].strip()
            rst_dict[config_name] = config_value
    return rst_dict
# load_config(_file_name="./weiclient.conf.template")

def load_core_config(_file_name = "/conf/weiclient.conf.core.site.template"):
    real_file_path = os.path.dirname(__file__)
    current_weiclient_path = os.path.abspath( real_file_path + "/../../../..")
    core_config_path = current_weiclient_path + _file_name
    core_config_file_path = os.path.abspath(core_config_path)
    core_file_dict = load_config(core_config_file_path)
    return core_file_dict

gloabl_init_known_parameter = [u'c', u'd', u'f', u'h', u'j', u'k', u'n', u't', u'v', u'x']
def init_get_opts(argv):
    # data_path= #./lib/client.sh # 数据目录，可为空，为数据传输需求提供
    # job_name=charCNN # 作业名
    # center_user_name=baozhan # 用户名
    # cluster_type=tensorflow_gpu # 任务所处集群类型
    # cluster_version=1.3.0 # 集群版本
    # cluster_name=EMR
    # src_dir=../weiclient # 客户端目录相对路径，也是控制中心任务隔离后工作目录
    #
    # host_name=http://controlcenter.ds.sina.com.cn # 控制中心域名
    # command=run.sh #start_storm.sh # storm 使用，提交任务脚本名称
    #
    # sample_name=../weiclient-test/samples/* # 样本库名称，可为目录
    # model_name=train.model # 样本库名称，可为目录
    # gpu=0 # 使用的gpu编号，0，1，2
    try:
        opts, args = getopt.getopt(argv,
                                   "hc:d:f:j:k:n:t:v:x:",
                                   ["cluster_name=",
                                    "data_path=",
                                    "conf_file=",
                                    "job_name=",
                                    "job_key=",
                                    "center_user_name=",
                                    "cluster_type=",
                                    "cluster_version=",
                                    "client_job_path="])
    except getopt.GetoptError:
        show_usage()
        sys.exit(2)
    param_dict = {}
    for opt, arg in opts:
        if opt == '-h':
            show_usage()
            sys.exit()
        elif opt in ("-c", "--cluster_name"):
            cluster_name = arg
            param_dict["cluster_name"] = cluster_name
        elif opt in ("-d", "--debug"):
            debug = arg
            param_dict["debug"] = debug
        elif opt in ("-f", "--conf_file"):
            conf_file = arg
            param_dict_file = load_core_config()
            param_dict_file.update(load_config(conf_file))
            param_dict_file.update(param_dict)
            param_dict = param_dict_file
        elif opt in ("-j", "--job_name"):
            job_name = arg
            param_dict["job_name"] = job_name
        elif opt in ("-k", "--job_key"):
            job_name = arg
            param_dict["job_key"] = job_name
        elif opt in ("-n", "--center_user_name"):
            center_user_name = arg
            param_dict["center_user_name"] = center_user_name
        elif opt in ("-t", "--cluster_type"):
            cluster_type = arg
            param_dict["cluster_type"] = cluster_type
        elif opt in ("-v", "--cluster_version"):
            cluster_version = arg
            param_dict["cluster_version "] = cluster_version
        elif opt in ("-x", "--client_job_path"):
            client_job_path = arg
            param_dict["client_job_path"] = client_job_path
    return param_dict

def query_get_opts(argv):
    try:
        opts, args = getopt.getopt(argv,
                                   "hc:f:n:j:t:",
                                   ["conf_file=",
                                    "cluster_name=",
                                    "center_user_name=",
                                    "job_name=",
                                    "query_type="])
    except getopt.GetoptError:
        show_usage_query()
        sys.exit(2)
    param_dict = {}
    for opt, arg in opts:
        if opt == '-h':
            show_usage_query()
            sys.exit()
        elif opt in ("-f", "--conf_file"):
            conf_file = arg
            # param_dict = load_config(conf_file)
            param_dict_file = load_core_config()
            param_dict_file.update(load_config(conf_file))
            param_dict_file.update(param_dict)
            param_dict = param_dict_file
        elif opt in ("-c", "--cluster_name"):
            cluster_name = arg
            param_dict["cluster_name"] = cluster_name
        elif opt in ("-n", "--center_user_name"):
            center_user_name = arg
            param_dict["center_user_name"] = center_user_name
        elif opt in ("-j", "--job_name"):
            job_name = arg
            param_dict["job_name"] = job_name
        elif opt in ("-t", "--query_type"):
            query_type = arg
            param_dict["query_type"] = query_type
    return param_dict

def query_job_get_opts(argv):
    try:
        opts, args = getopt.getopt(argv,
                                   "hf:j:n:p:t:",
                                   ["conf_file=",
                                    "job_name=",
                                    "center_user_name=",
                                    "query_name=",
                                    "query_type="])
    except getopt.GetoptError:
        show_usage_job_query()
        sys.exit(2)
    param_dict = {}
    for opt, arg in opts:
        if opt == '-h':
            show_usage_job_query()
            sys.exit()
        elif opt in ("-f", "--conf_file"):
            conf_file = arg
            param_dict_file = load_core_config()
            param_dict_file.update(load_config(conf_file))
            param_dict_file.update(param_dict)
            param_dict = param_dict_file
        elif opt in ("-j", "--job_name"):
            job_name = arg
            param_dict["job_name"] = job_name
        elif opt in ("-n", "--center_user_name"):
            center_user_name = arg
            param_dict["center_user_name"] = center_user_name
        elif opt in ("-p", "--query_name"):
            query_name = arg
            param_dict["query_name"] = query_name
        elif opt in ("-t", "--query_type"):
            query_type = arg
            param_dict["query_type"] = query_type
    return param_dict


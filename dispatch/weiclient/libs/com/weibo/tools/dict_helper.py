#!/usr/bin/python
# -*- coding: UTF-8 -*-
from com.weibo.tools import logger_helper

def get_or_else(_dict = {},
              _key = '',
              _default_value = None):
    if(_dict.has_key(_key) == False):
        value = _default_value
    else:
        value = _dict.get(_key)
    if(value == None):
        if(_default_value == None):
            return None
        else:
            return _default_value
    else:
        return value

def get_or_str(_dict = {},
                    _key = '',
                    _default_value = ''):
    if(_dict.has_key(_key) == False):
        value = _default_value
    else:
        value = _dict.get(_key)
    if(value == None):
        return _default_value
    else:
        return value

def get_or_warn(_dict = {},
               _key = '' ):
    logger = logger_helper.wei_logger("dict_helper")
    value = _dict.get(_key)
    if(value == None):
        logger.warn("key : %s Not Found !!" % _key)
        exit(1)
    else:
        return value

def dict_enhance(_dict):
    _dict["job_command"] = _dict.get("job_submit_command")
    _dict["job_tensorflow_gpu_num_pernode"] = _dict.get("job_tensorflow_gpu_num_pertask")
    return _dict

def dict_param_update_tensorflow(_dict):
    _dict["change_host"] = _dict["client_change_host"]
    _dict["host_name"] = _dict["client_center_host_name"]
    _dict["control_center_version"] = _dict["client_control_center_version"]
    _dict["cluster_type"] = "tensorflow_gpu"
    _dict["command"] = _dict["job_command"]
    _dict["isCheck"] = "1"
    _dict["gpu"] = _dict["job_tensorflow_gpu_num_pernode"]
    return _dict

def dict_param_update_tfcluster(_dict):
    _dict["change_host"] = _dict["client_change_host"]
    _dict["host_name"] = _dict["client_center_host_name"]
    _dict["control_center_version"] = _dict["client_control_center_version"]
    _dict["cluster_type"] = "tensorflow_cluster"
    _dict["command"] = _dict["job_command"]
    _dict["gpu"] = _dict["job_tensorflow_gpu_num_pernode"]
    _dict["psNumber"] = _dict["job_tensorflow_ps_number"]
    _dict["workerNumber"] = _dict["job_tensorflow_worker_number"]
    _dict["ps_port"] = _dict["job_tensorflow_ps_port"]
    _dict["worker_port"] = _dict["job_tensorflow_worker_number"]
    _dict["env"] = "local"
    return _dict

def dict_param_update_k8s(_dict):
    _dict["change_host"] = _dict["client_change_host"]
    _dict["host_name"] = _dict["client_center_host_name"]
    _dict["control_center_version"] = _dict["client_control_center_version"]
    _dict["job_submit_command"] = "sh " + _dict["job_submit_command"]
    _dict["job_query_command"] = "sh " + _dict["job_query_command"]
    _dict["job_log_command"] = "sh " + _dict["job_log_command"]
    _dict["job_stop_command"] = "sh " + _dict["job_stop_command"]
    _dict["job_command"] = _dict["job_submit_command"]
    # _dict["isCheck"] = "1"
    # _dict["gpu"] = _dict["job_tensorflow_gpu_num_pernode"]
    # _dict["psNumber"] = _dict["job_tensorflow_ps_number"]
    # _dict["workerNumber"] = _dict["job_tensorflow_worker_number"]
    # _dict["ps_port"] = _dict["job_tensorflow_ps_port"]
    # _dict["worker_port"] = _dict["job_tensorflow_worker_number"]
    _dict["env"] = "local"
    return _dict

def dict_param_update_storm(_dict):
    _dict["job_command"] = _dict["job_submit_command"]
    return _dict

def dict_param_update_spark(_dict):
    _dict["job_command"] = _dict["job_submit_command"]
    return _dict



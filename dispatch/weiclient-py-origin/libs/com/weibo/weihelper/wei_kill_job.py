#!/usr/bin/python
# -*- coding: UTF-8 -*-

from com.weibo.tools import http_helper, url_helper
from com.weibo.tools.logger_helper import wei_logger
from com.weibo.tools.show_usage import kill_request_info_check

from com.weibo.tools.dict_helper import get_or_else


def client_kill_job(_job_name = "Empty",
                    _job_stop_command ="Empty",
                    _param_map = {}):
    logger = wei_logger("wei_kill_job")
    logger.info("Job Stop Command: %s" % _job_stop_command)
    logger.info("Job Name: %s" % _job_name)
    # if(_param_map.has_key("client_change_host") and
    #            _param_map["client_change_host"] == "true"):
    #     client_center_host_name = get_or_else(_param_map,
    #                                           "client_center_host_name",
    #                                           "http://controlcenter.ds.sina.com.cn")
    # if(_param_map.has_key("client_control_center_version")):
    #     client_control_center_version = get_or_else(_param_map,
    #                                                 "client_control_center_version",
    #                                                 "controlCenter-1.0.0")

    client_center_host_name = url_helper.gen_host(_param_map)
    if(int(_param_map.get("job_common_is_docker")) == 0):
        url = url_helper.gen_url_kill_job(_client_center_host_name=client_center_host_name,
                                          _job_name=_job_name,
                                          _job_stop_command=_job_stop_command)
        post_interface = client_center_host_name + "/killJob.do"
        req_info = http_helper.post(post_interface,_param_map)
    elif(int(_param_map.get("job_common_is_docker")) == 1):
        post_interface = client_center_host_name + "/killJob.do"
        req_info = http_helper.post(post_interface,_param_map)
    else:
        logger.error("Job config error: 'Job_common_is_docker'")
        exit(1)
    kill_request_info_check(req_info)


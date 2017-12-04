#!/usr/bin/python
# -*- coding: UTF-8 -*-

from com.weibo.tools import logger_helper
from com.weibo.modules.cluster.weihelper import wei_query_job
from com.weibo.modules.cluster.weihelper import wei_query_cluster

logger = logger_helper.wei_logger("wei_query")

def run(_args = []):
    if(len(_args) < 1):
        logger.error("weicmd query ${subcommand} - supported: cluster,job")
    elif(_args[0].lower() == "cluster"):
        wei_query_cluster.query_cluster_info_client(_args)
    elif(_args[0].lower() == "job"):
        wei_query_job.query_job_info_client(_args)
    else:
        wei_query_job.query_job_info_client(["job"] + _args)

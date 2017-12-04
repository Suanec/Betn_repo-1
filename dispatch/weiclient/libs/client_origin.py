#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

from com.weibo.tools import logger_helper, init_get_opts
from com.weibo.weihelper import wei_kill_job, wei_submit, wei_rsync, wei_query_job

from com.weibo.tools import show_usage
from com.weibo.weihelper import wei_query_cluster


def client_main(_args):
    logger = logger_helper.wei_logger("client_main")
    # print _args
    # ['./bin/../libs/client_origin.py', 'kill', 'dcgan-gpu3'] - 0-based
    if(len(_args) < 2):
        logger.error(show_usage.global_usage())
        exit(1)
    if(_args[1].lower() == "submit"):
        wei_submit.client_submit(_args[2:])
    elif(_args[1].lower()  == "rsync"):
        if(len(_args) < 4):
            logger.error("weicmd rsync ${src_dir} ${dest_dir} ${target_reposity}")
        elif(len(_args) == 5):
            wei_rsync.client_rsync(_args[2], _args[3], _args[4])
        elif(len(_args) == 4):
            wei_rsync.client_rsync(_args[2], _args[3])
    elif(_args[1].lower()  == "query"):
        if(len(_args) < 3):
            logger.error("weicmd query ${subcommand} - supported: cluster,job")
        elif(_args[2].lower() == "cluster"):
            wei_query_cluster.query_cluster_info_client(_args[2:])
        elif(_args[2].lower() == "job"):
            wei_query_job.query_job_info_client(_args[2:])
        else:
            wei_query_job.query_job_info_client(["job"] + _args[2:])
    elif(_args[1].lower()  == "kill"):
        if(len(_args) < 3):
            logger.error("weicmd kill ${job_name} ${cluster_type}(can be empty) ")
        if(len(_args) <= 3):
            wei_kill_job.client_kill_job(_args[2])
        else:
            if(_args[2][0] == "-"):
                params = init_get_opts.init_get_opts(_args[2:])
                if(params.has_key("job_command") or
                       params.has_key("job_stop_command")):
                    wei_kill_job.client_kill_job(_job_name=params["job_name"],
                                                 _job_stop_command=params["job_stop_command"],
                                                 _param_map=params)
                else:
                    wei_kill_job.client_kill_job(params["job_name"])
            else:
                wei_kill_job.client_kill_job(_args[2], _args[3])
    else:
        logger.error(show_usage.global_usage())
        exit(1)


if __name__ == '__main__':
    client_main(sys.argv)


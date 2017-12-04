#!/usr/bin/python
# -*- coding: UTF-8 -*-
# model(client)

from com.weibo.tools import sys_helper
from com.weibo.tools.logger_helper import wei_logger

def client_rsync(_src_name = "",
                 _dest_name = "",
                 _target_repo = ""):
    logger = wei_logger("client_rsync")
    logger.info("src_name : %s" % _src_name)
    if(len(_target_repo) == 0):
        data_cmd_show = "rsync -vzrtopg --progress %s fileCenter::backup/data/" % _src_name
        logger.info("rsync data_cmd: %s" % data_cmd_show)
        data_cmd = "rsync -vzrtopg --progress %s 10.77.29.68::backup/data/" % _src_name
    else:
        data_cmd = "rsync -vzrtopg --progress %s %s%s" % (_src_name, _target_repo, _dest_name)
        logger.info("rsync data_cmd: %s" % data_cmd)
    sys_helper.sys_run(data_cmd)

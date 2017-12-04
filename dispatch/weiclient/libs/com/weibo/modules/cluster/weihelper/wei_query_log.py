#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import sys
import urllib2

from com.weibo.tools.url_helper import gen_host
from com.weibo.tools import logger_helper
from com.weibo.tools.init_get_opts import query_job_get_opts

logger = logger_helper.wei_logger("wei_query_log")

def query_log_client(_args):
    if(len(_args) < 2):
    #     print "[WARN] : Query job Informations Need Parameters."
    #     print "     OR  Query All job Informations Need Parameter 'all'."
    #     print "     OR  Query job Informations by Job Name Need Parameter '$job_name'."
    #     print """     OR  "-f" "--conf_file" """
    #     print """         "-j", "--job_name" """
    #     print """         "-n", "--user_name" """
    #     print """         "-t", "--query_type(username OR jobname)(k8s only supported jobname)" """
        exit(1)

if __name__ == '__main__':
    query_log_client(sys.argv)

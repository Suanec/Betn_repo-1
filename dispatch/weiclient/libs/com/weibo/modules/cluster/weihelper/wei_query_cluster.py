#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import sys
import urllib2

from com.weibo.tools.url_helper import gen_host
from com.weibo.tools import logger_helper
from com.weibo.tools.utils import privilege_completion
from com.weibo.tools.init_get_opts import query_get_opts

logger = logger_helper.wei_logger("query_cluster_info")

def useful_info(_key = ""):
    return (_key.find("version") >= 0
            or _key.find("clusterName") >= 0
            or _key.find("uiUrl") >= 0
            or _key.find("clusterType") >= 0)

def get_all_cluster(_cluster_name = "", _param = {}):
    if(len(_param) == 0):
        host_name = "http://controlcenter.ds.sina.com.cn/controlCenter-1.0.0"
    else:
        host_name = gen_host(_param)
    url = "%s/query.do?op=query&queryType=cluster&clusterName=%s" % (host_name, _cluster_name)
    response = urllib2.urlopen(url)
    cluster_info = response.read()
    result = json.loads(cluster_info).get("result")
    for cluster_elem in result:
        show_info = ""
        for key in filter(
                lambda _key: (_key.find("version") >= 0
                              or _key.find("clusterName") >= 0
                              or _key.find("uiUrl") >= 0
                              or _key.find("clusterType") >= 0),
                cluster_elem):
            show_info += "%s : %s\n\t" % (key, cluster_elem[key])
        logger.info("\n" + show_info)
# get_all_cluster("EMR")

def get_cluster_info_by_username(_username, _param = {}):
    if(len(_param) == 0):
        host_name = "http://controlcenter.ds.sina.com.cn/controlCenter-1.0.0"
    else:
        host_name = gen_host(_param)
    url = ("%s/account_group.do?account=" % host_name) + _username
    response = urllib2.urlopen(url)

    try:
        cluster_info = json.loads(response.read())[0]
    except (IndexError),e:
        logger.error("User Name %s has Wrong!!" % _username)
        exit(1)
    account = cluster_info.get("account")
    clusters = cluster_info.get("clusters")
    logger.info("Queried Account is : %s" % account + "\n\n")
    for cluster_elem in clusters:
        show_info = ""
        details = cluster_elem.get("details")
        if(cluster_elem.has_key("oprationInfo")):
            operation_info = cluster_elem.get("oprationInfo")
        if(cluster_elem.has_key("operationInfo")):
            operation_info = cluster_elem.get("operationInfo")
        for key in filter(
                lambda _key: (_key.find("version") >= 0
                              or _key.find("clusterName") >= 0
                              or _key.find("uiUrl") >= 0
                              or _key.find("clusterType") >= 0),
                details):
            show_info += "%s : %s\n\t" % (key, details[key])
        show_info += "operationInfo : %s" % privilege_completion(operation_info)
        logger.info("\n" + show_info)
# get_cluster_info_by_username("baozhan")

def get_cluster_by_username_with_clustername(_username, _clustername, _param = {}):
    if(len(_param) == 0):
        host_name = "http://controlcenter.ds.sina.com.cn/controlCenter-1.0.0"
    else:
        host_name = gen_host(_param)
    url = "%s/account_group.do?account=" % host_name + _username
    response = urllib2.urlopen(url)
    try:
        cluster_info = json.loads(response.read())[0]
    except (IndexError,StandardError),e:
        logger.error("User Name %s has Wrong!!" % _username)
        exit(1)
    account = cluster_info.get("account")
    clusters = cluster_info.get("clusters")
    logger.info("Queried Account is : %s" % account + "\n\n")
    for cluster_elem in clusters:
        show_info = ""
        details = cluster_elem.get("details")
        if(cluster_elem.has_key("oprationInfo")):
            operation_info = cluster_elem.get("oprationInfo")
        if(cluster_elem.has_key("operationInfo")):
            operation_info = cluster_elem.get("operationInfo")
        for key in filter(
                lambda _key: (_key.find("version") >= 0
                              or _key.find("clusterName") >= 0
                              or _key.find("uiUrl") >= 0
                              or _key.find("clusterType") >= 0),
                details):
            show_info += "%s : %s\n\t" % (key, details[key])
        show_info += "operationInfo : %s" % privilege_completion(operation_info)
        # if(details["clusterName"].encode("utf-8") == _clustername):
        if(details["clusterName"] == _clustername.decode("utf8")):
            logger.info("\n" + show_info)
# get_cluster_info_by_username("baozhan")

def get_group_info_by_username(_username, _param = {}):
    if(len(_param) == 0):
        host_name = "http://controlcenter.ds.sina.com.cn/controlCenter-1.0.0"
    else:
        host_name = gen_host(_param)
    url = "%s/account_group.do?account=" % host_name + _username
    response = urllib2.urlopen(url)
    try:
        cluster_info = json.loads(response.read())[0]
    except (IndexError,StandardError),e:
        logger.error("User Name %s has Wrong!!" % _username)
    finally:
        exit(1)
    account = cluster_info.get("account")
    group_name = cluster_info.get("groupName")
    group_info = cluster_info.get("groupInfo")
    group_names = cluster_info.get("groupNames")
    logger.info("Queried Account is : %s" % account + "\n")
    logger.info("Account Belong to : %s" % group_name + "\n")
    logger.info("Group Info List Below : %s" % group_info + "\n")
    logger.info("Group name has alias : %s" % group_names + "\n\n")
# get_group_info_by_username("baozhan")

def query_cluster_info_client(_args):
    if(len(_args) < 2):
        print "[WARN] : Query Cluster Informations Need Parameters."
        print "     OR  Query All Cluster Informations Need Parameter 'all'."
        print "     OR  Query Cluster Informations by User Name Need Parameter '$user_name'."
        exit(1)

    query_args = query_get_opts(_args[1:])
    if(len(_args) == 2):
        query_param = _args[1].lower()
        if(query_param == "all"):
            get_all_cluster("",query_args)
        else :
            get_cluster_info_by_username(query_param, query_args)
    else:
        if(query_args.has_key("query_type")):
            query_type = query_args.get("query_type")
            if(query_type == "all"):
                get_all_cluster("",query_args)
            elif(query_type == "username" and query_args.has_key("user_name")):
                get_cluster_info_by_username(query_args.get("user_name"), query_args)
            elif(query_type == "clustername" and query_args.has_key("cluster_name")):
                get_all_cluster(query_args.get("cluster_name"), query_args)
        elif(query_args.has_key("user_name") and query_args.has_key("cluster_name")):
            get_cluster_by_username_with_clustername(
                query_args.get("user_name"),
                query_args.get("cluster_name"), query_args
            )
        elif(query_args.has_key("cluster_name")):
            get_all_cluster(query_args.get("cluster_name"), query_args)
        elif(query_args.has_key("user_name")):
            get_cluster_info_by_username(query_args.get("user_name"), query_args)
        elif(not query_args.has_key("query_type") and query_args.has_key("user_name")):
            get_cluster_info_by_username(query_args.get("user_name"), query_args)

if __name__ == '__main__':
    query_cluster_info_client(sys.argv)

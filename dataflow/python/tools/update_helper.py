# !/usr/bin/python
# -*- coding: UTF-8 -*-

# Created by enzhao on 2017/12/11. 

import json,os,urllib2
from com.weibo.tools import logger_helper
from com.weibo.tools.http_helper import get
from com.weibo.tools.show_usage import *
from com.weibo.tools.sys_helper import *

logger = logger_helper.wei_logger("update_helper")
def check_update(_version = "0.5.2.0", _size = ""):
    url = "http://10.77.29.69:8080/controlCenter-1.0.0/api/clientUpdate"
    url = "http://10.77.29.69:8080/waic/api/clientUpdate"
    req_dict = json.loads(get(url))
    new_result = req_dict.get("result")[0]
    new_version = new_result.get("version")
    new_size = new_result.get("size")
    return not (_version == new_version and _size == new_size)

def download_weiclient_latest(_url = "", _weiclient_path = "../"):
    download_url = _url
    try:
        logger.debug("URL : " + _url)    #输出查看编码后的数据格式
        logger.debug("DOWNLOAD_URL : " + download_url)    #输出查看编码后的数据格式
        response = urllib2.urlopen(_url)
        remote_tar_bytes = response.read()
        tar_writer = open("%s/updateCache/weiclient-latest.tar" % _weiclient_path,"wb+")
        tar_writer.write(remote_tar_bytes)
        tar_writer.flush()
        tar_writer.close()
    except (urllib2.HTTPError, Exception),e:
        logger.error(e)
        exit(1)

def update_update(_cur_path = "."):
    download_url = "http://datastrategy.intra.weibo.com/software/dist/tar/weiclient/weiclient-latest.tar"
    weiclient_path = os.path.abspath(_cur_path)
    bin_dir_list = os.listdir("%s/bin" % weiclient_path)
    assert len(bin_dir_list) == 1
    assert bin_dir_list[0] == "weiclient"
    # prepare_cmd = "mkdir %s/updateCache"
    if(not os.path.isdir("%s/updateCache" % weiclient_path)):
        os.mkdir("%s/updateCache" % weiclient_path)
    # download_cmd = "wget -c -t 10 http://datastrategy.intra.weibo.com/software/dist/tar/weiclient/weiclient-0.5.0.1.tar -P %s/updateCache/"
    download_weiclient_latest(download_url, weiclient_path)
    untar_cmd = "tar -xf %s/updateCache/weiclient-latest.tar -C %s/updateCache/" % (weiclient_path,weiclient_path)
    # update_cmd = "rm -rf ./*; cp -r %s/updateCache/weiclient/libs/* %s/libs/"
    update_cmd = "cp -rf %s/updateCache/weiclient/libs/* %s/libs/" % (weiclient_path,weiclient_path)
    # cleansing_cmd = "rm -rf %s/updateCache"
    cleansing_cmd = "echo 'NEED : rm -rf %s/updateCache'" % weiclient_path
    print "after run"
    cmds = [untar_cmd, update_cmd, cleansing_cmd]
    # print cmds
    map( lambda cmd : sys_run(cmd), cmds)

def update(_cur_path = ".", _version = "0.5.2.0", _size = "1594368"):
    if(check_update(_version,_size)):
        update_update(_cur_path)
        print "update successed !! please restart weiclient."
        exit(0)



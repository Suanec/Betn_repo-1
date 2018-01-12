#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib, urllib2
import json

from com.weibo.tools import logger_helper
from com.weibo.tools import dict_helper

logger = logger_helper.wei_logger("http_helper")

#GET：
def get(_url):
    try:
        logger.debug("URL : " + _url)    #输出查看编码后的数据格式
        response = urllib2.urlopen(_url)
        req_info = response.read()
        logger.debug("%s" % dict_helper.json_format(req_info))
        return req_info
    except (urllib2.HTTPError, Exception),e:
        logger.error(e)
        exit(1)

#POST：
def post(_url,
         _values):
    try:
        data = urllib.urlencode(_values)    #适用urllib对数据进行格式化编码
        logger.debug("URL : " + _url)    #输出查看编码后的数据格式
        logger.debug("DATA : " + data)    #输出查看编码后的数据格式
        req = urllib2.Request(_url, data)    #生成页面请求的完整数据
        response = urllib2.urlopen(req)     #发送页面请求
        req_info = response.read()
        logger.debug("%s" % dict_helper.json_format(req_info))
        return req_info
    except (urllib2.HTTPError, Exception),e:
        logger.error(e)
        exit(1)
    return req_info    #获取服务器返回的页面信息

#POST_json：
def post_json(_url,
              _values):
    try:
        headers = {'Content-Type': 'application/json'}
        if(not _values.has_key("body")):
            raise IOError("url data encode when post json data. because of cannot found json body")
        json_assert = json.loads(_values.get("body"))
        data = _values.get("body")
        param_value = _values.copy()
        param_value.pop("body")
        param = urllib.urlencode(param_value)
        _url += ("?" + param)
        logger.debug("URL : " + _url)    #输出查看编码后的数据格式
        logger.debug("DATA : " + data)    #输出查看编码后的数据格式
        req = urllib2.Request(url=_url, data=data, headers=headers)    #生成页面请求的完整数据
        response = urllib2.urlopen(req)     #发送页面请求
        req_info = response.read()
        logger.debug(req_info)
        return req_info
    except (urllib2.HTTPError, Exception),e:
        logger.error(e)
        exit(1)
    return req_info    #获取服务器返回的页面信息
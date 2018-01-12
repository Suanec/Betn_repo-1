# !/usr/bin/python
# -*- coding: UTF-8 -*-

# Created by enzhao on 2017/12/11. 
import getopt
import os,sys

from com.weibo.tools import logger_helper
from com.weibo.tools.show_usage import *
from com.weibo.tools import dict_helper
from com.weibo.tools import init_get_opts

logger = logger_helper.wei_logger("args_helper")


def paramter_convertor(_param_dict = {}):
    _param_dict["job_name"] = dict_helper.get_or_else(
        _param_dict, "j",
        dict_helper.get_or_else(_param_dict, "job_name", "ERROR_JOB_NAME")
    )
    _param_dict["center_user_name"] = dict_helper.get_or_else(
        _param_dict, "n",
        dict_helper.get_or_else(_param_dict, "center_user_name", "ERROR_USER_NAME")
    )
    _param_dict["job_key"] = dict_helper.get_or_else(
        _param_dict, "k",
        dict_helper.get_or_else(_param_dict, "job_key", "EMPTY_JOB_KEY")
    )
    config_path = _param_dict.get("config") if _param_dict.has_key("config") else _param_dict.get("f")
    core_config_file_path = os.path.dirname(os.path.abspath(sys.argv[0])) + "/../conf/weiclient.conf.core.site.template"
    core_dict = init_get_opts.load_config(core_config_file_path)
    if(isinstance(config_path,str)):
        user_dict = init_get_opts.load_config(config_path)
        core_dict.update(user_dict)
    core_dict.update(_param_dict)
    return core_dict


def long_args_resolver(_args_arr = []):
    _args = filter(
        lambda x : len(x) > 0,
        _args_arr
    )
    args_size = len(_args)
    if(args_size <= 1):
        logger.error("long_args_resolver found error args less than one argument.")
        exit(1)
    args_dict = {}
    i = 0
    while(i < args_size):
        arg_pair = _args[i]
        pair_dict = long_args_pair_resolver(arg_pair)
        args_dict.update(pair_dict)
        i += 1
    if(i != args_size):
        logger.error("found error when finish parse arguments.")
        exit(1)
    return args_dict

def long_args_pair_resolver(_args = ""):
    pair_dict = {}
    arg_pair = _args
    if(not (arg_pair.startswith("--") and arg_pair.find("=") >= 0)):
        logger.error("error found long arguments : [%s]" % arg_pair)
        exit(1)
    [arg_key,arg_value] = arg_pair.split('=')
    logger.debug("parsed args pair : %s." % arg_pair)
    pair_dict[arg_key[2:]] = arg_value
    return pair_dict


def short_args_resolver(_args_arr = []):
    _args = filter(
        lambda x : len(x) > 0,
        _args_arr
    )
    args_size = len(_args)
    if(args_size <= 1):
        logger.error("short_args_resolver found error args less than one argument.")
        exit(1)
    args_dict = {}
    i = 0
    while(i < args_size):
        arg_pair = _args[i]
        pair_dict = short_args_pair_resolver(arg_pair)
        args_dict.update(pair_dict)
        i += 1
    if(i != args_size):
        logger.error("found error when finish parse arguments.")
        exit(1)
    return args_dict

def short_args_pair_resolver_equals1(_args = []):
    pair_dict = {}
    arg_pair = _args
    if(not (arg_pair.startswith("-") and arg_pair.find("=") >= 0)):
        logger.error("error found arguments : [%s]" % arg_pair)
        exit(1)
    [arg_key,arg_value] = arg_pair.split('=')
    logger.debug("parsed args pair : %s." % arg_pair)
    pair_dict[arg_key[1:]] = arg_value
    return pair_dict
def short_args_pair_resolver_equals(_args = []):
    pair_dict = {}
    arg_pair = _args
    equal_idx = arg_pair.find("=")
    if(arg_pair.startswith("-") and equal_idx >= 0):
        # arg_key = arg_pair[1] if equal_idx == 2 else arg_pair[1:equal_idx]
        arg_key = arg_pair[1:equal_idx]
        arg_value = arg_pair[equal_idx+1:]
        # [arg_key,arg_value] = arg_pair.split('=')
        logger.debug("parsed args pair : %s." % arg_pair)
    pair_dict[arg_key] = arg_value
    return pair_dict

def short_args_pair_resolver(_args = []):
    pair_dict = {}
    arg_pair = _args
    if(not (arg_pair.startswith("-") and arg_pair.find("=") >= 0)):
        logger.error("error found arguments : [%s]" % arg_pair)
        exit(1)
    [arg_key,arg_value] = arg_pair.split('=')
    logger.debug("parsed args pair : %s." % arg_pair)
    pair_dict[arg_key[1:]] = arg_value
    return pair_dict

def args_resolver_by_and(_args_arr = []):
    _args = filter(
        lambda x : len(x) > 0,
        _args_arr
    )
    args_size = len(_args)
    if(args_size <= 1):
        logger.error("args_resolver found error args less than one argument.")
        exit(1)
    args_dict = {}
    i = 0
    while(i < args_size):
        arg_pair = _args[i]
        if(arg_pair[0:2] == "--" and arg_pair.find("=") > 0):
            pair_dict = long_args_pair_resolver(arg_pair)
        elif (arg_pair[0:2] == "--" and arg_pair.find("=") < 0):
            pair_dict = {arg_pair[2:] : _args[i+1]}
            args_dict.update(pair_dict)
            i += 2
            continue
        elif (arg_pair[0:1] == "-" and arg_pair.find("=") > 0):
            pair_dict = short_args_pair_resolver_equals(arg_pair)
        elif (arg_pair[0:1] == "-" and arg_pair.find("=") < 0):
            pair_dict = {arg_pair[1:] : _args[i+1]}
            args_dict.update(pair_dict)
            i += 2
            continue
        else:
            logger.error("error found arguments : [%s]" % arg_pair)
            exit(1)
        args_dict.update(pair_dict)
        i += 1
    if(i != args_size):
        logger.error("found error when finish parse arguments.")
        exit(1)
    return args_dict

def args_resolver(_args_arr = [], _known_keys = []):
    _args = filter(
        lambda x : len(x) > 0,
        _args_arr
    )
    args_size = len(_args)
    if(args_size <= 1):
        logger.error("args_resolver found error args less than one argument.\n")
        exit(1)
    args_dict = {}
    i = 0
    while(i < args_size):
        arg_pair = _args[i]
        if(arg_pair[0:2] == "--"):
            if(arg_pair.find("=") > 0):
                pair_dict = long_args_pair_resolver(arg_pair)
            else:
                pair_dict = {arg_pair[2:] : _args[i+1]}
                args_dict.update(pair_dict)
                i += 2
                continue
        elif (arg_pair[0:1] == "-"):
            if(arg_pair.find("=") > 0):
                pair_dict = short_args_pair_resolver_equals(arg_pair)
            else:
                if((i+1 == args_size) or _args[i+1].startswith("-")):
                    logger.error("parameter founds error. please check.\n")
                    exit(1)
                pair_dict = {arg_pair[1:] : _args[i+1]}
                args_dict.update(pair_dict)
                i += 2
                continue
        else:
            logger.error("error found arguments : [%s]" % arg_pair)
            exit(1)
        args_dict.update(pair_dict)
        i += 1
    if(i != args_size):
        logger.error("found error when finish parse arguments.")
        exit(1)
    invalid_key = [key for key in args_dict.keys() if key not in _known_keys]
    if(len(_known_keys) > 0 and
               len(invalid_key) > 0):
        logger.error("invalid parameter keys found. %s " % invalid_key[0])
        exit(1)
    return args_dict



#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging

class WeiGlobalLogLevel:
    logger_level = logging.INFO
    @staticmethod
    def set_logger_level(_level = logging.INFO):
        WeiGlobalLogLevel.logger_level = _level
    @staticmethod
    def get_logger_level():
        return WeiGlobalLogLevel.logger_level

def wei_logger(_cls_name = "logger_helper",
               _log_level = WeiGlobalLogLevel.get_logger_level()):
    _format_str = '[%(levelname)s] : %(asctime)s %(filename)s[line:%(lineno)d]  %(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        format=_format_str,
                        filename='weiclient.log',
                        datefmt='%Y/%m/%d %H:%M:%S %a')
    console = logging.StreamHandler()
    console.setLevel(logging.WARN)
    console_formatter = logging.Formatter(_format_str)
    console.setFormatter(console_formatter)
    logger = logging.getLogger(_cls_name)
    logger.addHandler(console)
    logger.debug('%s logger init success!!' % _cls_name)
    return logger


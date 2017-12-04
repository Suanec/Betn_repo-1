# !/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

from com.weibo.reflection.libs.ref_load import *
# args = ["algorithm","cluster","init"]
def gen_module_name(_name = ""):
  _module_name = "com.weibo.modules."+_name + "." + _name + "_client"
  return _module_name

def client(_args = []):
  _file_name = _args[0]
  _module_name = gen_module_name(_args[1])
  _client_param = _args[2:]
  print _client_param
  obj_func = ref_load(_module_name)
  obj_func(_client_param)

if __name__ == '__main__':
  client(sys.argv)
# !/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

from com.weibo.reflection.libs.ref_load import *


def gen_module_name(_name = ""):
  return "com.weibo.modules.algorithm.wei_" + _name

def run(_args):
  _func_name = sys._getframe().f_code.co_name
  _file_name = __file__.split("/")[-1].split(".py")[0]
  print "this is " + _file_name + " " + _func_name  + " function."
  print _args
  ref_load(gen_module_name(_args[0]))(_args[1:])

if __name__ == "__main__":
  run()

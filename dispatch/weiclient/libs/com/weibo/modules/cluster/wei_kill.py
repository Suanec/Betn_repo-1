# !/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

def run(_args):
  _func_name = sys._getframe().f_code.co_name
  _file_name = __file__.split("/")[-1].split(".py")[0]
  print "this is " + _file_name + " " + _func_name  + " function."
  print _args

if __name__ == "__main__":
  run()

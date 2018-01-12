# !/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

def ref_load(_module_name = ""):
    if(sys.modules.has_key(_module_name)):
      del sys.modules[_module_name]
    try:
        modules_client = __import__(_module_name, fromlist = True)
    except ImportError:
        print "ImportError: No module named %s" % _module_name
        print "please check you command usage."
        exit(1)
    assert hasattr(modules_client,"run"),  "could not find function for client init," + \
      " please check version of weiclient."
    obj_func = getattr(modules_client,"run",None)
    return obj_func

# _args[0] : module_name
# _args[1] : module_parameters

def ref_call(_args = []):
    obj_func = ref_load(_args[0])
    obj_func(_args[1:])


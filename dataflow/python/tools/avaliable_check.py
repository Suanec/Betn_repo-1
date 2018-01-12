# !/usr/bin/python
# -*- coding: UTF-8 -*-

# Created by enzhao on 2017/12/27.
import os

# **********************************************
# MODULE AVALIABLE CHECK
# **********************************************

# count supportted module by list directory name
def module_avaliable_count(_file_name =""):
    file_abs_path = os.path.abspath(__file__) if(_file_name == "") else _file_name
    (file_real_path, file_real_name) = os.path.split(file_abs_path)
    module_dirs = sorted([dir_name
                   for dir_name in os.listdir(file_real_path)
                   if os.path.isdir(file_real_path+"/"+dir_name)])
    return module_dirs

# show module help info
def global_usage():
    usage = "Usage: weiclient [MODULE_NAME] [COMMAND] \n" \
            + "\n" \
            + "  where MODULE_NAME is one of:\n" \
            + "\n" \
            + "    algorithm                             algorithm job command\n" \
            + "\n" \
            + "    cluster                               cluster job command\n" \
            + "\n" \
            + "    init                                  init job command\n" \
            + "\n" \
            + "    version                               print the version\n" \
            + "\n" \
            + "    query                                 query info command\n" \
            + "\n" \
            + "    template                              develop api for developer\n" \
            + "\n" \
            + "Most commands print help when invoked w/o parameters.\n"
    return usage

def parameter_usage(_subcommand = ""):
    usage = "Usage: weiclient %s [COMMAND] \n" % _subcommand
    usage +=  "\n" \
            + "  where COMMAND is one of:\n" \
            + "\n" \
            + "    submit                                  action submit\n" \
            + "    query                                   action query\n" \
            + "    kill                                    action kill\n" \
            + "\n" \
            + " PARAMETERS supported:                  \n" \
            + "\n" \
            + "    -j <job_name>                           job_name setter\n" \
            + "    -k <job_key>                            job_key setter\n" \
            + "    -n <center_user_name>                   user_name setter\n" \
            + "    -x <client_job_path>                    client_job_path setter\n" \
            + "\n" \
            + " OR \n" \
            + "    -f <conf_file>                 config_file setter (RECOMMENDED)\n" \
            + "\n" \
            + "Most commands print help when invoked w/o parameters."
    return usage

def module_help_info(_file_path = ""):
    print "module name Found Error !"
    print "supportted module : "
    print module_avaliable_count(_file_path)

def module_check(_module_name = "", _file_path = ""):
    return _module_name in module_avaliable_count(_file_path)

def module_avaliable_check(_args = [], _file_path =""):
    if( not (len(_args) > 1 and module_check(_args[1], _file_path)) ):
        module_help_info(_file_path)
        print global_usage()
        exit(1)
    # elif( len(_args) > 1 and not module_check(_args[1], _file_path) )

# **********************************************
# SUBCOMMAND AVALIABLE CHECK
# **********************************************

def subcommand_avaliable_count(_file_name ="", _format = "wei_"):
    file_abs_path = os.path.abspath(__file__) if(_file_name == "") else _file_name
    (file_real_path, file_real_name) = os.path.split(file_abs_path)
    subcommand_files = sorted([dir_name.replace(_format,"").replace(".py","")
                          for dir_name in os.listdir(file_real_path)
                          if((not dir_name.endswith(".pyc")) and
                             dir_name.startswith(_format))])
    return subcommand_files

def subcommand_help_info(_file_path = "", _format = "wei_"):
    print "sub command Found Error !"
    print "supportted COMMAND : "
    print subcommand_avaliable_count(_file_path, _format)

def subcommand_check(_subcommand = "", _file_path = "", _format = "wei_"):
    return _subcommand in subcommand_avaliable_count(_file_path, _format)

def subcommand_avaliable_check(_args = [], _file_path = "", _format = "wei_"):
    # if(not(len(_args) > 1 and ))
    # pass
    print _args
    if(len(_args) < 1):
        subcommand_help_info(_file_path, _format)
        print parameter_usage()
        exit(1)
    elif (len(_args) > 2):
        if(not subcommand_check(_args[0], _file_path)):
            subcommand_help_info(_file_path, _format)
            print parameter_usage(_args[0])
            exit(1)





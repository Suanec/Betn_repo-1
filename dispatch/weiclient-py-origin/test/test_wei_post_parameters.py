#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random, unittest, sys, os
from src.libs.init_get_opts import init_get_opts
from src.libs.http_helper import post, get

class TestClient(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)
        print "hello world"

    def test_post(self):
        args = ["asdf","kill", "-f",
                "../src/conf/weiclient.conf.template",
                "-j",
                "kill_job_asdf"]
        paramMap = init_get_opts(args[2:])
        paramMap["change_host"] = paramMap["client_change_host"]
        paramMap["host_name"] = paramMap["client_center_host_name"]
        paramMap["control_center_version"] = paramMap["client_control_center_version"]
        paramMap["cluster_type"] = "tensorflow_gpu"
        paramMap["command"] = paramMap["job_command"]
        paramMap["gpu"] = paramMap["job_tensorflow_gpu_num_pernode"]
        # paramMap[""] = paramMap[""]
        # paramMap[""] = ""
        cc_host_name = paramMap["client_center_host_name"]
        host_name = "http://127.0.0.1:12306/index.html"
        get_host_name = "http://127.0.0.1:12306?fileMode=null&clusterType=tensorflow_gpu&account=baozhan&" \
                        "jobName=tfgpu13&version=1.3.0&command=start-deepctr.sh&clusterName=shishi&isCheck=1&gpu=2"
        get_cc_host_name = cc_host_name + "/controlCenter-1.0.0/notify.do?" \
                                          "fileMode=null&" \
                                          "clusterType=tensorflow_gpu&" \
                                          "fileName=baozhan-tensorflow-mesos-tfgpu13-1507621331457312&" \
                                          "account=baozhan&" \
                                          "jobName=tfgpu13&" \
                                          "version=1.3.0&" \
                                          "command=start-deepctr.sh&" \
                                          "clusterName=shishi&" \
                                          "isCheck=1&" \
                                          "gpu=2"
        post_cc_host_name = cc_host_name + "/controlCenter-1.0.0/notify.do"
        paramMap["fileMode"]="null"
        paramMap["clusterType"]="tensorflow_gpu"
        paramMap["fileName"]="baozhan-tensorflow-mesos-tfgpu13-1507621331457312"
        paramMap["account"]="baozhan"
        paramMap["jobName"]="tfgpu13"
        paramMap["version"]="1.3.0"
        paramMap["command"]="start-deepctr.sh"
        paramMap["clusterName"]="shishi"
        paramMap["isCheck"]="1"
        paramMap["gpu"]="2"

        # get(get_host_name)
        # get(get_cc_host_name)
        req = post(post_cc_host_name, paramMap)
        print req


if __name__ == '__main__':
    print "hello world"
    # sys.path.append("../weiclient/libs/client.py")
    # unittest.main()
    # TestClient.test_spark()

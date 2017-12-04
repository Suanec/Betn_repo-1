#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random, unittest, sys
from weiclient.libs.com.weibo.tools.show_usage import *
from weiclient.libs.client import client_main
# import libs.query_job_info
# import libs.client
# import libs.show_usage

class TestClient(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)
        print "hello world"


    def test_query(self):
        # args = ["asdf","query", "job","-t","jobname","-j","GenFeatureConfCC"]
        # args = ["./bin/weiclient","query", "job", "-t", "jobname",
        #         "-f",  "/Users/enzhao/suanec/ksp/dispatch/weiclient/conf/weiclient.conf.tf.k8s.template",
        #         "-j",  "query-k8s-status-1"]
        args = ["./bin/weiclient","query", "job", "-t", "log",
                "-f",  "/Users/enzhao/suanec/ksp/dispatch/weiclient/conf/weiclient.conf.tf.k8s.template",
                "-j",  "query-k8s-status-1",
                "-p",  "0 query-k8s-status-1-ps-0-738813975-gbp9m"]
        args = ["./bin/weiclient","query", "job",
                "-f",  "/Users/enzhao/suanec/ksp/dispatch/weiclient/conf/weiclient.conf.spark.yarn.template",
                "-t",  "jobname",
                "-j",  "query-spark-00"]
        args = ["./bin/weiclient","query",
                "-f",  "./conf/weiclient.conf.tf.weik8s.template",
                "-j",  "query-k8s-10"]
        # libs.query_job_info.get_all_job("GenFeatureConfCC")
        client_main(args)
        # show_success_info()


if __name__ == '__main__':
    print "hello world"

    unittest.main()

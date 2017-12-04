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
        args = ["asdf","query", "job","-t","jobname","-j","GenFeatureConfCC"]
        args = ["./bin/weiclient","submit",  "-f",  "/Users/enzhao/suanec/ksp/dispatch/weiclient/conf/weiclient.conf.tf.basedocker.template",  "-j",  "weiclient-basedocker"]
        # libs.query_job_info.get_all_job("GenFeatureConfCC")
        client_main(args)
        show_success_info()


if __name__ == '__main__':
    print "hello world"

    unittest.main()

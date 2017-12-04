#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random, unittest, sys, os
from client import client_main

class TestClient(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)
        print "hello world"

    def test_kill(self):
        args = ["asdf","kill", "-f",
                "/Users/enzhao/suanec/ksp/dispatch/git-weiclient/weiclient/release/weiclient-deepctr/conf/weiclient.conf.template",
                "-j",
                "kill_job_asdf"]
        args = ["./bin/weiclient","kill",
                "-f",  "/Users/enzhao/suanec/ksp/dispatch/weiclient/conf/weiclient.conf.tf.k8s.template",
                "-j",  "query-k8s-status-1" ]
        client_main(args)

if __name__ == '__main__':
    print "hello world"
    # sys.path.append("../weiclient/libs/client.py")
    # unittest.main()
    # TestClient.test_spark()

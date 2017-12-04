#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random, unittest, sys
import url_helper
import init_get_opts

class TestUrlHelper(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)
        print "hello world"

    def test_url_for_post(self):
        args = ["-f", "../conf/weiclient.conf.template"]
        pms = init_get_opts.init_get_opts(args)
        host = url_helper.gen_url_for_post(pms)
        print host
if __name__ == '__main__':
    print "hello world"
    unittest.main()

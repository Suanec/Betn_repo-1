#!/usr/bin/python
# -*- coding: UTF-8 -*-

def echo(_obj):
    def show(_value): print _value
    map(show,_obj)

def privilege_completion(_privilege = "w"):
    if(_privilege == "w"):
        return "write"
    elif(_privilege == "r"):
        return "read"
    elif(_privilege == "wr"):
        return "read and write"
    else:
        return "null"


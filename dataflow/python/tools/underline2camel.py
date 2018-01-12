# !/usr/bin/python
# -*- coding: UTF-8 -*-

# Created by enzhao on 2018/1/12.
def tail_underline_to_camel(_valiable = ""):
    parts = [x for x in _valiable.split("_") if len(x) > 0]
    if(len(parts) < 2):
        return parts
    camel_valiable = parts[0]
    tails = parts[1:]
    camel_tail = [part[0].upper() + part[1:] for part in tails]
    for x in camel_tail:
        camel_valiable += x
    return camel_valiable

def underline_to_camel(_valiable = ""):
    for index in range(0,len(_valiable)):
        if(_valiable[index] != "_"):
            break
    tail_camel_result = tail_underline_to_camel(_valiable[index:])
    camel_result = ""
    for i in range(0,index):
        camel_result += "_"
    return camel_result + tail_camel_result



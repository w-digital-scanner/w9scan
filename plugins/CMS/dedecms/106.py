#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Ario'
import re

def assign(service, arg):
    if service == "dedecms":
        return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl(url + 'data/admin/ver.txt')
    if code == 200:
        m = re.search('^(\d+)$', res)
        if m:
            security_info('TimeStamp: %s, Possible Version: %s' % (m.group(1), check_ver(m.group(1))))

def check_ver(arg):
    ver_histroy = {'20080307': 'v3 or v4 or v5',
                 '20080324': 'v5 above',
                 '20080807': '5.1 or 5.2',
                 '20081009': 'v5.1sp',
                 '20081218': '5.1sp',
                 '20090810': '5.5',
                 '20090912': '5.5',
                 '20100803': '5.6',
                 '20101021': '5.3',
                 '20111111': 'v5.7 or v5.6 or v5.5',
                 '20111205': '5.7.18',
                 '20111209': '5.6',
                 '20120430': '5.7SP or 5.7 or 5.6',
                 '20120621': '5.7SP1 or 5.7 or 5.6',
                 '20120709': '5.6',
                 '20121030': '5.7SP1 or 5.7',
                 '20121107': '5.7',
                 '20130608': 'V5.6-Final',
                 '20130922': 'V5.7SP1'}
    ver_list = sorted(list(ver_histroy.keys()))
    ver_list.append(arg)
    sorted_ver_list=sorted(ver_list)
    return ver_histroy[ver_list[sorted_ver_list.index(arg) - 1]]

if __name__ == '__main__':
    from dummy import *
    audit(assign('dedecms', 'http://www.ceowo.com/')[1])

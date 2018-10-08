#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '半块西瓜皮'
import socket
def audit(arg):
    ip,port = arg
    info = []
    try:
        s = socket.socket()
        s.connect((ip,port))
        s.send("\x3F\x00\x00\x00\x7E\x00\x00\x00\x00\x00\x00\x00\xD4\x07\x00\x00\x04\x00\x00\x00\x61\x64\x6D\x69\x6E\x2E\x24\x63\x6D\x64\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x18\x00\x00\x00\x10\x6C\x69\x73\x74\x44\x61\x74\x61\x62\x61\x73\x65\x73\x00\x01\x00\x00\x00\x00")
        data = s.recv(1024)
        if 'local' in data:
            security_hole("%s:%d" % (ip,port))
        s.close()
    except:
        pass
    url = 'http://%s:%d/' % (ip,port+1000)
    code ,_ ,body ,_,_ = curl.curl(url)
    if code == 200 and 'db version' in body:
        security_info(url)
def assign(service, arg):
    if service == "mongodb":
        return True, arg

if __name__ == '__main__':
    from dummy import *
    audit(assign('mongodb', ('58.215.185.154',27017))[1])

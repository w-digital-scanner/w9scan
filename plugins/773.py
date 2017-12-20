#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = DWBH
# __type__  = mongodb弱口令检测

import urlparse
import socket
import re
import hashlib
import struct
def md5(data):
    return hashlib.md5(data).hexdigest()
def haveauth(s):
    try:
        s.sendall('\x3F\x00\x00\x00\x97\x75\xBC\x60\xFF\xFF\xFF\xFF\xD4\x07\x00\x00\x00\x00\x00\x00\x61\x64\x6D\x69\x6E\x2E\x24\x63\x6D\x64\x00\x00\x00\x00\x00\x01\x00\x00\x00\x18\x00\x00\x00\x10\x6C\x69\x73\x74\x44\x61\x74\x61\x62\x61\x73\x65\x73\x00\x01\x00\x00\x00\x00')
        data = s.recv(1024)
        if 'databases' in data and 'local' in data:
            return False
    except:
        pass
    return True
    


def getnonce(s,ip,port):
    getnone="\x3A\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\xD4\x07\x00\x00"
    getnone=getnone+"\x00\x00\x00\x00\x61\x64\x6D\x69\x6E\x2E\x24\x63\x6D\x64\x00\x00"
    getnone=getnone+"\x00\x00\x00\xFF\xFF\xFF\xFF\x13\x00\x00\x00\x10\x67\x65\x74\x6E"
    getnone=getnone+"\x6F\x6E\x63\x65\x00\x01\x00\x00\x00\x00"

    s.sendall(getnone)
    data = s.recv(1024)
    #print repr(data)
    m = re.search(r'\w{16}',data)
    if m:
         return m.group(0)
    else:
        return None
def getauth(s,user,nonce,key):
    head = "\x03\x00\x00\x00\x00\x00\x00\x00\xD4\x07\x00\x00\x00\x00\x00\x00\x61\x64\x6D\x69\x6E\x2E\x24\x63\x6D\x64\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF"
    e1 = "\x10\x61\x75\x74\x68\x65\x6E\x74\x69\x63\x61\x74\x65\x00\x01\x00\x00\x00"
    userlen=struct.pack("i",len(user)+1)
    e2 = "\x02\x75\x73\x65\x72\x00"+userlen+user+"\x00"
    noncelen=struct.pack("i",len(nonce)+1)
    e3 = "\x02\x6E\x6F\x6E\x63\x65\x00"+noncelen+nonce+"\x00"
    keylen=struct.pack("i",len(key)+1)
    e4 = "\x02\x6B\x65\x79\x00"+keylen+key+"\x00"
    e = e1+e2+e3+e4+'\x00'
    document = struct.pack("i",len(e)+4)+e
    auth = struct.pack("i",len(document)+len(head)+4)+head+document
    s.sendall(auth)
    data = s.recv(1024)
    if "\x01\x6F\x6B\x00\x00\x00\x00\x00\x00\x00\xF0\x3F" in data:
        return True
    else:
        return False
    


def getkey(user,password,nonce):
    return md5(nonce+user+md5(user+':mongo:'+password))

def assign(service, arg):
    if service == "mongodb":
        return True, arg
    
def audit(args):
    ip,port=args
    try:
        s = socket.socket()
        s.connect((ip,port))
        if not haveauth(s):
            return
        pass_list = util.load_password_dict(
            ip,
            userfile='database/mysql_user.txt', 
            passfile='database/mysql_pass.txt',
            mix=True,
            )
        
        
        for u,p in pass_list:
            nonce=getnonce(s,ip,port)
            if not nonce:
                s.close()
                return
            ok = getauth(s,u,nonce,getkey(u,p,nonce)) 
            if ok:
                security_hole("mongodb://%s:%s@%s:%d" % (u,p,ip,port))
                s.close()
                return
    except:
        pass




if __name__ == '__main__':
    from dummy import *
    audit(assign('mongodb', ('127.0.0.1',27017))[1])


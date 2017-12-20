#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = DWBH
# __type__  = postgresSQL  md5加密方式弱口令检测

import urlparse
import socket
import re
import hashlib
import struct


def getauth(s,username,password):
    typeu="\x00\x03\x00\x00"
    user="\x75\x73\x65\x72\x00"
    uservalue=username+"\x00"
    db="\x64\x61\x74\x61\x62\x61\x73\x65\x00"
    dbvalue="\x00"
    app="\x61\x70\x70\x6C\x69\x63\x61\x74\x69\x6F\x6E\x5F\x6E\x61\x6D\x65\x00"
    appvalue="psql"+"\x00"
    encode="\x63\x6C\x69\x65\x6E\x74\x5F\x65\x6E\x63\x6F\x64\x69\x6E\x67\x00"
    encodevalue="\x47\x42\x4B\x00"
    data=typeu+user+uservalue+db+dbvalue+app+appvalue+encode+encodevalue+"\x00"
    payload=struct.pack("!i",len(data)+4)+data
    try:
        s.sendall(payload)
        res = s.recv(1024)
        authtype = struct.unpack("!i",res[5:9])[0]
        if res[0]=="R":
            if authtype==0:
                return 'noauth',0
            if authtype==5:
                return "md5",makeauth(username,password,res[-4:])
            else:
                return "auth",struct.unpack("!i",res[5:9])[0]
    except:
        pass
    return "baduser",-1
            


        
def md5(data):
    return hashlib.md5(data).hexdigest()
  
def makeauth(username,password,key):
    return 'md5'+md5(md5(password+username)+key)




def sendauth(s,auth):
    authstye="\x70\x00\x00\x00\x28"
    auth=authstye+auth+"\x00"
    try:
        s.sendall(auth)         
        data=s.recv(1024)
        if data[0]=="R" and data[5:9]=="\x00\x00\x00\x00":
            return True
    except:
        pass
    return False

def createsocket(ip,port):
    for x in range(10):
        try:
            s = socket.socket()
            s.connect((ip,port))        
            return s
        except:
            pass
    
def assign(service, arg):
    if service == "postgresql":
        return True, arg

def audit(args):
    ip,port=args
    baduser = []
    gooduser = []
    try:
        s = socket.socket()
        s.connect((ip,port))
        pass_list = util.load_password_dict(
            ip,
            userfile='database/mysql_user.txt', 
            passfile='database/mysql_pass.txt',
            mix=True,
            userlist=['postgres:postgres','postgres:root','postgres'],
            )
        
        for username,password in pass_list:
            if username in baduser:
                continue
            auth=getauth(s,username,password)
            if auth[0]=='noauth':
                security_hole("postgresql://%s:%d" % (ip,port))
                return
            if auth[0]=="md5":
                if sendauth(s,auth[1]):
                    security_hole("postgresql://%s:%s@%s:%d" % (username,password,ip,port))
                    s.close()
                    return
                else:
                    if username not in gooduser:
                        security_note("postgresql user: %s@%s:%d authtype:md5" % (username,ip,port))
                        gooduser.append(username)
            if auth[0]=='auth':
                if username not in gooduser:
                    security_note("postgresql user: %s@%s:%d authtype:%d" % (username,ip,port,auth[1]))
                    gooduser.append(username)
            if auth[0]=='baduser':
                baduser.append(username)
            s.close()
            s = createsocket(ip,port)
    except Exception,e:
        pass
        s.close()

if __name__ == '__main__':
    from dummy import *
    audit(assign('postgresql', ('192.168.0.132',5432))[1])



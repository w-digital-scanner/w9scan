#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-06-15 13:34:42
# @Author  : Medici.Yan (Medici.Yan@gmail.com)
# @Link    : http://blog.evalbug.com

import socket,struct
def validate(host,port,username,password):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(20)
        s.connect((host,port))
        payload1='\x05\x01\x02'#socks 5 版本1 02采用用户名密码验证
        s.send(payload1)
        data1=s.recv(1024)
        if data1!='\x05\x02': # Server response 05 02 use username/password validate 
            #Don't support user/pass authmethod
            s.close()
            return False
        #send validate data
        #version len(username) username len(password) password
        payload2=struct.pack('!BB'+str(len(username))+'sB'+str(len(password))+'s',1,len(username),username,len(password),password)
        s.send(payload2)
        data2=s.recv(1024)
        if data2 =='\x01\x00': #success
            #'username:%s\tPassword:%s---Success!'%(username,password)
            Flag=True
        else:
            #'username:%s\tPassword:%s\t---Auth Fail!'%(username,password)
            Flag=False
        s.close()
    except:
        #'validate host:%s with  %s/%s occurred some exception.'
        Flag=False
        if s:
            s.close()
    return Flag
def check(host,port):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(20)
        s.connect((host,port))
        payload1='\x05\x02\x00\x02'#socks 5 版本1 02采用用户名密码验证
        s.send(payload1)
        data1=s.recv(1024)
        if data1[0]!='\x05': # Server response 05 02 use username/password validate 
            #Don't support user/pass authmethod
            s.close()
            return False
        if data1[1]=='\x00':
            security_warning('socks5: %s:%s => NO AUTHENTICATION REQUIRED'%(host,str(port)))
            return False
        elif data1[1]=='\x02':
            return True
        else:
            return False
    except:
        if s:
            s.close()
        return False
def assign(service, arg):
    if service == 'socks5':
            return True, arg
def audit(arg):
    host,port = arg
    if check(host,port)==False:
        return
    pass_list = util.load_password_dict(host,userfile='database/ssh_user.txt',passfile='database/ssh_pass.txt')
    for useri,pwdj in pass_list:
        try:
            debug('Try %s/%s'%(useri,pwdj))
            ret=validate(host, int(port), useri, pwdj)
            if ret:
                security_warning('socks5 weak password=> %s:%s %s %s'%(host,str(port),useri,pwdj))
        except Exception, e:
            pass

if __name__ == '__main__':
    from dummy import *
    audit(assign('socks5', ('127.0.0.1',1080))[1])
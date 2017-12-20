#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
简单网络管理协议（SNMP）
通过community，相当于是密码来进行通信
如果是可读的community，则可以读取接口，vlan等信息
如果是可写的community。则可以直接读取配置文件，替换配置文件。也就是或是可以拿到最高权限了
在cisco交换，路由上测试通过
作者：半块西瓜皮
'''
import socket
def sendsnmp(ip,data):
    ret=''
    try:
        UDPClient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        UDPClient.settimeout(4)
        UDPClient.sendto(data, (ip,161))
        ret,addr = UDPClient.recvfrom(1024)
    except socket.error,msg:
        #connection reset by peer
        #port not open
        if msg.errno == 10054:
            return None
    finally:
        UDPClient.close()
    return ret


def makeget(password):
    data = '\x30'+chr(0x20+len(password))+'\x02\x01\x00\x04'+chr(len(password))+password+'\xA0\x19\x02\x01\x2B\x02\x01\x00\x02\x01\x00\x30\x0E\x30\x0C\x06\x08\x2B\x06\x01\x02\x01\x01\x04\x00\x05\x00'
    return data
def makeset(password,contact):
    data ='\x30'+chr(0x20+len(contact)+len(password))+'\x02\x01\x00\x04'+chr(len(password))+password+'\xA3'+chr(len(contact)+0x19)+'\x02\x01\x1B\x02\x01\x00\x02\x01\x00\x30'+chr(len(contact)+0xE)+'\x30'+chr(len(contact)+0xC)+'\x06\x08\x2B\x06\x01\x02\x01\x01\x04\x00\x04'+chr(len(contact))+contact
    return data

def testpassword(ip,password,contact='billy'):
    ret = sendsnmp(ip,makeget(password))
    if not ret:
        return (-1,'port not open')
    if(ret==''):
        return (0,'no response')
    original = ret[ret.rfind('\x04\x00\x04')+4:]
    ret = sendsnmp(ip,makeset(password,contact))
    if(ret.find('\x1b\x02\x01\x00\x02\x01\x00')==-1):
        return (1,'Read')
    sendsnmp(ip,makeset(password,original))
    return (2,'Read&Write')

def assign(service, arg):
    if service == "ip":
        return True, arg
def audit(ip):
    passwords = ['private','public','cisco','root','admin']
    for password in passwords:
        #debug('test snmp community %s',password)
        code,info = testpassword(ip,password)
        if code == -1:
            break
        if code == 2:
            security_hole('snmp community %s:%s' %(info,password))
            break
        if code == 1:
            security_warning('snmp community %s:%s' %(info,password))
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('ip', '192.168.0.1')[1])

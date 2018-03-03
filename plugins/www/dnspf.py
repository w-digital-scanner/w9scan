#!/usr/bin/env python
#coding:utf-8
"""

    Title:Dns spf default

    Description:query dns mx ,txt .

    Author:codier

    Blog:http://www.codier.cn

    Date:2015-08-03

    modify-end:2015-08-11

"""
import socket,struct,random

##    +---------------------+
##    |        Header       |
##    +---------------------+
##    |       Question      | the question for the name server
##    +---------------------+
##    |        Answer       | RRs answering the question
##    +---------------------+
##    |      Authority      | RRs pointing toward an authority
##    +---------------------+
##    |      Additional     | RRs holding additional information
##    +---------------------+
import urlparse
def get_url_host(url):
    host = util.get_domain_root(url)
    if ':' in host:
        host = host[:host.find(':')]
    return host

def assign(service, arg):
    if service == "www":
        return True, get_url_host(arg)
def audit(arg):
    dns = {
        "TID":0x2310,
        "Flags":0x0120,
        "Questions":0x0001,
        "AnswerRRs":0x0000,
        "AuthorityRRs":0x0000,
        "AdditionalRRS":0x0000,#header_end
        "Domain":dealDomain(arg),
        "SearchType":0x000f,
        "SearchClass":0x0001,
    }
    #common
    buff_head = struct.pack('!6H',dns["TID"],dns["Flags"],dns["Questions"],dns["AnswerRRs"],dns["AuthorityRRs"],dns["AdditionalRRS"])
    address = ('114.114.114.114',53)
    #gettargetmx
    if getDnsMx(buff_head,dns,address):
        if getDnsTxt(buff_head,dns,address):
            security_warning(arg)
#get domain mx record
def getDnsMx(buff_head,dns,address):
    buff_tail = struct.pack('!2H',dns["SearchType"],dns["SearchClass"])#type = 0x000f  =>mx
    mx_payload = buff_head + dns["Domain"] + buff_tail
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    for i in range(3):
        try:
            s.settimeout(10)
            s.sendto(mx_payload,address)
            st = s.recvfrom(1024)

            if st[0][6:8] > struct.pack('!H',0):
                return True
        except Exception :
            pass
        finally:
            s.close()
#format domain record
def dealDomain(url):
    buff = url.split('.')
    for index in range(len(buff)):
        buff[index] = struct.pack('!b',len(buff[index])) + buff[index]
    buff.append(struct.pack('!b',0))
    dns_format = ''.join(buff)
    return dns_format
#get domain txt record
def getDnsTxt(buff_head,dns,address):
    dns["SearchType"] = 0x0010
    buff_tail = struct.pack('!2H',dns["SearchType"],dns["SearchClass"])#type = 0x000f  =>mx
    mx_payload = buff_head + dns["Domain"] + buff_tail
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    for i in range(2):
        try:
            s.settimeout(5)
            s.sendto(mx_payload,address)
            st = s.recvfrom(1024)
            if st[0][6:8] == struct.pack('!H',0) or struct.pack('!5s','v=spf') not in st[0]:
                return True
        except Exception :
            pass
        finally:
            s.close()

if __name__ == '__main__':
    from dummy import *
    audit(assign('www','http://yunlai.cn:803/sfdsfds/')[1])
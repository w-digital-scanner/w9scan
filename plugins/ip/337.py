#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Medici.Yan'
#
import socket
import struct
def assign(service, arg):
	if service == "ip":
		return True, arg
def audit(arg):
	#pptp默认是1723端口，但是有些系统可能会修改端口
	for i in range(1720,1725):
		getPPTPVersion(arg, i)

def getPPTPVersion(host,port):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#start-control-connection-request
	'''Point-to-Point Tunnelling Protocol
		Length:156
		Message type:Ctrol Message(1)
		Magic Cookie: 0x1a2b3c4d (correct)
		Control Message Type: Start-Control-Connection-Request (1)
		Reserved: 0000
		Protocol version: 1.0
		Reserved: 0000
		Framing Capabilities: Asynchronous Framing supported (1)
		Bearer Capabilities: Analog access supported (1)
		Maximum Channels: 65535
		Firmware Revision: 1
		Host Name: none
		Vendor Name: medicean
	'''
	payload='\x00\x9c\x00\x01\x1a\x2b\x3c\x4d\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\xff\xff\x00\x01\x6e\x6f\x6e\x65\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x6d\x65\x64\x69\x63\x65\x61\x6e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
	try:
		socket.setdefaulttimeout(20)#超时
		s.connect((host,port))#连接对应主机和端口
		s.send(payload)
		data=s.recv(1024)
		length=data[0:2]		#pptp返回报文长度,156
		vendor=''
		if length == '\x00\x9c':
			FirmwareRevision=struct.unpack('i',data[27]+data[26]+'\x00\x00')	#data[26]，data[27]是版本，data[92:]是返回的操作系统名称
			for i in data[92:]:
				if i != '\x00':
					vendor+=i
			security_note(str(port)+'/tcp open pptp '+vendor+'(Firmware Revision '+str(FirmwareRevision[0])+')')
	except Exception :
		pass
	finally:
		s.close()

if __name__ == '__main__':
	from dummy import *
	audit(assign('ip', '202.202.111.159')[1])
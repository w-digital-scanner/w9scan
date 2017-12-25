#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Medici.Yan'
#Rsync弱口令检测
import socket,struct,hashlib,base64,time
def assign(service, arg):
	if service == "rsync" and len(arg)==2:
		return True, arg
def audit(arg):
	host=arg[0]
	port=arg[1]
	res=initialisation(host, port)
	if res[0]:
		#security_note("tcp/%s  rsync open Version:%s" % (port,res[2]))#这里有版本信息输出,合并到核心插件去了，就不显示了。
		if float(res[2])<30.0:#低版本的加密方式有所不一样,我暂时不想写了后面有时间再加上。
			return
		for i in range(len(res[3])-1):
			ClientCommand(host, port, res[3][i])

def initialisation(host,port):
	'''
		初始化并获得版本信息,每次会话前都要发送版本信息
	'''
	flag=False
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	rsync={"MagicHeader":"@RSYNCD:","HeaderVersion":" 30.0"}
	payload=struct.pack("!8s5ss",rsync["MagicHeader"],rsync["HeaderVersion"],"\n")#init
	try:
		socket.setdefaulttimeout(20)#超时
		s.connect((host,port))#连接对应主机和端口
		s.send(payload)
		data=s.recv(1024)
		reply=struct.unpack('!8s5ss',data)
		if len(reply)==3:
			flag=True	#端口开放
			rsynclist=ClientQuery(s)	#查询模块名
	except Exception :
		pass
	finally:
		s.close()
	if flag:
		return True,reply[0],reply[1],rsynclist
	return False,"port not open"

def ClientQuery(socket_pre):
	'''
		查询所有的模块名
		@return module name
	'''
	s=socket_pre
	payload=struct.pack("!s","\n")#query
	modulelist=[]
	try:
		s.send(payload)
		while True:
			data=s.recv(1024)#Module List lenth 17
			moduletemp=struct.unpack("!"+str(len(data))+"s",data)
			modulename=moduletemp[0].replace(" ","").split("\n")
			for i in range(len(modulename)):
				realname=modulename[i].split("\t")
				if realname[0] != "":
					modulelist.append(realname[0])
			if modulename[-2]=="@RSYNCD:EXIT":
				break
	except Exception :
		pass
	return modulelist

def ClientCommand(host,port,cmd):
	global userlist,pwdlist
	rsync={"MagicHeader":"@RSYNCD:","HeaderVersion":" 30.0"}
	payload1=struct.pack("!8s5ss",rsync["MagicHeader"],rsync["HeaderVersion"],"\n")
	payload2='%s\n'%cmd
	pass_list = util.load_password_dict(host,userfile='database/rsync_user.txt',passfile='database/ssh_pass.txt')
	for useri,pwdj in pass_list:
		try:
			user=useri
			password=pwdj
			#debug("try: %s,%s" %(useri,pwdj))
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((host,port))
			#step1 get version and init
			s.send(payload1)
			s.recv(1024)		#server initialisation
			#send cmd and generate the challenge code
			s.send(payload2)	#send client query
			data=s.recv(1024)	#data  @RSYNCD: AUTHREQD 9moobOy1VMjNAU/D4PB35g
			challenge=data[18:-1] #get challenge code
			#encrypt and generate the payload3  
			md=hashlib.md5()
			md.update(password)
			md.update(challenge)
			auth_send_data=base64.encodestring(md.digest())
			payload3="%s %s\n"%(user,auth_send_data[:-3])

			s.send(payload3)
			data3=s.recv(1024)#@RSYNCD: OK
			s.close()
			if 'OK' in data3: 
				if password=='':
					security_hole("Module:'%s' User/Password:%s/<empty>"%(cmd,user))
				else:
					security_hole("Module:'%s' User/Password:%s/%s"%(cmd,user,password))
				return
		except Exception, e:
			pass
		finally:
			s.close()
if __name__ == '__main__':
	from dummy import *
	audit(assign('rsync', ('172.18.19.90',873))[1])
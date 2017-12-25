#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-14 18:14:33
# @Author  : Medici.Yan (Medici.Yan@gmail.com)
# @Link    : http://mediciyan.tk

import socket,struct,time
def debugPacked(data):
	tmpstr=''
	for i in range(len(data)):
		tmpstr+=hex(ord(data[i]))+' '
		if i%4==3:
			tmpstr+='\n'
	print tmpstr

def GetPortCall(host,port,RPC_RPCVersion,RPC_Program,RPC_ProgramVersion,PM_Program,PM_Version):
	'''RPC Call'''
	RPC_XID=int(time.time())
	#RPC_XID=1428250246
	RPC_MessageType=0 # Call
	#RPC_RPCVersion=2
	#RPC_Program=100000 #portmap
	#RPC_ProgramVersion=2
	RPC_Procedure=3 # Get Port
	RPC_Credentials={"Flavor":0,"Length":0} #Flavor:AUTH_NULL
	RPC_Verifier={"Flavor":0,"Length":0}
	'''
	Portmap Getport Call
	'''
	#PM_Program=100005 # mount
	#PM_Version=3
	PM_Proto=6	# tcp
	PM_Port=0
	'''
	build the message
	'''
	payload=struct.pack("!LLLLLLLLLLLLLL",RPC_XID,RPC_MessageType,RPC_RPCVersion,RPC_Program,RPC_ProgramVersion,RPC_Procedure,RPC_Credentials['Flavor'],RPC_Credentials['Length'],RPC_Verifier['Flavor'],RPC_Verifier['Length'],PM_Program,PM_Version,PM_Proto,PM_Port)
	#debugPacked(payload)
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		socket.setdefaulttimeout(20)# set time out
		s.sendto(payload,(host,port))
		data=s.recvfrom(1024)
		#debugPacked(data[0])
		if data:
			recvupack=struct.unpack('!LLLLLLL',str(data[0]))
			nfs_port=recvupack[-1]
	except Exception, e:
		return False
	finally:
		s.close()
	if nfs_port:
		return nfs_port
	
def ExportCall(host,port,RPC_RPCVersion,RPC_Program,RPC_ProgramVersion):
	success=False
	name='testvul '# len(name) / 4 == 0
	MachineName={"length":len(name),'contents':name}

	FragmentHeader={'LastFragment':32768,'FragementLength':64+len(name)}
	RPC_XID=int(time.time())
	RPC_MessageType=0 # Call
	#RPC_RPCVersion=2
	#RPC_Program=100005 #MOUNT
	#RPC_ProgramVersion=3
	RPC_Procedure=5 # Export
	RPC_Credentials={"Flavor":1,"Length":24+len(name),'Stamp':int(time.time()),'MachineName':MachineName,'UID':0,'GID':0,'AuxiliaryGIDs1':1,'AuxiliaryGIDs2':0} #Flavor:AUTH_UNIX
	RPC_Verifier={"Flavor":0,"Length":0}
	payload=struct.pack("!HHLLLLLLLLLL"+str(len(name))+"sLLLLLL",FragmentHeader['LastFragment'],FragmentHeader['FragementLength'],RPC_XID,RPC_MessageType,RPC_RPCVersion,RPC_Program,RPC_ProgramVersion,RPC_Procedure,RPC_Credentials['Flavor'],RPC_Credentials['Length'],RPC_Credentials['Stamp'],RPC_Credentials['MachineName']['length'],RPC_Credentials['MachineName']['contents'],RPC_Credentials['UID'],RPC_Credentials['GID'],RPC_Credentials['AuxiliaryGIDs1'],RPC_Credentials['AuxiliaryGIDs2'],RPC_Verifier['Flavor'],RPC_Verifier['Length'])
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(20)
		s.connect((host,port))#连接对应主机和端口
		s.send(payload)
		data=s.recv(1024)
		if data:
			rpcrecv=struct.unpack("!HHLLLLLL",data[0:28])
			if rpcrecv[3]==1:#reply
				mountservice=data[28:]
				i=0
				count=0
				rep=[]
				while mountservice[i:i+4]!='\x00\x00\x00\x00':
					Directory_length=struct.unpack("!L",mountservice[i+4:i+8])[0] #(23,)
					Directory_contents=struct.unpack("!"+str(Directory_length)+"s",mountservice[i+8:i+8+Directory_length])[0]#('/var/www/html/nfs/test4',)
					#print "Directory:length:%s contents: %s"%(str(Directory_length),Directory_contents)
					i=i+8+Directory_length+4-(Directory_length%4)#fill bytes and move point

					Group_rep=[]
					while mountservice[i:i+4]!='\x00\x00\x00\x00':
						Group_length=struct.unpack("!L",mountservice[i+4:i+8])[0]
						Group_contents=struct.unpack("!"+str(Group_length)+"s",mountservice[i+8:i+8+Group_length])[0]
						#print "Group: length:%s, contents:%s"%(str(Group_length),Group_contents)
						i=i+8+Group_length+(4-Group_length%4)
						Group_rep.append(Group_contents)
					rep.append({"Directory":Directory_contents,"Groups":Group_rep})
					i=i+4
				if rep:
					for x in rep:
						temp=''
						for y in x['Groups']:
							temp+=y+' '
						security_warning("%s %s"%(x['Directory'],temp))
						success=True
	except Exception, e:
		pass
	finally:
		s.close()
		return success
def assign(service, arg):
	if service == "rpc":
		return True, arg

def audit(arg):
	RPC_RPCVersion=2
	RPC_Program=100000 #portmap
	#RPC_ProgramVersion=2
	PM_Program=100005   #Mountd 也就是NFS
	#PM_Version=3

	host=arg['host']
	
	rpcinfo=arg['rpcinfo']
	for i in range(len(rpcinfo)):
		if rpcinfo[i]['programname']=='rpcbind' and rpcinfo[i]['protocol']=='udp':
			port=rpcinfo[i]['port']
			if type(rpcinfo[i]['versions'])==str:
				rpc_versions=rpcinfo[i]['versions'].split(',')
			else:
				rpc_versions=list(str(rpcinfo[i]['versions']))

	mountd_versions=[]
	for i in range(len(rpcinfo)):
		if rpcinfo[i]['programnum']== PM_Program and rpcinfo[i]['protocol']=='tcp':
			if type(rpcinfo[i]['versions'])==int:
				mountd_versions.append(rpcinfo[i]['versions'])

	for RPC_ProgramVersion in rpc_versions:
		for PM_Version in mountd_versions:
			try:
				nfsport=GetPortCall(host, port,RPC_RPCVersion,RPC_Program,int(RPC_ProgramVersion),PM_Program,PM_Version)
				if nfsport !=False:
					success=ExportCall(host, nfsport,RPC_RPCVersion,PM_Program,PM_Version)
					if success:
						break
			except Exception, e:
				pass
if __name__ == '__main__':
	from dummy import *
	audit(assign('rpc', {'host': '172.18.19.90', 'rpcinfo': [{'versions': '2,3,4', 'protocol': 'tcp', 'programnum': 100000, 'programname': 'rpcbind', 'port': 111}, {'versions': '2,3,4', 'protocol': 'udp', 'programnum': 100000, 'programname': 'rpcbind', 'port': 111}, {'versions': '2,3,4', 'protocol': 'tcp', 'programnum': 100003, 'programname': 'nfs', 'port': 2049}, {'versions': '2,3,4', 'protocol': 'udp', 'programnum': 100003, 'programname': 'nfs', 'port': 2049}, {'versions': 2, 'protocol': 'tcp', 'programnum': 100005, 'programname': 'mountd', 'port': 45156}, {'versions': 3, 'protocol': 'tcp', 'programnum': 100005, 'programname': 'mountd', 'port': 49931}, {'versions': 1, 'protocol': 'tcp', 'programnum': 100005, 'programname': 'mountd', 'port': 53650}, {'versions': 2, 'protocol': 'udp', 'programnum': 100005, 'programname': 'mountd', 'port': 33925}, {'versions': 3, 'protocol': 'udp', 'programnum': 100005, 'programname': 'mountd', 'port': 49226}, {'versions': 1, 'protocol': 'udp', 'programnum': 100005, 'programname': 'mountd', 'port': 53492}, {'versions': '1,2', 'protocol': 'tcp', 'programnum': 100011, 'programname': 'rquotad', 'port': 875}, {'versions': '1,2', 'protocol': 'udp', 'programnum': 100011, 'programname': 'rquotad', 'port': 875}, {'versions': '1,3,4', 'protocol': 'tcp', 'programnum': 100021, 'programname': 'nlockmgr', 'port': 39414}, {'versions': '1,3,4', 'protocol': 'udp', 'programnum': 100021, 'programname': 'nlockmgr', 'port': 37443}, {'versions': '2,3', 'protocol': 'tcp', 'programnum': 100227, 'programname': 'nfs_acl', 'port': 2049}, {'versions': '2,3', 'protocol': 'udp', 'programnum': 100227, 'programname': 'nfs_acl', 'port': 2049}]})[1])

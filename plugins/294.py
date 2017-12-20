#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'ontheway'
import re
import urlparse

def assign(service, arg):
    if service == "www":
        url = urlparse.urlparse(arg).scheme + '://' + urlparse.urlparse(arg).netloc + urlparse.urlparse(arg).path
        query = urlparse.urlparse(arg).query
        arry = re.findall(r'&(.*?)=','&'+query)
        ret = []
        if arry:
            for i in range(0,len(arry)):
                ret.append(url + ' ' + arry[i])
            return True, arg ,ret
        return
    
def audit(arg):
    url = arg.replace('=','[]=')
    curl.curl(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://chen.dazupu.net.cn/indilist.php?ged=zh')[1])

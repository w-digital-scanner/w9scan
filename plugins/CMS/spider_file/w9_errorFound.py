#!/usr/bin/env python
#-*- coding:utf-8 -*-
# 只网址中的报错信息

from dummy import *
import re
import urlparse

def assign(service, arg):
    if service == 'spider_file':
        return True, arg

def audit(url,html):
    h = util.ErrorInfoSearch(html)
    if len(h) > 0:
        security_note("Found %s exist error message:%s"%(url,' '.join(h)),'Craw Found Error_message')
    arg = urlparse.urlparse(url).scheme + '://' + urlparse.urlparse(url).netloc + urlparse.urlparse(url).path
    query = urlparse.urlparse(url).query

    arry = re.findall(r'&(.*?)=', '&' + query)
    if arry:
        for item in arry:
            rets = arg + item
            rets = rets.replace('=', '[]=')
            code, head, html, redirect_url, log = hackhttp.http(rets)
            if code == 200:
                h = util.ErrorInfoSearch(html)
                if len(h) > 0:
                    security_note("Found %s exist error message:%s"%(rets,' '.join(h)),'Craw Found Error_message')

if __name__ == '__main__':
    print "1"
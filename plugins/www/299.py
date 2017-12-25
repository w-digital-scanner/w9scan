#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'ontheway'
import re
import urlparse
import md5

def assign(service, arg):
    if service == "www":
        host = urlparse.urlparse(arg).netloc
        arg = urlparse.urlparse(arg).scheme + "://" + host
        return True, arg ,host
    
def audit(arg):
    version = {'a57bd73e27be03a62dd6b3e1b537a72c':'4.0.0 - 4.2.3',
               '4b2c92409cf0bcf465d199e93a15ac3f':'4.3.0 - 4.3.10',
               '50caaf268b4f3d260d720a1a29c5fe21':'4.3.11 - 4.4.6; and 5.0.4 - 5.1.2',
               '85be3b4be7bfe839cbb3b4f2d30ff983':'5.0.0 - 5.0.3',
               '37e194b799d4aaff10e39c4e3b2679a2':'5.1.3 - 5.2.13',
               'fb3bbd9ccc4b3d9e0b3be89c5ff98a14':'5.3.0 - current'}
    url = arg + "/?=PHPE9568F36-D428-11d2-A769-00AA001ACF42"
    code, _, body, _, _ = curl.curl(url)
    if code == 200:
        ver_md5 = md5.md5(body).hexdigest()
        if version.get(ver_md5):
            security_note('php version:%s' % version[ver_md5])

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://www.example.com/')[1])

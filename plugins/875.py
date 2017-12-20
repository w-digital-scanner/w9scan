#!/usr/bin/env python
#author:yichin
#refer:http://lab.onsec.ru/2013/03/tomcat-servlet-examples-threats.html

import re
import urlparse

def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)


def audit(arg):
    url = arg + 'examples/servlets/servlet/SessionExample'
    code, head, res, errcode, _ = curl.curl('-A "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36" '+ url)
    if code == 200:
        m = re.search('<title>Sessions Example</title>', res)
        if m:
            security_warning(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://www.sms7.cn/')[1])
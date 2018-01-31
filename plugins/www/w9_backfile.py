#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# author:w8ay

import urlparse

# 12.#domain#.rar  代表当前扫描的域名 比如设置为 #domain#.rar 则实际扫描的是www.baidu.com.rar
# 13.#domain#.zip  代表当前扫描的域名 比如设置为 #domain#.rar 则实际扫描的是www.baidu.com.zip
# 14.#domainnopoint#.rar  代表当前扫描的域名，但是要去掉域名中的点“.” 比如 wwwbaiducom.rar
# 15.#domainnopoint#.zip  代表当前扫描的域名，但是要去掉域名中的点“.” 比如 wwwbaiducom.zip
# 16.#topdomain#.rar      代表当前扫描的域名取顶级域名比如 baidu.com.rar
# 17.#topdomain#.zip      代表当前扫描的域名取顶级域名比如 baidu.com.zip
# 18.#domaincenter#.rar   代表当前扫描的域名的中间部分 比如 baidu.rar
# 19.#domaincenter#.zip   代表当前扫描的域名的中间部分 比如 baidu.zip
# 20.#topdomainunderline#.rar 代表当前扫描的域名取顶级域名并去掉点加下划线 比如 www_baidu_com.rar - 低调求发展* k# T5 L9 E6 d( @/ [
# 21.#topdomainunderline#.zip 代表当前扫描的域名取顶级域名并去掉点加下划线 比如 www_baidu_com.zip; t; I6 q# q3 ~  ?
# 22.#underlinedomain#.rar    代表当前扫描的域名取顶级域名并去掉点加下划线 比如 baidu_com.rar
# 23.#underlinedomain#.zip    代表当前扫描的域名取顶级域名并去掉点加下划线 比如 baidu_com.zip

def assign(service, arg):
    if service == "www":
        return True,arg

def audit(arg):
    parse = urlparse.urlparse(arg)
    url = "%s://%s/"%(parse.scheme,parse.netloc)
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
            new = key.replace('.',"_")
            host_keys.append(new)
    for i in host_keys:
        new = "%s.rar"%(i)
        listFile.append(new)
        new = "%s.zip" % (i)
        listFile.append(new)
        new = "%s.tar.gz" % (i)
        listFile.append(new)
        new = "%s.tar" % (i)
        listFile.append(new)
    for payload in listFile:
        loads = url + payload
        code, head, html, redirect_url, log = hackhttp.http(loads)
        if code == 200 and 'Content-Type: application' in head:
            security_hole('可能的源代码泄露 URL:%s'%loads)

if __name__ == '__main__':
    from dummy import *
    audit("http://blog.hacking8.com/")

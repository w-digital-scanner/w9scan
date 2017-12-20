#!/usr/bin/env python
import re

def assign(service, arg):
    if service != "cmstop":
        return
    return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl(url + 'cmstop/apps/system/view/template/edit.php')
    if code == 200:
        m = re.search(' in <b>([^<]+)</b> on line <b>(\d+)</b>', res)
        if m:
            security_info(m.group(1))


if __name__ == '__main__':
    from __loader import *
    audit(assign('cmstop', 'http://www.haosax.com/')[1])

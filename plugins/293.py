#!/usr/bin/env python
import re

def assign(service, arg):
    if service == "ecshop":
        return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl(url + 'includes/fckeditor/editor/dialog/fck_spellerpages/spellerpages/server-scripts/spellchecker.php')
    if code == 200:
        m = re.search('in <b>([^<]+)</b> on line <b>(\d+)</b>', res)
        if m:
            security_info(m.group(1))

if __name__ == '__main__':
    from dummy import *
    audit(assign('ecshop', 'http://www.out521.com/shop/')[1])

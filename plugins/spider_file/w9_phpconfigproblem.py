#!/usr/bin/env python
#coding=utf8
#author:w8ay

import re
import urlparse

def assign(service, arg):
    if service == 'spider_file':
        return True, arg
        
def audit(url, body):
    match = re.search('/<td class="e">allow_url_fopen<\/td><td class="v">On<\/td>/',body)
    if match:
        security_note("phpinfo_allow_url_fopen " + url)

    match = re.search('/<td class="e">register_globals<\/td><td class="v">On<\/td>/',body)
    if match:
        security_note("phpinfo_register_globals " + url)
    
    match = re.search('/<td class="e">allow_url_include<\/td><td class="v">On<\/td>/',body)
    if match:
        security_note("phpinfo_allow_url_include " + url)

    match = re.search('/<td class="e">session.use_trans_sid<\/td><td class="v">1<\/td>/',body)
    if match:
        security_note("phpinfo_session_use_trans_sid " + url)

    match = re.search('/<td class="e">open_basedir<\/td><td class="v"><i>no value<\/i><\/td>/',body)
    if match:
        security_note("phpinfo_open_basedir " + url)

    match = re.search('/<td class="e">display_errors<\/td><td class="v">On<\/td>/',body)
    if match:
        security_note("phpinfo_display_errors " + url)
    
    match = re.search('/<td class="e">session\.use_only_cookies<\/td><td class="v">Off<\/td>/',body)
    if match:
        security_note("phpinfo_session_use_only_cookies " + url)

if __name__ == '__main__':
    # import local simulation environment
    from dummy import *
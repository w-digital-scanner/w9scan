#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urlparse

def assign(service, arg):
    if service == "www":
        r = urlparse.urlparse(arg)
        if r.path.endswith('.action') or r.path.endswith('.do'):
            return True, '%s://%s%s' % (r.scheme, r.netloc,r.path)

def audit(arg):
    task_push('struts',arg)

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://117.141.5.246:8800/oa/login/login!forwardFrameIndex.action')[1])
    audit(assign('www', 'http://www.dwhjz.com/index.do?a=3')[1])
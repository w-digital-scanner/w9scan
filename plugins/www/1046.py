#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#ref http://wooyun.org/bugs/wooyun-2015-0104880

import urlparse
def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/website-rank/getVoteRecordByManuscriptId.action' % (arr.scheme, arr.netloc)

def audit(arg):
    task_push('struts',arg)
                        

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://www.example.com:88/')[1])
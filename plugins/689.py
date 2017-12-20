#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urlparse
def assign(service, arg):
    if service != "www": 
        return
    r = urlparse.urlparse(arg)
    paths = r.path.split('/')
    n = len(paths)
    ret = []
    if n < 3:
        return True, '%s://%s/' % (r.scheme, r.netloc)
    elif n <= 5:
        # return recrusive directory list
        for i in range(1, n - 1):
            ret.append('%s://%s/%s/' % (r.scheme, r.netloc, '/'.join(paths[1:i+1])))
    return True, ret
def audit(arg):
    payloads = [
    'database/PowerEasy4.mdb',
    'database/PowerEasy5.mdb',
    'database/PowerEasy6.mdb',
    'database/PowerEasy2005.mdb',
    'database/PowerEasy2006.mdb',
    'database/PE_Region.mdb',
    'data/dvbbs7.mdb',
    'databackup/dvbbs7.mdb',
    'bbs/databackup/dvbbs7.mdb',
    'data/zm_marry.asp',
    'databackup/dvbbs7.mdb',
    'admin/data/qcdn_news.mdb',
    'firend.mdb',
    'database/newcloud6.mdb',
    'database/%23newasp.mdb',
    'blogdata/L-BLOG.mdb',
    'blog/blogdata/L-BLOG.mdb',
    'database/bbsxp.mdb',
    'bbs/database/bbsxp.mdb',
    'access/sf2.mdb',
    'data/Leadbbs.mdb',
    'bbs/Data/LeadBBS.mdb',
    'bbs/access/sf2.mdb',
    'fdnews.asp',
    'bbs/fdnews.asp',
    'admin/ydxzdate.asa',
    'data/down.mdb',
    'data/db1.mdb',
    'database/Database.mdb',
    'db/xzjddown.mdb',
    'admin/data/user.asp',
    'data_jk/joekoe_data.asp',
    'data/news3000.asp',
    'data/appoen.mdb',
    'data/12912.asp',
    'database.asp',
    'download.mdb',
    'dxxobbs/mdb/dxxobbs.mdb',
    'db/6k.asp',
    'database/snowboy.mdb',
    'database/%23mmdata.mdb',
    'editor/db/ewebeditor.mdbeWebEditor/db/ewebeditor.mdb',
    ]
    for payload in payloads:
        url = arg + payload
        code, head, body, error, _ = curl.curl('--max-filesize 1024000 '+url)
        if code == 200 and 'Standard Jet DB' in body:
            security_hole(url)
            break


if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://127.0.0.1/a/a/1.asp')[1])
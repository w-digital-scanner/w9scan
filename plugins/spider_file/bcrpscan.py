#!/usr/bin/env python
#-*- coding:utf-8 -*-
#From:https://github.com/secfree/bcrpscan/blob/master/py_unittest.py

import urlparse
import hashlib

DIR_PROBE_EXTS = ['.tar.gz', '.zip', '.rar', '.tar.bz2']
FILE_PROBE_EXTS = ['.bak', '.swp', '.1']
NOT_EXIST = hashlib.md5("not_exist").hexdigest()[8:16]


def assign(service, arg):
    if service == 'spider_file':
        return True, arg

def audit(url,html):
    probe_url(url)


def probe_url(url):
    """
    Scan web path based on an url.

    :param url: url
    :type url: str
    """
    if not url or not url.startswith('http'):
        return
    if url.count('/') == 2:
        url = '%s/' % url

    pr = urlparse.urlparse(url)
    paths = get_parent_paths(pr.path)
    for p in paths:
        if p == "/":
            continue
        if p[-1] == '/':
            for ext in DIR_PROBE_EXTS:
                u = '%s://%s%s%s' % (pr.scheme, pr.netloc, p[:-1], ext)
                code, head, body, redirect, log = hackhttp.http(u)
                if code == 200:
                    security_note(u,'bcrpscan')
        else:
            for ext in FILE_PROBE_EXTS:
                u = '%s://%s%s%s' % (pr.scheme, pr.netloc, p, ext)
                code, head, body, redirect, log = hackhttp.http(u)
                if code == 200:
                    security_note(u,'bcrpscan')


def get_parent_paths(path):
    '''
    Get a path's parent paths.

    :param path: path
    :type path: str

    :rparam: parent paths
    :rtype: list
    '''
    paths = []
    if not path or path[0] != '/':
        return paths
    paths.append(path)
    tph = path
    if path[-1] == '/':
        tph = path[:-1]
    while tph:
        tph = tph[:tph.rfind('/') + 1]
        paths.append(tph)
        tph = tph[:-1]
    return paths


if __name__ == '__main__':
    from dummy import *
    audit("https://github.com/secfree/bcrpscan/blob/master/bcrpscan.py","")


    '''
    https: // github.com / secfree / bcrpscan / blob / master / bcrpscan.py.bak
    https: // github.com / secfree / bcrpscan / blob / master / bcrpscan.py.swp
    https: // github.com / secfree / bcrpscan / blob / master / bcrpscan.py
    .1
    https: // github.com / secfree / bcrpscan / blob / master.tar.gz
    https: // github.com / secfree / bcrpscan / blob / master.zip
    https: // github.com / secfree / bcrpscan / blob / master.rar
    https: // github.com / secfree / bcrpscan / blob / master.tar.bz2
    https: // github.com / secfree / bcrpscan / blob.tar.gz
    https: // github.com / secfree / bcrpscan / blob.zip
    https: // github.com / secfree / bcrpscan / blob.rar
    https: // github.com / secfree / bcrpscan / blob.tar.bz2
    https: // github.com / secfree / bcrpscan.tar.gz
    https: // github.com / secfree / bcrpscan.zip
    https: // github.com / secfree / bcrpscan.rar
    https: // github.com / secfree / bcrpscan.tar.bz2
    https: // github.com / secfree.tar.gz
    https: // github.com / secfree.zip
    https: // github.com / secfree.rar
    https: // github.com / secfree.tar.bz2
    '''
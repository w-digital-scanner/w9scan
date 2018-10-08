#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: w8ay
# @Date:   2017年12月20日 20:39:06

import re,urlparse
from lib.utils.cmsdata import cms_dict
import hashlib

def getMD5(password):
    m = hashlib.md5()
    m.update(password)
    return m.hexdigest()

def makeurl(url):
    prox = "http://"
    if(url.startswith("https://")):
        prox = "https://"
    url_info = urlparse.urlparse(url)
    url = prox + url_info.netloc + "/"

    return url

def isMatching(f_path, cms_name, sign, res, code, host, head):
    isMatch = False
    if f_path.endswith(".gif"):
        if sign:
            isMatch = getMD5(res) == sign
        else:
            isMatch = res.startswith("GIF89a")

    elif f_path.endswith(".png"):
        if sign:
            isMatch = getMD5(res) == sign
        else:
            isMatch = res.startswith("\x89PNG\x0d\x0a\x1a\x0a")

    elif f_path.endswith(".jpg"):
        if sign:
            isMatch = getMD5(res) == sign
        else:
            isMatch = res.startswith("\xff\xd8\xff\xe0\x00\x10JFIF")

    elif f_path.endswith(".ico"):
        if sign:
            isMatch = getMD5(res) == sign
        else:
            isMatch = res.startswith("\x00\x00\x00")

    elif code == 200:
        if sign and res.find(sign) != -1 or head.find(sign) != -1:
            isMatch = True

    elif sign and head.find(sign) != -1:
        isMatch = True

    if isMatch:
        task_push(cms_name, host, target=util.get_url_host(host))
        security_note(cms_name,'whatcms')
        #print "%s %s" % (cms_name, host)
        return True

    return False

def assign(service, arg):
    if service == "www":
        return True,makeurl(arg)

def audit(arg):
    cms_cache = {}
    cache = {}

    def _cache(url):
        if url in cache:
            return cache[url]
        else:
            status_code, header, html_body, error, error = curl.curl2(url)

            if status_code != 200 or not html_body:
                html_body = ""

            cache[url] = (status_code, header, html_body)
            return status_code, header, html_body

    for cmsname in cms_dict:
        cms_hash_list = cms_dict[cmsname]

        for cms_hash in cms_hash_list:
            if isinstance(cms_hash, tuple):
                f_path, sign = cms_hash
            else:
                f_path, sign = cms_hash, None

            if not isinstance(f_path, list):
                f_path = [f_path]

            for file_path in f_path:
                if file_path not in cms_cache:
                    cms_cache[file_path] = []
                cms_cache[file_path].append((cmsname, sign))

    cms_key = cms_cache.keys()
    cms_key.sort(key=len)

    isMatch = False

    for f_path in cms_key:
        if isMatch:
            break
        for cms_name, sign in cms_cache[f_path]:
            code, head, res = _cache(arg + f_path)
            isMatch =isMatching(f_path, cms_name, sign, res, code, arg, head)
            if isMatch:
                break

if __name__ == '__main__':
    #print assign("www","https://blog.hacking8.com/sagasg/zxc.php?asdzxc")
    audit("https://www.t00ls.net/")
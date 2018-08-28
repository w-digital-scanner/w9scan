#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# Embedded file name: struts.py
import urlparse
import re


def assign(service, arg):
    if service == "www":
        return True, arg


def _get_new_urls(page_url, links):
    new_urls = set()
    for link in links:
        new_url = link
        new_full_url = urlparse.urljoin(page_url, new_url)
        OO0o = urlparse.urlparse(new_full_url)
        if OO0o.path.endswith(".action") or OO0o.path.endswith(".do"):
            new_urls.add(new_full_url)
    return new_urls


def audit(arg):
    # task_push('struts',arg)
    code, head, html, redirect_url, log = hackhttp.http(arg)

    webreg = re.compile('''<a[^>]+href=["\'](.*?)["\']''', re.IGNORECASE)
    urls = webreg.findall(html)
    struts_urls = _get_new_urls(arg, urls)
    if struts_urls:
        security_info("struts框架")
    for struts_url in struts_urls:
        task_push('struts', struts_url)


if __name__ == '__main__':
    from dummy import *

    # KEY---9a176f89756545161a807d6b5803333756eccaaad7ea2daa4e5eeb6c37a09ec0---

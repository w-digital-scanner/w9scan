#!/usr/bin/env python
# -*- coding: utf-8 -*-
# DedeCms data/mysql_error_trace.inc 敏感信息泄露

def assign(service, arg):
    if service == "dedecms":
        return True, arg

def audit(arg):
    url = arg + 'data/mysql_error_trace.inc'
    _, _, body, _, _ = curl.curl(url)
    if body and body.find('<?php  exit();') != -1:
        security_note(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('dedecms', 'http://www.9ifd.com/')[1])

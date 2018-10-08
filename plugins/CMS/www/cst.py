#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from re import search,I


def assign(service, arg):
    if service != "www":
        return
    return True, arg

def audit(arg):
    # headers 
    headers = {'Fuck':'hello_word'}
    # send request 
    try:
        code, head, body, redirect, log = hackhttp.http(arg, headers=headers)
    except:
        return False
    # 
    regexp = r"hello_word"
    if 'Fuck' in head or 'fuck' in head:
        if search(regexp,head,I):
            security_note('This site is vulnerabile to Cross Site Tracing (XST) at: %s'%(arg))

if __name__ == "__main__":
    from dummy import *
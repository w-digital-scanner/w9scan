#!/usr/bin/env python
# -*- coding: utf-8 -*-
# package for test

from thirdparty import miniCurl
from thirdparty import ThreadPool

def security_hole(msg):
    print msg

def security_info(msg):
    print msg
    
ThreadPool = ThreadPool.ThreadPool
curl = miniCurl.Curl()
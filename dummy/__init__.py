#!/usr/bin/env python
# -*- coding: utf-8 -*-
# package for test

from thirdparty import miniCurl
from thirdparty import ThreadPool
from thirdparty import hackhttp
from lib.utils import until

def security_hole(msg):
    print msg

def security_info(msg):
    print msg
    
ThreadPool = ThreadPool.w8_threadpool
curl = miniCurl.Curl()
hackhttp = hackhttp.hackhttp()
util = until
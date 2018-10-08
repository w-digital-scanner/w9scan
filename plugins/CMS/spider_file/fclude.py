#!/usr/bin/env python
#-*- coding:utf-8 -*-
import urlparse

class LRFI:

    def __init__(self, url):
        self.url = url
        self.p = urlparse.urlparse(url)
    
    def _checkVaild(self):
        for param in self.p.query.split("&"):
            try:
                key,value = param.split("=")
            except:
                continue
            if key == ("key" or "filename") or "." in value:
                return True
        return False

    def rfi(self):
        check_url = "http://www.baidu.com"
        check_html = "<!--STATUS OK-->"

        for param in self.p.query.split("&"):
            key,value = param.split("=")
            if key == ("key" or "filename") or "." in value:
                new_url = self.url.replace("%s=%s"%(key,value),"%s=%s"%(key,check_url))
                code, head, body, redirect, log = hackhttp.http(new_url)
                if code == 200 and check_html in body:
                    security_hole(new_url,'file_include')
    
    def lfi(self):
        flagText = "w9scan niube!"
        for param in self.p.query.split("&"):
            key,value = param.split("=")
            if key == ("key" or "filename") or "." in value:
                new_url = self.url.replace("%s=%s"%(key,value),"%s=%s"%(key,"php://input"))
                code, head, body, redirect, log = hackhttp.http(new_url,post=flagText)

                if code == 200 and flagText in body:
                    security_hole(new_url,'file_include')


def assign(service, arg):
    if service == 'spider_file':
        return True, arg

def audit(url,html):
    lf = LRFI(url)
    if lf._checkVaild():
        lf.rfi()
        lf.lfi()    
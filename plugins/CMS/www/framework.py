#!/usr/bin/env python
# coding:utf-8
import urlparse
from re import search,I

class frame():

    def __init__(self,arg,header,html):
        self.url = arg
        self.header = header
        self.html = html

    def cakephp(self):
        _ = False
        _ |= search("CAKEPHP=",self.header) is not None
        if _ : security_note("CakePHP - PHP Framework","Framework")
    
    def cherrypy(self):
        _ = False
        _ |= search("CherryPy",self.header) is not None
        if _ : security_note("CherryPy - Python Framework","Framework")
    
    def codeigniter(self):
        _ = False
        _ |= search("ci_session=",self.header) is not None
        if _ : security_note("CodeIgniter - PHP Framework","Framework")
    
    def django(self):
        _ = False
        _ |= search("wsgiserver/",self.header) is not None
        _ |= search("python/",self.header) is not None
        _ |= search("csrftoken=",self.header) is not None
        _ |= search(r"\<meta name\=\"robots\" content\=\"NONE,NOARCHIVE\"\>\<title\>Welcome to Django\<\/title\>",self.html) is not None 
        if _ : security_note("Django - Python Framework","Framework")

    def drupal(self):
        _  = False
        if 'set-cookie' in self.header:
            _ |= search(r"SESS[a-z0-9]{32}=[a-z0-9]{32}",self.header,I) is not None
        if 'x-drupal-cache' in self.header:_ |= True
        _ |= search(r"\<script type\=\"text\/javascript\" src\=\"[^\"]*\/misc\/drupal.js[^\"]*\"\>\<\/script\>",self.html) is not None
        _ |= search(r"<[^>]+alt\=\"Powered by Drupal, an open source content management system\"",self.html) is not None
        _ |= search(r"@import \"[^\"]*\/misc\/drupal.css\"",self.html) is not None
        _ |= search(r"jQuery.extend\(drupal\.S*",self.html) is not None
        _ |= search(r"Drupal.extend\(\S*",self.html) is not None
        if _ : security_note("Drupal","Framework")

    def flask(self):
        _ = False
        _ |= search("flask",self.header) is not None
        if _ : security_note("Flask - Python Framework","Framework")
    
    def larvel(self):
        _ = False
        _ |= search("laravel_session=",self.header) is not None
        if _ : security_note("Larvel - PHP Framework","Framework")

    def web2py(self):
        _ = False
        _ |= search("web2py",self.header) is not None
        _ |= search(r"\<div id\=\"serendipityLeftSideBar\"\>",self.html) is not None
        if _ : security_note("Web2Py - Python Framework","Framework")
    
    def yii(self):
        _ = False
        _ |= search(r"\<a href\=\"http://www.yiiframework.com/\" rel\=\"external\"\>Yii Framework\<\/a\>",self.html) is not None
        _ |= search(r"\>Yii Framework\<\/a\>",self.html) is not None
        if _ : security_note("Yii - PHP Framework","Framework")
    
    def zend(self):
        _ = False
        _ |= search("zend",self.header) is not None
        _ |= search(r"\<meta name\=\"generator\" content\=\"Zend.com CMS ([\d\.]+)\"",self.html) is not None
        _ |= search(r"<meta name\=\"vendor\" content\=\"Zend Technologies",self.html) is not None 
        _ |= search(r"\"Powered by Zend Framework\"",self.html) is not None
        _ |= search(r" alt\=\"Powered by Zend Framework!\" \/\>",self.html) is not None
        if _ : security_note("Zend - PHP Framework","Framework")

def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    try:
        code, head, html, redirect_url, log = hackhttp.http(arg)
    except:
        return False
    f = frame(arg,head,html)
    f.cakephp()
    f.cherrypy()
    f.codeigniter()
    f.django()
    f.drupal()
    f.flask()
    f.larvel()
    f.web2py()
    f.zend()



if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://codier.cn/')[1])
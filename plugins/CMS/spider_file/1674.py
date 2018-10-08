#!/usr/bin/env python
#coding=utf8
import re
import urlparse

'''
Only one function named 'audit', the function is automatically called during the spider crawling
    url     : the URL of current page
    head    : HTTP Response header
    body    : HTTP Body
'''
def assign(service, arg):
    if service == 'spider_file':
        return True, arg
        
def audit(url, body):

    asmxs = re.findall(r'<script src="([^.]+.asmx)', body)
    arr = urlparse.urlparse(url)
    mainurl = '%s://%s' % (arr.scheme, arr.netloc)

    for asmx in asmxs:
        security_note(mainurl+asmx)

if __name__ == '__main__':
    # import local simulation environment
    from dummy import *
    audit('http://www.snxrsj.gov.cn/admin/login.aspx','','''
<script src="/ScriptResource.axd?d=-tEFDvFQHJ02D84x6r6qlOpdhvC8b5kMSGWTkX3E7v-hF2SrPCccMtZVjKt52FyZk9grfiToBQhTVmTR9O-LkdFhdiIFmr6wqSYmVQDOtf9xnMd9_T95mKyR-H1O5GKc2VAqClxZVsb9T83H2YkjpWrgOqJlmiIB72U6G_sA24Ls3nn-0&amp;t=635640826123593750" type="text/javascript"></script>
<script src="/WebService/UserLogin.asmx/jsdebug" type="text/javascript"></script>

''')
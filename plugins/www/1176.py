#!/usr/bin/env python
# coding:utf-8
"""
    Title:Script language recognition
    Description:Automatic identification of PHP, ASP,JSP, ASPX, HTML
    Author:codier
    Blog:http://www.codier.cn
    Date:2015-07-25
"""
import re
import urlparse
#识别脚本语言
def getScript(url):
    app_suffix = []
    signature_buff = ['php','asp.net']
    session_buff = ['aspsessionid-asp','jsessionid-jsp','phpsessid-php','asp.net_sessionid-aspx']
    web_suffix = ['php','asp','aspx','jsp']
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200:
        m = re.search('X-Powered-By: (.*?)[\r|\n]+', head,flags=re.S)
        if m:
            buff = m.group(1).lower()
            for index in signature_buff:
                if index in buff:
                    app_suffix.append(index)
                    
        m = re.search('Set-Cookie: (.*?)=', head,flags=re.S)
        if m:
            buff = m.group(1).lower()
            for index in session_buff:
                if (index[:index.find('-')] in buff) and (index[index.find('-')+1:] not in app_suffix):
                    app_suffix.append(index[index.find('-')+1:])

        m = re.findall(r'href=(?:"|\'|\s)*[/\w]*\.(jsp|php|aspx|asp)',res,re.I)
        if m:
            max_buff = 'asp'
            for index in web_suffix:
                if m.count(index) > m.count(max_buff):
                    max_buff = index
            if max_buff not in app_suffix:
                app_suffix.append(max_buff)


        if 'asp' in app_suffix or 'aspx' in app_suffix :
            if 'asp.net' in app_suffix:app_suffix.remove('asp.net')
        if len(app_suffix) == 0:app_suffix.append('html')
    return app_suffix

def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    app_suffix = getScript(arg)
    if len(app_suffix) != 0:
        security_note(arg + str(app_suffix))

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://codier.cn/')[1])
    #audit(assign('discuz', 'http://127.0.0.1/')[1])
    #audit(assign('discuz', 'http://www.szidk.net/')[1])
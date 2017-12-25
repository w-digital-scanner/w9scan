#!/usr/bin/evn python
import socket
import urlparse

def assign(service, arg):
    if service == 'www':
        url_info = urlparse.urlparse(arg)
        hostname = socket.gethostbyname(url_info.netloc)
        return True, hostname

def audit(arg):
    security_info("IP:" + arg)
    task_push("ip",arg)

if __name__ == "__main__":
    print assign("www","https://blog.hacking8.com")

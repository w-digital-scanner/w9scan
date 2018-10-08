# Embedded file name: iisput.py
import re
import urlparse
import socket


def assign(service, arg):
    if service == "www":
        url_info = urlparse.urlparse(arg)
        return True, '%s://%s/alert.txt' % (url_info.scheme, url_info.netloc)


def audit(arg):
    data = '''There are some secure problems in you system, please fix it.'''
    # code, head, body, errcode, final_url
    code, head, body, errcode, final_url = curl.curl('-T -d "%s" %s' % (data, arg))
    if code == 200 or code == 201:
        for i in range(2):
            code, final_url, body, final_url, final_url = curl.curl(arg)
            if body.find(data) != -1:
                security_hole(arg)
                break
            url_info = urlparse.urlparse(arg)
            hostname = socket.gethostbyname(url_info.hostname)
            if not hostname:
                break
            arg = "%s://%s%s%s" % (url_info.scheme, hostname,
                                   ":%d" % url_info.port if url_info.port else "",
                                   url_info.path)
            security_warning("%s %s" % ("iisput", arg))


if __name__ == '__main__':
    from dummy import *

    # KEY---3f9632f701953df91e7b13b428d18ab7a549520831cc2a46984c83e81b933673---

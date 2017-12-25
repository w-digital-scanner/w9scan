# Embedded file name: dotnet.py
import re
import urlparse

def assign(service, arg):
    if service == "www":
        url_info = urlparse.urlparse(arg)
        return (True, "%s://%s/~.aspx" % (url_info.scheme, url_info.netloc))


def audit(arg):
    url = arg
    status_code, header, body, errcode, _ = curl.curl(url)

    if status_code == 404:
        if re.search("[A-Z]:[\/]", body, re.M):
            security_warning(url)

        regex_ = re.search("Microsoft .NET Framework [^:\n]+:[\d\.]+;[^\r\n<]+", body, re.M | re.I)
        if regex_:
            security_note(".Net Version:" + regex_.group(0))


if __name__ == '__main__':
    from dummy import *

    exit()

# KEY---e0a46b005bc3e4b63bf33f9097023d87614810c0b71a355e0934a7bc8a862f32---

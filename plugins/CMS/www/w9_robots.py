# Embedded file name: robots.py
import re
import urlparse


def assign(service, arg):
    if service == "www":
        url_info = urlparse.urlparse(arg)
        return True, '''%s://%s/robots.txt''' % (url_info.scheme, url_info.netloc)


def audit(arg):
    arg = arg
    # code, head, body, ecode, redirect_url
    code, head, body, errorcode, redirect_url = curl.curl(arg)
    if code == 200:
        if re.search("Content\-Type:\s+[^\n]*text[^\n]+", head, re.M) and body.find('''<''') == -1:
            regex_data = ""
            for re_data in re.finditer("[^\r\n]+(admin|manage)[^\r\n]+", body, re.M | re.I):
                regex_data += re_data.group(0)

            regex_data = regex_data.strip()
            if regex_data:
                security_note(arg + " : " + regex_data)


if __name__ == '__main__':
    from dummy import *

    audit(assign("www", "http://ver007.com/")[1])
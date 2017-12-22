# Embedded file name: url_redirect.py
import re
import urlparse
import urllib
import time


def assign(service, arg):
    if service != "www":
        return
    OO0o = urlparse.urlparse(arg)
    Oo0Ooo = urlparse.parse_qsl(OO0o.query)
    for O0O0OO0O0O0, iiiii in Oo0Ooo:
        arg = arg.replace(iiiii, O0O0OO0O0O0)

    if urlparse.urlparse(arg).query.find('''=''') == -1 or len(Oo0Ooo) > 6:
        return
    else:
        return True, arg


def iI1(action, query, k, v):
    i1I11i = []
    OoOoOO00 = "http://www.gov.cn/?" + str(time.time())
    for I11i, O0O in query:
        O0O = OoOoOO00 if I11i == k else O0O
        i1I11i.append((I11i, O0O))

    iI111iI = urllib.urlencode(i1I11i)
    IiII = "%s?%s" % (action, iI111iI)
    iI1Ii11111iIi, i1i1II, O0oo0OO0, I1i1iiI1, I1i1iiI1 = curl.curl(IiII)
    if i1i1II.find("Location: http://www.gov.cn/") != -1:
        return True, "%s?%s" % (action, iI111iI)


def audit(arg):
    Ii1iI = arg
    Oo = urlparse.urlparse(Ii1iI)
    I1Ii11I1Ii1i = urlparse.urlunsplit((Oo.scheme, Oo.netloc, Oo.path, "", ""))
    Oo0Ooo = urlparse.parse_qsl(Oo.query)
    oo = ["__VIEWSTATE", "IbtnEnter.x", "IbtnEnter.y"]
    for O0O0OO0O0O0, iiiii in Oo0Ooo:
        if O0O0OO0O0O0 in oo:
            continue
        debug("[RDB] %s %s-", O0O0OO0O0O0, I1Ii11I1Ii1i)
        IiII1I1i1i1ii = iI1(I1Ii11I1Ii1i, Oo0Ooo, O0O0OO0O0O0, iiiii)
        if IiII1I1i1i1ii:
            security_info(IiII1I1i1i1ii[1])
            return


if __name__ == '__main__':
    from dummy import *

    # KEY---efb1fdfd9905e92bacd3a5367c4727dc7ae722ab7f214e1434b6e25041d34190---

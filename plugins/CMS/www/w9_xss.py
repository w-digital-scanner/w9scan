# Embedded file name: xss.py

import re
import urlparse
import urllib


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
        return (True, arg)


def iI1(method, action, query, k, v):
    i1I11i = ["""-->'"><H1>XSS@HERE</H1>"""]
    for OoOoOO00 in i1I11i:
        I11i = []
        for O0O, Oo in query:
            Oo = OoOoOO00 if O0O == k else Oo
            I11i.append((O0O, Oo))

        IiII = urllib.urlencode(I11i)
        iI1Ii11111iIi = None
        if method == "GET":
            iI1Ii11111iIi = "%s?%s" % (action, IiII)
        elif method == "POST":
            iI1Ii11111iIi = '-d "%s" %s' % (IiII, action)
        else:
            return False
        i1i1II, O0oo0OO0, I1i1iiI1, iiIIIII1i1iI, iiIIIII1i1iI = curl.curl("-L " + iI1Ii11111iIi)
        if I1i1iiI1.find("<H1>XSS@HERE") != -1 and I1i1iiI1.find('\\"><H1>XSS') == -1:
            return (True, '%s?%s' % (action, IiII))


def audit(arg):

    ooO0oooOoO0 = arg
    II11i = urlparse.urlparse(ooO0oooOoO0)
    i1oOOoo00O0O = urlparse.urlunsplit((II11i.scheme, II11i.netloc, II11i.path, "", ""))
    Oo0Ooo = urlparse.parse_qsl(II11i.query)

    i1111 = ['__VIEWSTATE', 'IbtnEnter.x', 'IbtnEnter.y']
    i11 = ["GET", "POST"]

    for I11 in i11:

        for O0O0OO0O0O0, iiiii in Oo0Ooo:
            if O0O0OO0O0O0 in i1111:
                continue

            debug('[XSS] <%s> %s %s', I11, O0O0OO0O0O0, i1oOOoo00O0O)
            Oo0o0000o0o0 = iI1(I11, i1oOOoo00O0O, Oo0Ooo, O0O0OO0O0O0, iiiii)

            if Oo0o0000o0o0:
                security_info('<%s> %s' % (I11, Oo0o0000o0o0[1]))
                return


if __name__ == '__main__':
    pass


    # KEY---6eaf26b1043248ae94ca258db5d5b068a610a213aa1d2af703532163d0bd1717---

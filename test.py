# coding:utf-8

import urlparse

u = "http://testphp.vulnweb.com/listproducts.php?artist=1&asfss=www"
parse = urlparse.urlparse(u)
print parse
if not parse.query:
    pass




for i in parse.query.split('&'):
    k,v = i.split('=')
    print k,is_number(v)

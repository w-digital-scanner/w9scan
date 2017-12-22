from thirdparty import hackhttp
hh = hackhttp.hackhttp()
url = "http://www.adfun.cn/"
code, head, html, redirect_url, log = hh.http(url) #code, head, html, redirect_url, log = hh.http(url)
print code, head, html, redirect_url, log
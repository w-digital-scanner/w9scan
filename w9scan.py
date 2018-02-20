#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: w8ay
# @Date:   2017年12月17日 19:21:35

import sys

sys.dont_write_bytecode = True  # 不生成pyc文件
try:
    __import__("lib.utils.versioncheck")  # this has to be the first non-standard import
except ImportError:
    exit("[!] wrong installation detected (missing modules). Please install python version for 2.7.x")

from lib.core.common import weAreFrozen
from lib.core.common import getUnicode
from lib.core.common import setPaths
from lib.core.common import makeurl
from lib.core.common import banner
from lib.core.common import Get_lineNumber_fileName
from lib.core.log import logger
import os
import inspect,time
from distutils.version import LooseVersion
from lib.core.settings import VERSION
from lib.core.settings import LIST_PLUGINS
from lib.core.data import urlconfig
from lib.core.exploit import Exploit_run
from lib.utils import crawler
from lib.core.common import createIssueForBlog
from lib.core.update import updateProgram
import argparse,multiprocessing

def modulePath():
    """
    This will get us the program's directory, even if we are frozen
    using py2exe
    """

    try:
        _ = sys.executable if weAreFrozen() else __file__
    except NameError:
        _ = inspect.getsourcefile(modulePath)

    return getUnicode(os.path.dirname(os.path.realpath(_)), encoding=sys.getfilesystemencoding())

def checkEnvironment():
    try:
        os.path.isdir(modulePath())
    except UnicodeEncodeError:
        errMsg = "your system does not properly handle non-ASCII paths. "
        errMsg += "Please move the w9scan's directory to the other location"
        logger.critical(errMsg)
        raise SystemExit

    if LooseVersion(VERSION) < LooseVersion("1.0"):
        errMsg = "your runtime environment (e.g. PYTHONPATH) is "
        errMsg += "broken. Please make sure that you are not running "
        errMsg += "newer versions of w9scan with runtime scripts for older "
        errMsg += "versions"
        logger.critical(errMsg)
        raise SystemExit


def main():
    """
    Main function of w9scan when running from command line.
    """
    checkEnvironment() # 检测环境
    setPaths(modulePath()) # 为一些目录和文件设置了绝对路径
    banner()
    
    parser = argparse.ArgumentParser(description="w9scan scanner")
    parser.add_argument("--update", help="update w9scan",action="store_true")
    parser.add_argument("--guide", help="w9scan to guide",action="store_true")
    parser.add_argument("-u", help="url")
    parser.add_argument("-p","--plugin", help="plugins")
    
    args = parser.parse_args()
    urlconfig.mutiurl = False
    urlconfig.url = []
    if args.update:
        updateProgram()
        return 0
    if args.u and args.plugin:
        url = args.u
        if url.startswith("@"):
            urlconfig.mutiurl = True
            fileName = url[1:]
            try:
                o = open(fileName,"r").readlines()
                for u in o:
                    urlconfig.url.append(makeurl(u.strip()))
            except IOError as error:
                logger.critical("Filename:'%s' open faild"%fileName)
                exit()
            if len(o) == 0:
                logger.critical("[xxx] The target address is empty")
                exit()
            print urlconfig.url
        else:
            urlconfig.url.append(makeurl(url))
        
        urlconfig.scanport = False
        urlconfig.find_service = False
        urlconfig.threadNum = 5
        urlconfig.deepMax = 100
        urlconfig.diyPlugin = LIST_PLUGINS
        startTime = time.clock()
        e = Exploit_run(urlconfig.threadNum)
        for u in urlconfig.url:
            print('[***] ScanStart Target:%s' % u)
            e.setCurrentUrl(u)
            e.load_modules(args.plugin,u)
            e.run()
            time.sleep(0.01)
        endTime = time.clock()
        urlconfig.runningTime = endTime - startTime
        e.report()
        return 0
    try:
        inputUrl = raw_input('[1] Input url > ')
        
        if inputUrl is '':
            logger.critical("[xxx] You have to enter the url")
            exit()
        if inputUrl.startswith("@"):
            urlconfig.mutiurl = True
            fileName = inputUrl[1:]
            try:
                o = open(fileName,"r").readlines()
                for url in o:
                    urlconfig.url.append(makeurl(url.strip()))
            except IOError as error:
                logger.critical("Filename:'%s' open faild"%fileName)
                exit()
            if len(o) == 0:
                logger.critical("[xxx] The target address is empty")
                exit()
            print urlconfig.url
        else:
            urlconfig.url.append(makeurl(inputUrl))
        print '[***] URL has been loaded:%d' % len(urlconfig.url)
        print("[Tips] You can select these plugins (%s) or select all"%(' '.join(LIST_PLUGINS)))
        diyPlugin = raw_input("[2] Please select the required plugins > ")

        if diyPlugin.lower() == 'all':
            urlconfig.diyPlugin = LIST_PLUGINS
        else:
            urlconfig.diyPlugin = diyPlugin.strip().split(' ')
        print "[***] You select the plugins:%s"%(' '.join(urlconfig.diyPlugin))    
        urlconfig.scanport = False
        urlconfig.find_service = False
        if 'find_service' in urlconfig.diyPlugin:
            urlconfig.find_service = True
            input_scanport = raw_input('[2.1] Need you scan all ports ?(Y/N) (default N)> ')
            if input_scanport.lower() in ("y","yes"):
                urlconfig.scanport = True
        
        urlconfig.threadNum = raw_input('[3] You need start number of thread (default 5) > ')
        if urlconfig.threadNum == '':
            urlconfig.threadNum = 5

        urlconfig.threadNum = int(urlconfig.threadNum)
        urlconfig.deepMax = raw_input('[4] Set the depth of the crawler (default 200 | 0 don\'t use crawler ) > ')
        if urlconfig.deepMax == '':
            urlconfig.deepMax = 100

        startTime = time.clock()
        e = Exploit_run(urlconfig.threadNum)

        for url in urlconfig.url:
            print('[***] ScanStart Target:%s' % url)
            e.setCurrentUrl(url)
            e.load_modules("www",url)
            e.run()
            if not urlconfig.mutiurl:
                e.init_spider()
                s = crawler.SpiderMain(url)
                s.craw()
            time.sleep(0.01)

        endTime = time.clock()
        urlconfig.runningTime = endTime - startTime
        e.report()
        
    except KeyboardInterrupt:
        print("[***] User Interrupt")
        exit()
    except Exception as info:
        logger.critical("[xxx] MainError: %s:%s"%(str(Exception),info))
        data = e.buildHtml.getData()
        aax = "error:%s urlconfig:%s date:%s"%(str(Exception) + " " + str(info),str(urlconfig),data)
        createIssueForBlog(aax)
        exit()

if __name__ == '__main__':
    main()
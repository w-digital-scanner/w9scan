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
from lib.core.common import Banner,makeurl
import os
import inspect,time
from distutils.version import LooseVersion
from lib.core.settings import VERSION,LIST_PLUGINS,IS_WIN
from lib.core.data import urlconfig,logger
from lib.core.exploit import Exploit_run
from lib.core.option import initOption
from thirdparty.colorama.initialise import init as winowsColorInit
from lib.core.common import createIssueForBlog,systemQuit,printMessage
from lib.core.engine import pluginScan,webScan
from lib.core.exception import ToolkitUserQuitException
from lib.core.exception import ToolkitMissingPrivileges
from lib.core.exception import ToolkitSystemException,ToolkitPluginException

import argparse,multiprocessing
from lib.core.enums import EXIT_STATUS

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
    
    parser = argparse.ArgumentParser(description="w9scan scanner")
    parser.add_argument("--update", help="update w9scan",action="store_true")
    parser.add_argument("--guide", help="w9scan to guide",action="store_true")
    parser.add_argument("--banner", help="output the banner",action="store_true")
    parser.add_argument("-u", help="url")
    parser.add_argument("-p","--plugin", help="plugins")
    parser.add_argument("-s","--search",help="find infomation of plugin")
    parser.add_argument("--debug",help="output debug info",action="store_true",default = False)
    args = parser.parse_args()

    if IS_WIN:
        winowsColorInit()
    Banner()
    initOption(args)
    
    try:
        pluginScan()
        webScan()

    except ToolkitMissingPrivileges, e:
        logger.error(e)
        systemQuit(EXIT_STATUS.ERROR_EXIT)

    except ToolkitSystemException, e:
        logger.error(e)
        systemQuit(EXIT_STATUS.ERROR_EXIT)

    except ToolkitUserQuitException:
        systemQuit(EXIT_STATUS.USER_QUIT)

    except ToolkitPluginException,e:
        createIssueForBlog(e)
        logger.warning('It seems like you reached a unhandled exception, We have automatically uploaded the exception information, please wait for a later update.')

    except KeyboardInterrupt:
        systemQuit(EXIT_STATUS.USER_QUIT)

    except Exception as info:
        logger.warning("error:%s "%(str(Exception) + " " + str(info)))
        logger.warning('It seems like you reached a unhandled exception, please report it to author\'s mail:<master@hacking8.com> or raise a issue via:<https://github.com/boy-hacl/w9scan/issues/new>.')

if __name__ == '__main__':
    main()
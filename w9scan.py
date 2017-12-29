#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: w8ay
# @Date:   2017年12月17日 19:21:35

import sys

sys.dont_write_bytecode = True  # 不生成pyc文件
from lib.core.common import weAreFrozen
from lib.core.common import getUnicode
from lib.core.common import setPaths
from lib.core.common import makeurl
from lib.core.common import banner
from lib.core.log import logger
import os
import inspect
from distutils.version import LooseVersion
from lib.core.settings import VERSION
from lib.core.data import urlconfig
from lib.core.exploit import Exploit_run
from lib.utils import crawler

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
    try:
        checkEnvironment() # 检测环境
        setPaths(modulePath()) # 为一些目录和文件设置了绝对路径
        banner()

        urlconfig.url = raw_input('Input url > ')
        urlconfig.url = makeurl(urlconfig.url)

        urlconfig.scanport = False
        input_scanport = raw_input('Need scan all ports ?(Y/N) (default N)> ')
        if input_scanport.lower() in ("y","yes"):
            urlconfig.scanport = True

        
        urlconfig.threadNum = raw_input('You need start number of thread(Recommendation number is 5) > ')
        urlconfig.threadNum = int(urlconfig.threadNum)

        e = Exploit_run(urlconfig.threadNum)
        print '[***] ScanStart Target:%s' % urlconfig.url
        # e.load_modules("www",urlconfig.url)
        # e.run()
        e.init_spider()
        s = crawler.SpiderMain(urlconfig.url)
        s.craw()
        logger.report()
    except KeyboardInterrupt:
        logger.critical("[***] User Interrupt")
        exit()
    except Exception as info:
        print info
        exit()


if __name__ == '__main__':
    main()
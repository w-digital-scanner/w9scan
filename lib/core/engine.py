#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/boy-hack/w9scan
# author = w8ay
from lib.core.data import logger,urlconfig
import time,sys
from lib.core.exploit import Exploit_run
from lib.core.settings import LIST_PLUGINS
from lib.core.common import printMessage
from lib.utils import crawler

def pluginScan():
    if not urlconfig.mutiurl:
        return False
    urlconfig.scanport = False
    urlconfig.find_service = False
    urlconfig.threadNum = 5
    urlconfig.deepMax = 100
    urlconfig.diyPlugin = LIST_PLUGINS
    startTime = time.clock()
    e = Exploit_run(urlconfig.threadNum)
    for u in urlconfig.url:
        logger.info('ScanStart Target:%s' % u)
        e.setCurrentUrl(u)
        e.load_modules(urlconfig.plugin,u)
        e.run()
        time.sleep(0.01)
    endTime = time.clock()
    urlconfig.runningTime = endTime - startTime
    e.report()
    sys.exit()

def webScan():
    startTime = time.clock()
    e = Exploit_run(urlconfig.threadNum)

    for url in urlconfig.url:
        logger.info('ScanStart Target:%s' % url)
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
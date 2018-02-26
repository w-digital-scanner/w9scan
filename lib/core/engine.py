#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/boy-hack/w9scan
# author = w8ay
from lib.core.data import logger,urlconfig
import time,sys
from lib.core.exploit import Exploit_run
from lib.core.settings import LIST_PLUGINS
from lib.core.common import printMessage

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
        printMessage('[***] ScanStart Target:%s' % u)
        e.setCurrentUrl(u)
        e.load_modules(urlconfig.plugin,u)
        e.run()
        time.sleep(0.01)
    endTime = time.clock()
    urlconfig.runningTime = endTime - startTime
    e.report()
    sys.exit()
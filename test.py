# coding:utf-8
from lib.core.exploit import Exploit_run
from lib.utils import crawler
from w9scan import checkEnvironment,setPaths,modulePath
from lib.core.data import urlconfig

url = 'https://blog.hacking8.com/'
urlconfig.url = url
urlconfig.scanport = False
checkEnvironment() # 检测环境
setPaths(modulePath()) # 为一些目录和文件设置了绝对路径
e = Exploit_run(5)
e.init_spider()
s = crawler.SpiderMain(url)
s.craw()
e.report()
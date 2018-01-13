# coding:utf-8
from lib.core.data import urlconfig

try:
    urlconfig.url = "aaa"
    urlconfig.aa = "zzz"
    raise Exception
except:
    print str(urlconfig)
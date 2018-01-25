# coding:utf-8
from lib.core.data import urlconfig

# Selectable list of plugins
LIST_PLUGINS = ["subdomain","find_service","whatcms","struts"]
b = ['subdomain']
remove_plugins = list(set(LIST_PLUGINS).difference(set(b))) # b中有而a中没有的
print remove_plugins

print 'find_service' in remove_plugins
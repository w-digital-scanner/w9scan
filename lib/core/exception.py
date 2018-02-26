#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ReadPluginsException(Exception):
    pass

class LoadPluginException(Exception):
    pass

class LoadModuleException(Exception):
    pass

class BuildHtmlErrorException(Exception):
    pass

class SaveReportException(Exception):
    pass

class ToolkitBaseException(Exception):
    pass

class ToolkitDataException(ToolkitBaseException):
    pass

class ToolkitMissingPrivileges(ToolkitBaseException):
    pass

class ToolkitUserQuitException(ToolkitBaseException):
    pass

class ToolkitSystemException(ToolkitBaseException):
    pass

class ToolkitValueException(ToolkitBaseException):
    pass

class ToolkitPluginException(ToolkitBaseException):
    pass
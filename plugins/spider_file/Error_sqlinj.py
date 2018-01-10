#!/usr/bin/env python
#-*- coding:utf-8 -*-
# 寻找SQL报错语句

from dummy import *
import urlparse
import hashlib
from urllib import quote as urlencode
from urllib import unquote as urldecode
import re
import os

class dbms:
    DB2 = 'IBM DB2 database'
    MSSQL = 'Microsoft SQL database'
    ORACLE = 'Oracle database'
    SYBASE = 'Sybase database'
    POSTGRE = 'PostgreSQL database'
    MYSQL = 'MySQL database'
    JAVA = 'Java connector'
    ACCESS = 'Microsoft Access database'
    INFORMIX = 'Informix database'
    INTERBASE = 'Interbase database'
    DMLDATABASE = 'DML Language database'
    UNKNOWN = 'Unknown database'

def md5(src):
    m2 = hashlib.md5()
    m2.update(src)
    return m2.hexdigest()

def assign(service, arg):
    if service == 'spider_file':
        return True, arg

def audit(url,html):
    parse = urlparse.urlparse(url)
    if not parse.query:
        return

    for path in parse.query.split('&'):
        if '=' not in path:
            continue
        k, v = path.split('=')
        quotes = '\''
        try:
            url_1 = url.replace("%s=%s"%(k,v),"%s=%s"%(k,urlencode(v + quotes)))
            code, head, html2, redirect_url, log = hackhttp.http(url_1)
            for sql_regex, dbms_type in Get_sql_errors():
                match1 = sql_regex.search(html)
                match2 = sql_regex.search(html2)
                if  match2 and not match1 :
                    msg = 'A SQL error was found in the response supplied by the web application,'
                    msg += match2.group(0)  + '". The error was found '
                    #res.append( (sql_regex, match.group(0), dbms_type) )
                    security_hole(log["request"].replace(os.linesep,'</br>'),"Error_sqlinj dbms_type:%s url:%s"%(dbms_type,url,match2.group(0)))
        except Exception,e:
            print e
            
            

def Get_sql_errors():
    errors = []
    # ASP / MSSQL
    errors.append( ('System\.Data\.OleDb\.OleDbException', dbms.MSSQL ) )
    errors.append( ('\\[SQL Server\\]', dbms.MSSQL ) )
    errors.append( ('\\[Microsoft\\]\\[ODBC SQL Server Driver\\]', dbms.MSSQL ) )
    errors.append( ('\\[SQLServer JDBC Driver\\]', dbms.MSSQL ) )
    errors.append( ('\\[SqlException', dbms.MSSQL ) )
    errors.append( ('System.Data.SqlClient.SqlException', dbms.MSSQL ) )
    errors.append( ('Unclosed quotation mark after the character string', dbms.MSSQL ) )
    errors.append( ("'80040e14'", dbms.MSSQL ) )
    errors.append( ('mssql_query\\(\\)', dbms.MSSQL ) )
    errors.append( ('odbc_exec\\(\\)', dbms.MSSQL ) )
    errors.append( ('Microsoft OLE DB Provider for ODBC Drivers', dbms.MSSQL ))
    errors.append( ('Microsoft OLE DB Provider for SQL Server', dbms.MSSQL ))
    errors.append( ('Incorrect syntax near', dbms.MSSQL ) )
    errors.append( ('Sintaxis incorrecta cerca de', dbms.MSSQL ) )
    errors.append( ('Syntax error in string in query expression', dbms.MSSQL ) )
    errors.append( ('ADODB\\.Field \\(0x800A0BCD\\)<br>', dbms.MSSQL ) )
    errors.append( ("Procedure '[^']+' requires parameter '[^']+'", dbms.MSSQL ))
    errors.append( ("ADODB\\.Recordset'", dbms.MSSQL ))
    errors.append( ("Unclosed quotation mark before the character string", dbms.MSSQL ))
    
    # DB2
    errors.append( ('SQLCODE', dbms.DB2 ) )
    errors.append( ('DB2 SQL error:', dbms.DB2 ) )
    errors.append( ('SQLSTATE', dbms.DB2 ) )
    errors.append( ('\\[IBM\\]\\[CLI Driver\\]\\[DB2/6000\\]', dbms.DB2 ) )
    errors.append( ('\\[CLI Driver\\]', dbms.DB2 ) )
    errors.append( ('\\[DB2/6000\\]', dbms.DB2 ) )
    
    # Sybase
    errors.append( ("Sybase message:", dbms.SYBASE ) )
    
    # Access
    errors.append( ('Syntax error in query expression', dbms.ACCESS ))
    errors.append( ('Data type mismatch in criteria expression.', dbms.ACCESS ))
    errors.append( ('Microsoft JET Database Engine', dbms.ACCESS ))
    errors.append( ('\\[Microsoft\\]\\[ODBC Microsoft Access Driver\\]', dbms.ACCESS ) )
    
    # ORACLE
    errors.append( ('(PLS|ORA)-[0-9][0-9][0-9][0-9]', dbms.ORACLE ) )
    
    # POSTGRE
    errors.append( ('PostgreSQL query failed:', dbms.POSTGRE ) )
    errors.append( ('supplied argument is not a valid PostgreSQL result', dbms.POSTGRE ) )
    errors.append( ('pg_query\\(\\) \\[:', dbms.POSTGRE ) )
    errors.append( ('pg_exec\\(\\) \\[:', dbms.POSTGRE ) )
    
    # MYSQL
    errors.append( ('supplied argument is not a valid MySQL', dbms.MYSQL ) )
    errors.append( ('Column count doesn\'t match value count at row', dbms.MYSQL ) )
    errors.append( ('mysql_fetch_array\\(\\)', dbms.MYSQL ) )
    errors.append( ('mysql_', dbms.MYSQL ) )
    errors.append( ('on MySQL result index', dbms.MYSQL ) )
    errors.append( ('You have an error in your SQL syntax;', dbms.MYSQL ) )
    errors.append( ('You have an error in your SQL syntax near', dbms.MYSQL ) )
    errors.append( ('MySQL server version for the right syntax to use', dbms.MYSQL ) )
    errors.append( ('\\[MySQL\\]\\[ODBC', dbms.MYSQL ))
    errors.append( ("Column count doesn't match", dbms.MYSQL ))
    errors.append( ("the used select statements have different number of columns", dbms.MYSQL ))
    errors.append( ("Table '[^']+' doesn't exist", dbms.MYSQL ))

    
    # Informix
    errors.append( ('com\\.informix\\.jdbc', dbms.INFORMIX ))
    errors.append( ('Dynamic Page Generation Error:', dbms.INFORMIX ))
    errors.append( ('An illegal character has been found in the statement', dbms.INFORMIX ))
    
    errors.append( ('<b>Warning</b>:  ibase_', dbms.INTERBASE ))
    errors.append( ('Dynamic SQL Error', dbms.INTERBASE ))
    
    # DML
    errors.append( ('\\[DM_QUERY_E_SYNTAX\\]', dbms.DMLDATABASE ))
    errors.append( ('has occurred in the vicinity of:', dbms.DMLDATABASE ))
    errors.append( ('A Parser Error \\(syntax error\\)', dbms.DMLDATABASE ))
    
    # Java
    errors.append( ('java\\.sql\\.SQLException', dbms.JAVA ))
    errors.append( ('Unexpected end of command in statement', dbms.JAVA ))

    # Coldfusion
    errors.append( ('\\[Macromedia\\]\\[SQLServer JDBC Driver\\]', dbms.MSSQL ))
    
    # Generic errors..
    errors.append( ('SELECT .*? FROM .*?', dbms.UNKNOWN ))
    errors.append( ('UPDATE .*? SET .*?', dbms.UNKNOWN ))
    errors.append( ('INSERT INTO .*?', dbms.UNKNOWN ))
    errors.append( ('Unknown column', dbms.UNKNOWN ))
    errors.append( ('where clause', dbms.UNKNOWN ))
    errors.append( ('SqlServer', dbms.UNKNOWN ))

    sql_errors = []
    for re_string, dbms_type in errors:
        sql_errors.append((re.compile(re_string, re.IGNORECASE), dbms_type))
    return sql_errors

if __name__ == '__main__':
    url = "http://testphp.vulnweb.com/listproducts.php?artist=1"
    code, head, html, redirect_url, log = hackhttp.http(url)
    audit(url,html)
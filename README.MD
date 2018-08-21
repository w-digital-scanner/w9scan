## w9scan
> 一款全能型的网站漏洞扫描器，借鉴了各位前辈的优秀代码。内置1200+插件可对网站进行一次规模的检测，功能包括但不限于web指纹检测、端口指纹检测、网站结构分析、各种流行的漏洞检测、爬虫以及SQL注入检测、XSS检测等等，w9scan会自动生成精美HTML格式结果报告。  

[![Python 2.7](https://img.shields.io/badge/python-2.7-yellow.svg)](https://www.python.org/)  [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://github.com/boy-hack/w9scan/blob/master/GPL-2.0)

#### 目标
- Linux/Windos通用
- Python 2 不额外安装第三方库
- 做开源扫描器中的 Top1
- 先让软件work起来，再来优化各种细节
- [版本升级记录](./UPDATELOG.MD)

### Useage
- `python w9scan.py --update` 更新程序
- `python w9scan.py --guide` 向导模式启动w9scan
- `python w9scan.py -u "https://x.hacking8.com" ` 快速扫描网站
- `python w9scan.py -u "https://blog.hacking8.com/" -p emlog` 指定插件扫描网站
- `python w9scan.py -u "@1.txt" -p emlog` 指定插件批量扫描网站
- `python w9scan.py -s emlog` 搜索插件是否存在
- `--banner` 输出banner
- `--debug` 输出调试信息  

[![asciicast](https://asciinema.org/a/4WhO54hcf43fySjxJOLyjczSm.png)](https://asciinema.org/a/4WhO54hcf43fySjxJOLyjczSm)

#### TIPS
- 本人并不崇尚命令行哲学，对于这个是能简则简
- 直接使用`python w9scan.py`即可使用向导模式使用w9scan
- 向导模式中输入URL时可以输入类似`@1.txt`,代表批量扫描1.txt内的URL
- 有关配置线程，超时时间，header头等等参数可以打开config.conf配置
- 使用`-u`参数默认加载`指纹识别` `服务发现`模块，不启用`fuzz` `子域名爆破`等

## Features

- __指纹检测__
	+ 可识别常见网站CMS指纹 (`300`+)
	+ 可识别常见网站框架Frame
	+ 识别常用端口服务指纹  
	+ 检测网站脚本语言
    + 检测操作系统类型
	+ 检测网站防火墙 (WAF)

- __攻击参数__
	+ SQL注入 (基于爬虫)
    + XSS注入 (基于爬虫)
    + 大量Fuzz参数扫描
    + CVE 漏洞
    + `1200+` 指定插件定向攻击，插件支持参见[https://github.com/boy-hack/w9scan/tree/master/plugins](https://github.com/boy-hack/w9scan/tree/master/plugins)
    + `struts` 漏洞集合
    + Shellshock cgi test
    + `heartbeat` 心脏出血
    + IIS解析漏洞
    + IIS Put 漏洞

- __暴力破解__
	+ 备份文件以及目录 (基于爬虫)
	+ 备份文件以及目录 (基于域名)
	+ 常见目录
	+ 常见文件
    + 子域名暴力解析
    + `fckeditor`路径枚举
    + 常见`mdb`数据库枚举
    + `git` `svn` 泄露识别
    + `TOMCAT web.xml` 泄露

- __信息收集__
	+ Emails (基于爬虫)
	+ 私有IP (基于爬虫)
	+ E-mail (基于爬虫)
	+ 检测 Warnings,Fatal Error,...
    + PHP 版本识别
    + IIS 信息泄露
    + IP地址归属地
    + 集成`Wappalyzer`识别脚本
    + `robots.txt` 解析
    + 检测header中不安全头
    + 检测Cookie中不安全因素

## FAQ
- 兼容bugscan插件？  
    程序设计就是通过调用bugscan插件运行的，bugscan插件均为网上收集
- 插件内置吗？  
    内置1300+插件，不断更新中
- 如何交流?  
    email或者开issue都可以，如果想研究代码可以参考下面文章
    1. [http://www.freebuf.com/sectool/162120.html](http://www.freebuf.com/sectool/162120.html)
    2. [https://blog.hacking8.com/?tag=w9scan](https://blog.hacking8.com/?tag=w9scan)

## 免责
w9scan扫描器项目仅用于学习，自检网络安全，禁止用于其他用途。

## Thx
- 感谢一位网友提供了部分bugscan代码
- 爬虫的SQL和XSS模块部分参考 [https://github.com/youmengxuefei/web_vul_scan](https://github.com/youmengxuefei/web_vul_scan)
- 仿照 [POC-T](https://github.com/Xyntax/POC-T/) 代码结构
- 网络访问引擎 [Hackhttp](https://github.com/BugScanTeam/hackhttp/)
- 基于爬虫的备份文件查找 [bcrpscan](https://github.com/secfree/bcrpscan)
- [WebEye](https://github.com/zerokeeper/WebEye/)
- [cobra](https://github.com/wufeifei/cobra)
- [s7scan](https://github.com/jiangsir404/S7scan)
- [WAScan](https://github.com/m4ll0k/WAScan)

## w9scan
> 一款全能型的网站漏洞扫描器，借鉴了各位前辈的优秀代码。内置1200+插件可对网站进行一次规模的检测，功能包括但不限于web指纹检测、端口指纹检测、网站结构分析、各种流行的漏洞检测、爬虫以及SQL注入检测、XSS检测等等，w9scan会自动生成精美HTML格式结果报告。  

[![Python 2.7](https://img.shields.io/badge/python-2.7-yellow.svg)](https://www.python.org/)  [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://github.com/boy-hack/w9scan/blob/master/GPL-2.0)

#### 目标
- Linux/Windos通用
- Python 2 不额外安装第三方库
- 做开源扫描器中的 Top1
- 先让软件work起来，再来优化各种细节
- [版本升级记录](./UPDATELOG.MD)

## TODO List
- [ ] 替换`hackhttp`模块
- [ ] 增加`DNS域泄露`模块
- [ ] 插件编写规则修改，不在使用`security_hole`等消息传递，而是直接`return`即可。
- [ ] 检测识别到脚本语言后，Fuzz采用该脚本后缀
- [ ] 核心并发框架的改动
- [ ] 运行www插件前运行infomation插件信息收集，收集到足够数据保存到_G,在调用_G插件。
- [ ] cms指纹插件优化
- [ ] 增强爬虫后的处理，增加了爬虫后的敏感文件扫描插件，参见cydx
- [ ] 异常处理增强，插件报错后会显示出差的代码位置。
- [ ] sql注入模块集成了sqlmap注入检测器
- [ ] 自动在github上报告错误


github上脑图展示了调用的各种插件。从信息收集到调用。
W9scan是世界第一的漏洞扫描器

加入awvs、appscan的规则库

## 免责
w9scan扫描器项目仅用于学习，自检网络安全，禁止用于其他用途。

## Thx
- 感谢一位朋友提供&四叶草授权的bugscan代码
- 爬虫的SQL和XSS模块部分参考 [https://github.com/youmengxuefei/web_vul_scan](https://github.com/youmengxuefei/web_vul_scan)
- 仿照 [POC-T](https://github.com/Xyntax/POC-T/) 代码结构
- 网络访问引擎 [Hackhttp](https://github.com/BugScanTeam/hackhttp/)
- 基于爬虫的备份文件查找 [bcrpscan](https://github.com/secfree/bcrpscan)
- [WebEye](https://github.com/zerokeeper/WebEye/)
- [cobra](https://github.com/wufeifei/cobra)
- [s7scan](https://github.com/jiangsir404/S7scan)
- [WAScan](https://github.com/m4ll0k/WAScan)
- [ctf-wscan](https://github.com/kingkaki/ctf-wscan)

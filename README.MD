## w9scan
> 一款全能型的网站漏洞扫描器，借鉴了各位前辈的优秀代码。内置1200+插件可对网站进行一次规模的检测，功能包括但不限于web指纹检测、端口指纹检测、网站结构分析、各种流行的漏洞检测、爬虫以及SQL注入检测、XSS检测等等，w9scan会自动生成精美HTML格式结果报告。  

[![Python 2.6|2.7](https://img.shields.io/badge/python-2.6|2.7-yellow.svg)](https://www.python.org/)  [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://github.com/boy-hack/w9scan/blob/master/GPL-2.0)

#### 目标
- Linux/Windos通用
- Python 2 不额外安装第三方库
- 做开源扫描器中的 Top1
- 先让软件work起来，再来优化各种细节
- [版本升级记录](./UPDATELOG)

### Useage
- `python w9scan.py --update` 更新程序
- `python w9scan.py --guide` 向导模式启动w9scan
- `python w9scan.py -u "https://blog.hacking8.com/" -p emlog` 指定插件扫描网站
- `python w9scan.py -u "@1.txt" -p emlog` 指定插件批量扫描网站
- `python w9scan.py -s emlog` 搜索插件是否存在
- `--banner` 输出banner
- `--debug` 输出调试信息

#### TIPS
- 本人并不崇尚命令行哲学，对于这个是能简则简
- 直接使用`python w9scan.py`即可使用向导模式使用w9scan
- 向导模式中输入URL时可以输入类似`@1.txt`,代表批量扫描1.txt内的URL
- 好多人给我点赞了，受宠若惊，谢谢大家的star，代码说实话有点"丑"，但我会继续学习Python来完善它的

## FAQ
- 兼容bugscan插件？  
    程序设计就是通过调用bugscan插件运行的，bugscan插件均为网上收集
- 插件内置吗？  
    内置1000+插件，不断更新中
- 感觉没有想象中的好用啊  
    倒是说说你想怎么好用呀？
- 一千多个脚本对目标站轮训？  
    先调用`www`服务的插件，由这些插件在调用其他插件`指纹识别` `端口服务识别`等。
- 与w8scan的关系？  
    为w8scan的扫描器代码探路
- 如何交流?  
    email或者开issue都可以，如果想研究代码可以参考下面文章
    1. [http://www.freebuf.com/sectool/162120.html](http://www.freebuf.com/sectool/162120.html)
    2. [https://blog.hacking8.com/?tag=w9scan](https://blog.hacking8.com/?tag=w9scan)

## 免责
w9scan扫描器项目仅用于学习，禁止用于其他用途。

## Thx
- 感谢一位网友提供了部分bugscan代码
- 爬虫的SQL和XSS模块部分参考 [https://github.com/youmengxuefei/web_vul_scan](https://github.com/youmengxuefei/web_vul_scan)
- 仿照 [POC-T](https://github.com/Xyntax/POC-T/) 代码结构
- 网络访问引擎 [Hackhttp](https://github.com/BugScanTeam/hackhttp/)
- 基于爬虫的备份文件查找 [bcrpscan](https://github.com/secfree/bcrpscan)
- [WebEye](https://github.com/zerokeeper/WebEye/)
- [cobra](https://github.com/wufeifei/cobra)

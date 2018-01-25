## w9scan
一款全能型的扫描器，吸收各位前辈的优秀代码。因看不惯某喷子，项目曾删除过一次，但现在觉得没有必要斤斤计较。开心就好~ 希望大家不要关注，我想默默写代码想干嘛就干嘛，不喜欢一堆人关注我，修改代码起来需要特别谨慎，每次commit都要写注释好麻烦~1

#### 目标
- Linux/Windos通用
- python不额外安装第三方库
- 做开源扫描器中的 Top1
- 先让软件work起来，再来优化各种细节！

## 升级记录
- 接下来要做的: 扫描器架构简介，插件编写指南 优化各种插件性能，效率，以及精准度

- 1.6.2 对主程序逻辑优化，优化时间计算
- 1.6.1 可自定义配置需要扫描的模块(子域名 端口 CMS识别 struts)
- 1.6.0 实现了生成html格式报告(超酷的报告) html借用了 [cobra](https://github.com/wufeifei/cobra)
- 1.5.0 实现了子域名解析爆破(用特殊的方法10行代码完成 hO(∩_∩)Oh) 可以看文件`subdomain.py`
- 1.4.3 加入了WAF/CDN探测模块`waf_identify.py` 感谢[WebEye](https://github.com/zerokeeper/WebEye/)的代码以及指纹信息
- 1.4.2 加入爬虫的备份文件探测模块 参考[bcrpscan](https://github.com/secfree/bcrpscan)
- 1.4.1 完成了爬虫的`信息收集`模块和`XSS`扫描模块 ，SQL注入以及XSS扫描代码参考[https://github.com/youmengxuefei/web_vul_scan](https://github.com/youmengxuefei/web_vul_scan)
- 元旦了，祝自己快乐
- 1.4.0 完成爬虫模块[单线程] 完成`sql注入`模块 包含`int注入` `字符注入` `报错查找`
- 1.3.3 解决了程序异常，去掉了老的线程池，改用了[POC-T](https://github.com/Xyntax/POC-T/blob/2.0/lib/controller/engine.py)的线程引擎
- 1.3.2 分类了exp文件夹，使整理更方便
- 1.3.1 部分插件加入了线程池，使速度更快了 添加了部分插件
- 1.3 加入线程池，使速度更快了  内置buildtwitch分析网站结构
- 1.2 加入了IP端口服务识别，对IP开放端口定向识别并破解
- 1.1 扫描器雏形，指纹识别雏形

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
    ![](https://github.com/boy-hack/w9scan/blob/master/images/qqgroup.png)  
    特意成立了QQ群用于交流，qq群仅发布在github，我想尽量维护一个交流的氛围

## 免责
w9scan扫描器项目仅用于学习，禁止用于其他用途。

## 运行测试

用`w9scan 1.6.0` 扫描 http://testphp.vulnweb.com/ 的扫描报告生成在`vulnweb.com_1515587017.html`可自行查看
![](https://github.com/boy-hack/w9scan/blob/master/images/report.png)


## Useage
python w9scan.py

## Thx
- 感谢一位网友提供了部分bugscan代码
- 爬虫的SQL和XSS模块部分参考 [https://github.com/youmengxuefei/web_vul_scan](https://github.com/youmengxuefei/web_vul_scan)
- 线程控制参考 [POC-T](https://github.com/Xyntax/POC-T/blob/2.0/lib/controller/engine.py)
- 网络访问引擎 [Hackhttp](https://github.com/BugScanTeam/hackhttp/)
- 基于爬虫的备份文件查找 [bcrpscan](https://github.com/secfree/bcrpscan)
- [WebEye](https://github.com/zerokeeper/WebEye/)
- [cobra](https://github.com/wufeifei/cobra)
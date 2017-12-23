## w9scan
本地完美调用bugscan的插件运行的扫描器

## Requirement
- require python 2.7
- 不需要安装其他第三方库
- 支持Windos/Linux  win10 Ubuntu 测试成功

## 升级记录
- 接下来要做的: 爬虫模块 WAF/CDN探测模块
- 1.3 加入线程池，使速度更快了
- 1.2 加入了IP端口服务识别，对IP开放端口定向识别并破解
- 1.1 扫描器雏形，指纹识别雏形

## FAQ
- 兼容bugscan插件？  
    程序设计就是通过调用bugscan插件运行的，bugscan插件均为网上收集
- 插件内置吗？  
    内置1000+插件
- 感觉没有想象中的好用啊  
    不断完善中，欢迎提出建议
- 需要登录账号么？  
    逗我笑吗? 。。
- 一千多个脚本对目标站轮训？  
    先调用`www`服务的插件，由这些插件在调用其他插件`指纹识别` `端口服务识别`等。

## 免责
w9scan扫描器项目仅用于学习，其他目的一概不允许。

## 运行测试
### Linux 
![](https://github.com/boy-hack/w9scan/blob/master/linux1.png)
![](https://github.com/boy-hack/w9scan/blob/master/linux2.png)
### Win
![](https://github.com/boy-hack/w9scan/blob/master/win1.png)
![](https://github.com/boy-hack/w9scan/blob/master/win2.png)
## Useage
python w9scan.py

## Thx
- 感谢一位网友提供了部分bugscan代码
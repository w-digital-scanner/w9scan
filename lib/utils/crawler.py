# coding:utf-8
# 爬虫模块，如何调用相关爬虫模块?
# 爬到的文件丢给任务'spider_file' 爬虫完丢给任务`spider_end`

import urlparse
import re
from thirdparty import hackhttp
from lib.core.data import w9_hash_pycode,logger
from lib.utils import until
from lib.core.data import urlconfig

req = hackhttp.hackhttp()

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

class SpiderMain(object):

    def __init__(self,root):
        self.urls = UrlManager()
        self.root = root
        self.deep = 0
        self.maxdeep = urlconfig.deepMax # Max deep
        self.SIMILAR_SET = set()
        self.domain = urlparse.urlparse(root).netloc
        self.IGNORE_EXT = ['css','js','jpg','png','gif','rar','pdf','doc']
#不期待的文件后缀

    def craw(self):
        self.urls.add_new_url(self.root)
        while self.urls.has_new_url() and self.maxdeep>self.deep and self.maxdeep > 0:
            new_url = self.urls.get_new_url()
            logger.debug("craw:" + new_url)
            try:
                html = until.w9_get(new_url)
                check(new_url,html)
            except:
                html = ''
            new_urls = self._parse(new_url, html)
            self.urls.add_new_urls(new_urls)
            self.deep = self.deep + 1

    def _parse(self, page_url, content):
        if content is None:
            return
        webreg = re.compile('''<a[^>]+href=["\'](.*?)["\']''', re.IGNORECASE)
        urls = webreg.findall(content)
        _news = self._get_new_urls(page_url, urls)
        return _news

    def _judge(self, url):
        netloc = urlparse.urlparse(url).netloc
        if (self.domain != netloc):
            return False
        if(self.url_similar_check(url) is False):
            return False
        # 指定后缀判断
        ext = urlparse.urlparse(url)[2].split('.')[-1]
        if ext in self.IGNORE_EXT:
            return False
        return True

    def url_similar_check(self, url):
        '''
        URL相似度分析
        当url路径和参数键值类似时，则判为重复
        '''
        url_struct = urlparse.urlparse(url)
        query_key = '|'.join(sorted([i.split('=')[0] for i in url_struct.query.split('&')]))
        url_hash = hash(url_struct.path + query_key)
        if url_hash not in self.SIMILAR_SET:
            self.SIMILAR_SET.add(url_hash)
            return True
        return False

    def _get_new_urls(self, page_url, links):
        new_urls = set()
        for link in links:
            new_url = link
            new_full_url = urlparse.urljoin(page_url, new_url)
            if (self._judge(new_full_url)):
                new_urls.add(new_full_url)
        return new_urls

def check(url,html = ''):
    for k, v in w9_hash_pycode.iteritems():
        try:
            pluginObj = v["pluginObj"]
            service = v["service"]
            if(service == "spider_file"):
                pluginObj.audit(url,html)
        except Exception as errinfo:
            logger.error("spider plugin:%s errinfo:%s url:%s"%(k,errinfo,url))

def check_end():
    for k, v in w9_hash_pycode.iteritems():
        try:
            pluginObj = v["pluginObj"]
            service = v["service"]
            if(service == "spider_end"):
                pluginObj.audit()
        except:
            pass

if __name__ == '__main__':
    u = "http://testphp.vulnweb.com/index.php"
    s = SpiderMain(u)
    s.craw()
